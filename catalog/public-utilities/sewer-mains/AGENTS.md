# AGENTS.md — Sewer Mains

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-mains/sewer-mains.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

21 columns, 16,250 rows.

| column | type |
| --- | --- |
| `Agency` | string |
| `PipeDiam` | double |
| `PipeType` | string |
| `Type` | string |
| `InstYear` | double |
| `ID` | string |
| `SLOPE` | double |
| `FROM_INV` | double |
| `TO_INV` | double |
| `Up_MH` | string |
| `Down_Mh` | string |
| `NumConnect` | int16 |
| `Shape` | binary |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `Shape.len` | double |
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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-mains/sewer-mains.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Agency", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-mains/sewer-mains.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `South Valley Sewer District` — 5,378
- `Cottonwood Improvement District` — 5,263
- `Sandy Suburban Improvement District` — 3,766
- `Midvalley Improvement District` — 1,843

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/2](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/2) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
