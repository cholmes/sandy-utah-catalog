# AGENTS.md — Zoning Districts

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/zoning/zoning.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

13 columns, 454 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `ZONE` | string |
| `ZONE_ACREA` | double |
| `LEGEND_COD` | string |
| `SD_ZONE` | string |
| `NAME` | string |
| `Definition` | string |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `Editor_Date` | timestamp[ms] |
| `Zone_Code` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/zoning/zoning.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "LEGEND_COD", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/zoning/zoning.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `R2` — 83
- `R3` — 66
- `MF2` — 40
- `R1` — 38
- `MF1` — 30
- `R4` — 28
- `OS1` — 25
- `MF4` — 24
- `PO1` — 22
- `R5` — 14
- `C3` — 11
- `C1` — 10

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Zoning_Ex/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Zoning_Ex/FeatureServer/0) on 2026-10-06T19:21:37Z.
Sandy City publishes no licence for this data; see the [README](README.md).
