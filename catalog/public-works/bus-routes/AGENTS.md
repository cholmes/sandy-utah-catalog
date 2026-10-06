# AGENTS.md — UTA Bus Routes

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/bus-routes/bus-routes.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

10 columns, 49 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `frequency` | string |
| `routetype` | string |
| `avgbrd` | int32 |
| `city` | string |
| `county` | string |
| `Shape` | binary |
| `Shape.STLength()` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/bus-routes/bus-routes.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "routetype", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/bus-routes/bus-routes.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Regular` — 34
- `Frequent` — 9
- `Limited` — 5
- `Ski` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/UTA_Routes/MapServer/5](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/UTA_Routes/MapServer/5) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
