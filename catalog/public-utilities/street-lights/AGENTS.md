# AGENTS.md — Street Lights

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/street-lights/street-lights.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

34 columns, 8,727 rows.

24 of 34 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`POLE_NUM`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,727 rows, 8,451 distinct values, ranging 0 to 1.1402e+08.

**`COMMENTS`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`GPS_DATE`** — *timestamp[ms]*  
Date the location was captured by GPS in the field. Measured in the published file: Populated on 93% of 8,727 rows, 554 distinct values.

**`NORTHING`** — *double*  
Y coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`EASTING`** — *double*  
X coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`JURISDICTI`** — *string*  
Jurisdiction. Measured in the published file: Populated on 98% of 8,727 rows, 4 distinct values.

**`FIXTURE_TY`** — *string*  
Fixture Type. Measured in the published file: Populated on 100% of 8,727 rows, 11 distinct values.

**`LAMP_TYPE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 8,727 rows, 5 distinct values.

**`WATTS`** — *double*  
Watts (1). Measured in the published file: Populated on 100% of 8,727 rows, 45 distinct values, ranging 15 to 300.

**`LUMEN`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 80% of 8,727 rows, 23 distinct values, ranging 0 to 50000.

**`NUM_HEADS`** — *int32*  
# Heads. Measured in the published file: Populated on 99% of 8,727 rows, 2 distinct values, ranging 1 to 2.

**`RATE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,727 rows, 2 distinct values.

**`POLE_TYPES`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 8,727 rows, 23 distinct values.

**`FEATURE_ID`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 8,727 rows, 8,459 distinct values, ranging 7143 to 4.45574e+06.

**`DATE_INSTA`** — *timestamp[ms]*  
Install Date. Measured in the published file: Populated on 94% of 8,727 rows, 1,007 distinct values.

**`POLESUFFIX`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 8,727 rows, 8,366 distinct values, ranging 0 to 3.27076e+06.

**`LOCATION`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 99% of 8,727 rows, 8,015 distinct values.

**`EPOLE_NUM`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,727 rows, 8,450 distinct values.

**`FacilityID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 8,727 rows, 8,723 distinct values.

**`FIXTURE_INSTALL`** — *timestamp[ms]*  
Fixture Install Date. Measured in the published file: Populated on 23% of 8,727 rows, 1,188 distinct values.

**`SANDY_NUMBER`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,727 rows, 8,495 distinct values.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`STATUS`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 100% of 8,727 rows, 4 distinct values.

**`LampInstall`** — *timestamp[ms]*  
Lamp Install Date. Measured in the published file: Populated on 73% of 8,727 rows, 6,262 distinct values.

**`PoleReplace`** — *timestamp[ms]*  
Pole Replace Date. Measured in the published file: Populated on 3% of 8,727 rows, 300 distinct values.

**`WATTS_2`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 2% of 8,727 rows, 5 distinct values, ranging 45 to 105.

**`Lamp_Temperature`** — *string*  
One of. The source layer's domain allows: `4000K`, `3000K`, `NA`.

**`POLE_OWNER`** — *string*  
Coded value. The source layer's domain allows: `Sandy City`, `Rocky Mountain Power`, `Private`, `UDOT`, `Salt Lake County`, `Communications`. Codes: `Sandy City` = Sandy City, `RMP` = Rocky Mountain Power, `Private` = Private, `UDOT` = UDOT, `Salt Lake County` = Salt Lake County, `Communications` = Communications.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

**`POLE_OWNER`**

- `Sandy City` = Sandy City
- `RMP` = Rocky Mountain Power
- `Private` = Private
- `UDOT` = UDOT
- `Salt Lake County` = Salt Lake County
- `Communications` = Communications

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/street-lights/street-lights.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StreetLights/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StreetLights/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
