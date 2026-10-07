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

15 of 18 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Project_Name`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 64 rows, 64 distinct values.

**`Description`** — *string*  
Description of the feature, entered by city staff. Measured in the published file: Populated on 56% of 64 rows, 35 distinct values.

**`Address`** — *string*  
Street address of the feature. Measured in the published file: Populated on 95% of 64 rows, 58 distinct values.

**`Project_Type`** — *string*  
One of. The source layer's domain allows: `Subdivision Plat`, `Site Plan Review`, `Residential`, `Special Event`, `Other`.

**`Key_Words`** — *string*  
One of. The source layer's domain allows: `Plat`, `Site Plan`, `Deed`, `Permit`, `Event`, `Project`, `Other`.

**`Case_Number`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 64 rows, 64 distinct values.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`DocumentsLink`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 47% of 64 rows, 30 distinct values.

**`Bond`** — *string*  
One of. The source layer's domain allows: `Not Calc`, `Waiting`, `Posted`, `Warranty`, `Refunded`, `N/A`.

**`Status`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 48% of 64 rows, 6 distinct values.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/development-projects/development-projects.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Development_Projects/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Development_Projects/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
