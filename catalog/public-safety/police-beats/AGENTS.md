# AGENTS.md — Police Beats

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-beats/police-beats.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

7 columns, 4 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `NAME` | string |
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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-beats/police-beats.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "NAME", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-beats/police-beats.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Crescent` — 1
- `Sandy` — 1
- `Alta Canyon` — 1
- `Bell Canyon` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceBeats/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceBeats/MapServer/0) on 2026-10-06T21:15:15Z.
Sandy City publishes no licence for this data; see the [README](README.md).
