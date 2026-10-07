# AGENTS.md — Storm Drain Manholes

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-manholes/storm-manholes.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

43 columns, 8,402 rows.

41 of 43 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`FacilityID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 8,402 rows, 8,396 distinct values.

**`NORTHING`** — *double*  
Y coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`EASTING`** — *double*  
X coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`ELEVATION`** — *double*  
Elevation of the feature. Measured in the published file: Populated on 60% of 8,402 rows, 4,869 distinct values, ranging -1 to 5361.07.

**`PIPE_TYPE`** — *string*  
Coded value. The source layer's domain allows: `RCP`, `CMP`, `ADS`, `PVC`, `DIP`, `SMP`, `Open Ditch`, `Combo Box`, `Box Culvert`, `CCCP`, and 6 more. Codes: `RCP` = RCP, `CMP` = CMP, `ADS` = ADS, `PVC` = PVC, `DIP` = DIP, `SMP` = SMP, `OD` = Open Ditch, `CB` = Combo Box, `BC` = Box Culvert, `CCCP` = CCCP, `HDP` = HDPE, `SUM` = Sump.

**`OWNERSHIP`** — *string*  
Who owns the asset. Sandy's utility layers include assets owned by other cities, the county, UDOT and private parties. Measured in the published file: Populated on 100% of 8,402 rows, 6 distinct values.

**`PIPE_SIZE`** — *double*  
Nominal pipe diameter, in inches. Measured in the published file: Populated on 50% of 8,402 rows, 43 distinct values, ranging 0 to 92.

**`INVERT1`** — *double*  
Elevation of one of the pipe inverts at this structure. A structure with several connecting pipes carries one numbered column per invert. The invert is the inside bottom of the pipe. Measured in the published file: Populated on 44% of 8,402 rows, 933 distinct values, ranging 0 to 44359.5.

**`INVERT2`** — *double*  
Elevation of one of the pipe inverts at this structure. A structure with several connecting pipes carries one numbered column per invert. The invert is the inside bottom of the pipe. Measured in the published file: Populated on 31% of 8,402 rows, 516 distinct values, ranging 0 to 5233.48.

**`INVERT3`** — *double*  
Elevation of one of the pipe inverts at this structure. A structure with several connecting pipes carries one numbered column per invert. The invert is the inside bottom of the pipe. Measured in the published file: Populated on 21% of 8,402 rows, 198 distinct values, ranging 0 to 5231.51.

**`INVERT4`** — *double*  
Elevation of one of the pipe inverts at this structure. A structure with several connecting pipes carries one numbered column per invert. The invert is the inside bottom of the pipe. Measured in the published file: Populated on 31% of 8,402 rows, 31 distinct values, ranging 0 to 4699.

**`INVERT_OUT`** — *double*  
Elevation of the pipe invert where flow leaves the structure. Measured in the published file: Populated on 48% of 8,402 rows, 1,019 distinct values, ranging 0 to 441197.

**`GPSDATE`** — *timestamp[ms]*  
Date the location was captured by GPS in the field. Measured in the published file: Populated on 26% of 8,402 rows, 630 distinct values.

**`BOX_DEPTH`** — *double*  
Depth of the structure box below the rim. Measured in the published file: Populated on 61% of 8,402 rows, 427 distinct values, ranging 0 to 4968.

**`ACTIVE`** — *string*  
Whether the asset is in service. Measured in the published file: Populated on 83% of 8,402 rows, 4 distinct values.

**`Comments`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`RuleID`** — *int32*  
Esri symbology rule identifier. It selects a renderer class in the city's own map documents and carries no meaning about the feature itself.

**`LADDER_1`** — *string*  
Coded value. The source layer's domain allows: `Yes`, `No`. Codes: `Y` = Yes, `N` = No.

**`SANDTRAP`** — *string*  
Coded value. The source layer's domain allows: `Yes`, `No`. Codes: `Y` = Yes, `N` = No.

**`PROJECT`** — *string*  
Capital project the asset was built or replaced under. Measured in the published file: Populated on 19% of 8,402 rows, 229 distinct values.

**`DATEINSTALLED`** — *timestamp[ms]*  
Date the asset was installed. Measured in the published file: Populated on 14% of 8,402 rows, 119 distinct values.

**`Orifice`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 4% of 8,402 rows, 2 distinct values, ranging 0 to 2.

**`INVERT5`** — *int32*  
Elevation of one of the pipe inverts at this structure. A structure with several connecting pipes carries one numbered column per invert. The invert is the inside bottom of the pipe. Measured in the published file: Populated on 4% of 8,402 rows, 2 distinct values, ranging 0 to 4700.

**`InvertNum`** — *int32*  
Identifier of the invert within the structure, where a structure has more than one connecting pipe. Measured in the published file: Populated on 4% of 8,402 rows, 1 distinct values.

**`Terrain_ELEVATION`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 4% of 8,402 rows, 1 distinct values.

**`INVESTIGATE`** — *string*  
Flag set by staff where the record needs field verification. Measured in the published file: Populated on 55% of 8,402 rows, 8 distinct values.

**`COMMENT_SUMMARY`** — *string*  
Summary of inspection or maintenance comments. Measured in the published file: Populated on 10% of 8,402 rows, 11 distinct values.

**`PRIORITY`** — *string*  
Maintenance or response priority assigned by the city. Measured in the published file: Populated on 0% of 8,402 rows, 1 distinct values.

**`STATUS`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 100% of 8,402 rows, 4 distinct values.

**`InspDate`** — *timestamp[ms]*  
Date of the most recent inspection. Measured in the published file: Populated on 3% of 8,402 rows, 230 distinct values.

**`StructCond`** — *string*  
Structural Condition. Measured in the published file: Populated on 3% of 8,402 rows, 2 distinct values.

**`FrameLid`** — *string*  
Frame and Lid. Measured in the published file: Populated on 3% of 8,402 rows, 3 distinct values.

**`FloorBenchCond`** — *string*  
Floor/Bench Condition. Measured in the published file: Populated on 3% of 8,402 rows, 2 distinct values.

**`MaintRating`** — *string*  
Maintenance condition rating assigned at the last inspection. The source layer declares no code list, so the scale is not documented. Measured in the published file: Populated on 3% of 8,402 rows, 4 distinct values.

**`MaintSched`** — *string*  
How often the asset is scheduled for maintenance. Measured in the published file: Populated on 58% of 8,402 rows, 2 distinct values.

**`InspectionZone`** — *int16*  
Inspection zone the asset is grouped into for scheduling. Measured in the published file: Populated on 57% of 8,402 rows, 6 distinct values, ranging 0 to 5.

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

**`PIPE_TYPE`**

- `RCP` = RCP
- `CMP` = CMP
- `ADS` = ADS
- `PVC` = PVC
- `DIP` = DIP
- `SMP` = SMP
- `OD` = Open Ditch
- `CB` = Combo Box
- `BC` = Box Culvert
- `CCCP` = CCCP
- `HDP` = HDPE
- `SUM` = Sump
- `CCIP` = CCIP
- `CIPP` = CIPP
- `SC` = Steel Casing
- `RCP ELL` = RCP Elliptical

**`RuleID`**

- `1` = <Null>
- `2` = Overlayed NO
- `3` = Overlayed Yes

**`LADDER_1`**

- `Y` = Yes
- `N` = No

**`SANDTRAP`**

- `Y` = Yes
- `N` = No

**`STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-manholes/storm-manholes.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/1?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
