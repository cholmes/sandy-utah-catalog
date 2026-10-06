# AGENTS.md — Future Land Use

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3857** (WGS 84 / Pseudo-Mercator). Linear units are **Mercator metres, which are not ground distances away from the equator**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3857', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/future-land-use/future-land-use.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3857 too.

## Schema

6 columns, 979 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Future_Land_Use` | string |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/future-land-use/future-land-use.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Future_Land_Use", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/future-land-use/future-land-use.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `LN` — 343
- `OP` — 143
- `MN` — 143
- `RLN` — 102
- `LC` — 90
- `NAC` — 43
- `HC` — 31
- `HN` — 30
- `CAIRNS` — 21
- `IN` — 17
- `RC` — 16

## Provenance

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Sandy_Future_Land_Use_Map_WFL1/FeatureServer/12](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Sandy_Future_Land_Use_Map_WFL1/FeatureServer/12) on 2026-10-06T19:54:13Z.
Sandy City publishes no licence for this data; see the [README](README.md).
