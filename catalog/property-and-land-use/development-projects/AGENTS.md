# AGENTS.md — Development Projects

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/development-projects/development-projects.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

18 columns, 64 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Project_Name` | string |
| `Description` | string |
| `Address` | string |
| `Project_Type` | string |
| `Key_Words` | string |
| `Case_Number` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `DocumentsLink` | string |
| `Bond` | string |
| `Status` | string |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Project_Type` — Project Type**

- `Subdivision Plat` = Subdivision Plat
- `Site Plan Review` = Site Plan Review
- `Residential` = Residential
- `Special Event` = Special Event
- `Other` = Other

**`Key_Words` — Key Words**

- `Plat` = Plat
- `Site Plan` = Site Plan
- `Deed` = Deed
- `Permit` = Permit
- `Event` = Event
- `Project` = Project
- `Other` = Other

**`Bond`**

- `Not Calc` = Not Calc
- `Waiting` = Waiting
- `Posted` = Posted
- `Warranty` = Warranty
- `Refunded` = Refunded
- `N/A` = N/A

**`Status`**

- `Prelim` = Prelim
- `Review` = Review
- `Final Review` = Final Review
- `Pre-Construct` = Pre-Construct
- `Construction` = Construction
- `Inspection` = Inspection
- `Complete` = Complete
- `N/A` = N/A

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/development-projects/development-projects.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Development_Projects/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Development_Projects/FeatureServer/0) on 2026-10-06T21:15:15Z.
Sandy City publishes no licence for this data; see the [README](README.md).
