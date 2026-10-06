# AGENTS.md — Street and Park Trees

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/street-trees/street-trees.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

26 columns, 7,966 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Address` | string |
| `Species` | string |
| `Other_Spec` | string |
| `Tree_ID_` | int32 |
| `Caliper` | string |
| `Height` | string |
| `Condition` | string |
| `Max_PDOP` | double |
| `Collection_date` | timestamp[ms] |
| `Status` | string |
| `Comments` | string |
| `Photo` | string |
| `AssetID` | string |
| `Location` | string |
| `Disease_Abiotic` | string |
| `Disease_Biotic` | string |
| `Disease_Comment` | string |
| `Disease_Date` | timestamp[ms] |
| `Hazard` | string |
| `Hazard_Date` | timestamp[ms] |
| `Pruning_Needs` | string |
| `Pruning_Date` | timestamp[ms] |
| `Tree_Value` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/street-trees/street-trees.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Grounds_and_Forestry/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Grounds_and_Forestry/FeatureServer/0) on 2026-10-06T20:37:26Z.
Sandy City publishes no licence for this data; see the [README](README.md).
