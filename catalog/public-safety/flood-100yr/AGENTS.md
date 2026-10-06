# AGENTS.md — Approximate 100-Year Floodplain

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/flood-100yr/flood-100yr.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

25 columns, 828 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `DFIRM_ID` | string |
| `VERSION_ID` | string |
| `FLD_AR_ID` | string |
| `STUDY_TYP` | string |
| `FLD_ZONE` | string |
| `ZONE_SUBTY` | string |
| `SFHA_TF` | string |
| `STATIC_BFE` | double |
| `V_DATUM` | string |
| `DEPTH` | double |
| `LEN_UNIT` | string |
| `VELOCITY` | double |
| `VEL_UNIT` | string |
| `AR_REVERT` | string |
| `AR_SUBTRV` | string |
| `BFE_REVERT` | double |
| `DEP_REVERT` | double |
| `DUAL_ZONE` | string |
| `SOURCE_CIT` | string |
| `Shape` | binary |
| `Shape.STArea()` | double |
| `Shape.STLength()` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/flood-100yr/flood-100yr.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "ZONE_SUBTY", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/flood-100yr/flood-100yr.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- ` ` — 692
- `FLOODWAY` — 136

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Hazards/MapServer/5](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Hazards/MapServer/5) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
