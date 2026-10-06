# AGENTS.md — Sewer Manholes

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-manholes/sewer-manholes.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

19 columns, 16,020 rows.

| column | type |
| --- | --- |
| `Agency` | string |
| `DIAMETER` | double |
| `RIM_ELEV` | double |
| `X` | double |
| `Y` | double |
| `DepthToFlo` | double |
| `NumPipesIn` | int16 |
| `InSizes` | string |
| `OutSize` | string |
| `MH_ID` | string |
| `NumLateral` | int16 |
| `Shape` | binary |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `OBJECTID` | int64 |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Agency`**

- `Cottonwood Improvement District` = Cottonwood Improvement District
- `Midvale City` = Midvale City
- `Midvalley Improvement District` = Midvalley Improvement District
- `Sandy Suburban Improvement District` = Sandy Suburban Improvement District
- `South Valley Sewer District` = South Valley Sewer District
- `Other/Unknown` = Other/Unknown

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-manholes/sewer-manholes.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/1) on 2026-10-06T20:37:26Z.
Sandy City publishes no licence for this data; see the [README](README.md).
