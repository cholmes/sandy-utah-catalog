# AGENTS.md — Storm Detention Ponds

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/detention-ponds/detention-ponds.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

23 columns, 210 rows.

16 of 23 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`NAME`** — *string*  
Name of the feature. Measured in the published file: Populated on 56% of 210 rows, 95 distinct values.

**`ADDRESS`** — *string*  
Street address of the feature. Measured in the published file: Populated on 27% of 210 rows, 51 distinct values.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`FACILITYID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 210 rows, 210 distinct values.

**`OWNERSHIP`** — *string*  
Who owns the asset. Sandy's utility layers include assets owned by other cities, the county, UDOT and private parties. Measured in the published file: Populated on 98% of 210 rows, 6 distinct values.

**`MaintRating`** — *string*  
Maintenance condition rating assigned at the last inspection. The source layer declares no code list, so the scale is not documented. Measured in the published file: Populated on 17% of 210 rows, 3 distinct values.

**`FrameGrate`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 1 distinct values.

**`StructCond`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 1 distinct values.

**`FloorBench`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 1 distinct values.

**`InspDate`** — *timestamp[ms]*  
Date of the most recent inspection. Measured in the published file: Populated on 17% of 210 rows, 36 distinct values.

**`MaintSched`** — *string*  
How often the asset is scheduled for maintenance. Measured in the published file: Populated on 19% of 210 rows, 1 distinct values.

**`DamGopher`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 2 distinct values.

**`DamSinkHoles`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 1 distinct values.

**`SpillwayGopher`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 2 distinct values.

**`SpillwaySinkHoles`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 210 rows, 1 distinct values.

**`TYPE`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 98% of 210 rows, 4 distinct values.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`TYPE` — Detention or Retention**

- `Detention` = Detention
- `Retention` = Retentioun
- `Underground Detention` = Underground Detention
- `Underground Retention` = Underground Retention

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/detention-ponds/detention-ponds.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/7](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/7?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
