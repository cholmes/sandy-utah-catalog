# AGENTS.md — Water Tanks

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-tanks/water-tanks.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

36 columns, 9 rows.

34 of 36 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`PubUtils.PU.SandyTanks_Points.AREA`** — *double*  
AREA. Measured in the published file: Populated on 78% of 9 rows, 1 distinct values.

**`PERIMETER`** — *double*  
Polygon perimeter carried as an attribute, in the units of the source coordinate system. Recompute from the geometry rather than trusting it. Measured in the published file: Populated on 78% of 9 rows, 1 distinct values.

**`SANDY_TANKS_`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 9 rows, 9 distinct values, ranging 2 to 12.

**`SANDY_TANKS_ID`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 9 rows, 9 distinct values, ranging 2 to 12.

**`TANK_NAME`** — *string*  
Name of the storage tank.

**`LOCATION`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 100% of 9 rows, 9 distinct values.

**`CAPACITY`** — *string*  
Nominal capacity, written with its unit, such as `5 MG` for five million gallons.

**`FLOOR_EL`** — *double*  
Elevation of the tank floor, in feet.

**`GROUND_EL`** — *double*  
Ground elevation at the tank, in feet.

**`OVER_EL`** — *double*  
Overflow elevation, in feet. The difference from ground level sets the pressure the tank delivers.

**`OVER_DEPTH`** — *double*  
Water depth at overflow, in feet.

**`DIMENSIONS`** — *string*  
Physical dimensions of the tank.

**`ZONE_`** — *double*  
Water pressure zone the tank serves, joining to `water-pressure-zones`.

**`CONST_TYPE`** — *string*  
Construction type of the tank, such as concrete or steel.

**`YEAR_CONST`** — *double*  
Year the tank was built.

**`MGCAPACITY`** — *double*  
Capacity in millions of gallons, as a number.

**`ENGINEER`** — *string*  
Engineering firm that designed the tank.

**`CONTRACTOR`** — *string*  
Contractor that built the tank.

**`MAINT_DATE`** — *timestamp[ms]*  
Date of the last recorded maintenance.

**`MAINT_TYPE`** — *string*  
Type of the last recorded maintenance.

**`X_COORD`** — *double*  
X coordinate copied into an attribute. The geometry is authoritative.

**`Y_COORD`** — *double*  
Y coordinate copied into an attribute.

**`FACILITYID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 9 rows, 9 distinct values.

**`POLYGONID`** — *int32*  
Identifier carried over from an earlier coverage format. Measured in the published file: Populated on 78% of 9 rows, 1 distinct values.

**`SCALE`** — *double*  
Cartographic scale the symbol is drawn at on the city's own maps. Measured in the published file: Populated on 78% of 9 rows, 1 distinct values.

**`ANGLE`** — *double*  
Rotation angle of the symbol on the city's own maps. Measured in the published file: Populated on 78% of 9 rows, 1 distinct values.

**`Enabled`** — *int16*  
Coded value. The source layer's domain allows: `False`, `True`. Codes: `0` = False, `1` = True.

**`AncillaryRole`** — *int16*  
Coded value. The source layer's domain allows: `None`, `Source`, `Sink`. Codes: `0` = None, `1` = Source, `2` = Sink.

**`CONST_STATUS`** — *string*  
Construction status of the asset. Measured in the published file: Populated on 11% of 9 rows, 1 distinct values.

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

**`Enabled`**

- `0` = False
- `1` = True

**`AncillaryRole`**

- `0` = None
- `1` = Source
- `2` = Sink

**`CONST_STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-tanks/water-tanks.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SandyTank_and_Well_Points/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SandyTank_and_Well_Points/FeatureServer/1?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
