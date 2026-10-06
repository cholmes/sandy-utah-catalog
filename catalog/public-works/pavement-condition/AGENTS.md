# AGENTS.md — Pavement Condition

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/pavement-condition/pavement-condition.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

37 columns, 2,165 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Location` | string |
| `PMA_TXT` | string |
| `Section_Num` | string |
| `Municipality` | string |
| `PWA` | int16 |
| `Council_District` | string |
| `Quadrant` | string |
| `Street_Name` | string |
| `From_Location` | string |
| `To_Location` | string |
| `FunctionClass` | string |
| `GIS_Length` | double |
| `GIS_Width` | double |
| `Avg_SectionWidth` | int16 |
| `RM_Length` | double |
| `RM_Width` | double |
| `RM_Area` | double |
| `Pavement_Type` | string |
| `AADT_Count` | int32 |
| `AADT_Date` | timestamp[ms] |
| `Lanes` | int16 |
| `One_Way` | int16 |
| `PQI` | double |
| `PQI_Date` | timestamp[ms] |
| `Year_Built` | string |
| `Cost_Window` | string |
| `Costs_SqFt` | double |
| `Road_Value` | double |
| `GASB_Class` | string |
| `GASB_Cond_Group` | string |
| `Shape__Length` | double |
| `Date_Built_Annexed` | timestamp[ms] |
| `Road_Source` | string |
| `Maintenance_District` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Road_Source`**

- `Annexation` = Annexation
- `Developer` = Developer
- `City` = City
- `Other` = Other

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/pavement-condition/pavement-condition.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "GASB_Cond_Group", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/pavement-condition/pavement-condition.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Good` — 1,543
- `Fair` — 540
- `Poor` — 48

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/PMA_Segments/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/PMA_Segments/FeatureServer/0) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
