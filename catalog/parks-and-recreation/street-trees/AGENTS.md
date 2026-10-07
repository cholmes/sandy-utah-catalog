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


**Where these meanings come from.** Public tree inventory maintained by Sandy City Parks and Recreation, collected in the field with GPS.

26 of 26 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Address`** — *string*  
Street address of the feature. Measured in the published file: Populated on 99% of 7,966 rows, 170 distinct values.

**`Species`** — *string*  
Tree species.

**`Other_Spec`** — *string*  
Species written in free text where it is not on the pick list.

**`Tree_ID_`** — *int32*  
Identifier of the tree in the inventory.

**`Caliper`** — *string*  
Trunk diameter, in inches. Arborists measure caliper at a standard height above ground.

**`Height`** — *string*  
Tree height, in feet.

**`Condition`** — *string*  
Condition assessed at the last inspection.

**`Max_PDOP`** — *double*  
Positional dilution of precision at capture. A GPS quality measure where a lower number means a better fix.

**`Collection_date`** — *timestamp[ms]*  
Date the tree was surveyed in the field.

**`Status`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 49% of 7,966 rows, 4 distinct values.

**`Comments`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`Photo`** — *string*  
Reference to a field photograph of the tree.

**`AssetID`** — *string*  
Identifier of the asset in the city's maintenance management system. Measured in the published file: Populated on 99% of 7,966 rows, 7,899 distinct values.

**`Location`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 100% of 7,966 rows, 153 distinct values.

**`Disease_Abiotic`** — *string*  
Non-living stress affecting the tree, such as drought or soil compaction.

**`Disease_Biotic`** — *string*  
Living agent affecting the tree, such as an insect or a fungus.

**`Disease_Comment`** — *string*  
Note on the tree's health.

**`Disease_Date`** — *timestamp[ms]*  
Date the health problem was recorded.

**`Hazard`** — *string*  
Type of hazard mapped. Empty in all 7,966 rows of the published file.

**`Hazard_Date`** — *timestamp[ms]*  
Date the tree was recorded as a hazard.

**`Pruning_Needs`** — *string*  
Pruning the tree requires.

**`Pruning_Date`** — *timestamp[ms]*  
Date the tree was last pruned.

**`Tree_Value`** — *string*  
Appraised value of the tree, in dollars. Municipal tree inventories carry this to support claims when a tree is damaged.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Grounds_and_Forestry/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Grounds_and_Forestry/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
