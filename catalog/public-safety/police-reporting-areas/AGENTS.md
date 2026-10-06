# AGENTS.md — Police Reporting Areas

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566**, NAD83/HARN Utah Central, in **US survey feet**. `ST_Length` and `ST_Area` return feet and square feet, not metres. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/public-safety/police-reporting-areas/police-reporting-areas.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

16 columns, 439 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `OLDAREA` | string |
| `CITY` | string |
| `CITYDESCR` | string |
| `DISP_AREA` | string |
| `DISP_AREA_` | string |
| `TYPE` | string |
| `TYPE_DESC` | string |
| `STATUS` | string |
| `REPT_AREA` | string |
| `ACRES` | double |
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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/public-safety/police-reporting-areas/police-reporting-areas.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Police_Reporting_Areas/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Police_Reporting_Areas/MapServer/1) on 2026-10-06T19:01:44Z.
Sandy City publishes no licence for this data; see the [README](README.md).
