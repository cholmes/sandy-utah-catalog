# AGENTS.md — Garbage Collection Days

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/garbage-days/garbage-days.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

8 columns, 5 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `WEEKDAY` | int16 |
| `DAY_NAME` | string |
| `Shape` | binary |
| `Shape.area` | double |
| `Shape.len` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/garbage-days/garbage-days.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "DAY_NAME", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/garbage-days/garbage-days.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Tuesday` — 1
- `Friday` — 1
- `Wednesday` — 1
- `Thursday` — 1
- `Monday` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/GarbageDays/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/GarbageDays/MapServer/0) on 2026-10-06T21:15:15Z.
Sandy City publishes no licence for this data; see the [README](README.md).
