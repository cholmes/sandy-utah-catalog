# AGENTS.md — Storm Drain Pipes

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-drain-pipes/storm-drain-pipes.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

49 columns, 19,492 rows.

33 of 49 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`FacilityID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 19,492 rows, 19,484 distinct values.

**`PIPE_TYPE`** — *string*  
Coded value. The source layer's domain allows: `RCP`, `CMP`, `ADS`, `PVC`, `DIP`, `SMP`, `Open Ditch`, `Combo Box`, `Box Culvert`, `CCCP`, and 6 more. Codes: `RCP` = RCP, `CMP` = CMP, `ADS` = ADS, `PVC` = PVC, `DIP` = DIP, `SMP` = SMP, `OD` = Open Ditch, `CB` = Combo Box, `BC` = Box Culvert, `CCCP` = CCCP, `HDP` = HDPE, `SUM` = Sump.

**`IRRIGATION`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 19,492 rows, 5 distinct values, ranging 0 to 4.

**`PIPE_SIZE`** — *double*  
Nominal pipe diameter, in inches. Measured in the published file: Populated on 92% of 19,492 rows, 57 distinct values, ranging 0 to 144.

**`INVERT_IN`** — *double*  
Elevation of the pipe invert where flow enters the structure. The invert is the inside bottom of the pipe. Measured in the published file: Populated on 44% of 19,492 rows, 7,958 distinct values, ranging 0 to 5778.25.

**`INVERT_OUT`** — *double*  
Elevation of the pipe invert where flow leaves the structure. Measured in the published file: Populated on 36% of 19,492 rows, 5,015 distinct values, ranging 0 to 450728.

**`DIP_IN`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 44% of 19,492 rows, 526 distinct values, ranging -1 to 4472.54.

**`DIP_OUT`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 36% of 19,492 rows, 427 distinct values, ranging -1 to 671.

**`ACTIVE`** — *string*  
Whether the asset is in service. Measured in the published file: Populated on 64% of 19,492 rows, 3 distinct values.

**`RuleID`** — *int32*  
Esri symbology rule identifier. It selects a renderer class in the city's own map documents and carries no meaning about the feature itself.

**`Comments`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`link`** — *string*  
Link to a page about this feature on a city or partner website.

**`PROJECT`** — *string*  
Capital project the asset was built or replaced under. Measured in the published file: Populated on 25% of 19,492 rows, 316 distinct values.

**`OWNERSHIP`** — *string*  
Who owns the asset. Sandy's utility layers include assets owned by other cities, the county, UDOT and private parties. Measured in the published file: Populated on 100% of 19,492 rows, 6 distinct values.

**`DATEINSTALLED`** — *timestamp[ms]*  
Date the asset was installed. Measured in the published file: Populated on 29% of 19,492 rows, 189 distinct values.

**`InvertNum`** — *int32*  
Identifier of the invert within the structure, where a structure has more than one connecting pipe. Measured in the published file: Populated on 5% of 19,492 rows, 2 distinct values, ranging 0 to 1.

**`PRIORITY`** — *string*  
Maintenance or response priority assigned by the city. Measured in the published file: Populated on 0% of 19,492 rows, 1 distinct values.

**`STATUS`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 100% of 19,492 rows, 4 distinct values.

**`INVESTIGATE`** — *string*  
Flag set by staff where the record needs field verification. Measured in the published file: Populated on 66% of 19,492 rows, 10 distinct values.

**`CONDITION`** — *int32*  
One of. The source layer's domain allows: `0`, `1`, `2`, `3`, `4`, `5`.

**`CRITICALITY`** — *int32*  
One of. The source layer's domain allows: `0`, `1`, `2`, `3`, `4`, `5`.

**`Cond_Age`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 5% of 19,492 rows, 1 distinct values.

**`Cond_Inspection`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 5% of 19,492 rows, 1 distinct values.

**`Cond_Material`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 14% of 19,492 rows, 4 distinct values, ranging 0 to 100.

**`Crit_Size`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 9% of 19,492 rows, 11 distinct values, ranging 0 to 105.

**`Crit_Loc`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 9% of 19,492 rows, 11 distinct values, ranging 0 to 105.

**`Crit_Irr`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 9% of 19,492 rows, 6 distinct values, ranging -2 to 105.

**`Total_Score`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 8% of 19,492 rows, 18 distinct values, ranging 0 to 209.

**`InspDate`** — *timestamp[ms]*  
Date of the most recent inspection. Measured in the published file: Populated on 9% of 19,492 rows, 936 distinct values.

**`PipeCond`** — *string*  
Pipe Condition. Coded value. The source layer's domain allows: `0 - New or Perfect Condition`, `1 - Excellent Condition`, `2 - Good Condition (Minor Defects Only)`, `3 - Fair Condition (Moderate Deterioration)`, `4 - Poor Condition (Significant Deterioration)`, `5 - Failing or Failed`. Codes: `0` = 0 - New or Perfect Condition, `1` = 1 - Excellent Condition, `2` = 2 - Good Condition (Minor Defects Only), `3` = 3 - Fair Condition (Moderate Deterioration), `4` = 4 - Poor Condition (Significant Deterioration), `5` = 5 - Failing or Failed.

**`MaintRating`** — *string*  
Maintenance condition rating assigned at the last inspection. The source layer declares no code list, so the scale is not documented. Measured in the published file: Populated on 4% of 19,492 rows, 5 distinct values.

**`MaintSched`** — *string*  
How often the asset is scheduled for maintenance. Measured in the published file: Populated on 68% of 19,492 rows, 2 distinct values.

**`InspectionZone`** — *int16*  
Inspection zone the asset is grouped into for scheduling. Measured in the published file: Populated on 67% of 19,492 rows, 6 distinct values, ranging 0 to 5.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`PIPE_SHAPE`** — *string*  
Coded value. The source layer's domain allows: `Arched`, `Barrel`, `Circular`, `Egg-shaped`, `Horseshoe`, `Other`, `Oval`, `Rectangle`, `Square`, `Trapezoidal`, and 2 more. Codes: `Arched` = Arched, `Barrel` = Barrel, `Circular` = Circular, `Egg` = Egg-shaped, `Horseshoe` = Horseshoe, `Other` = Other, `Oval` = Oval, `Rectangle` = Rectangle, `Square` = Square, `Trapezoidal` = Trapezoidal, `U-shaped with flat top` = U-shaped with flat top, `Unknown` = Unknown.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`IrrigationLine`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 1% of 19,492 rows, 4 distinct values.

**`CUES_SCORE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 7% of 19,492 rows, 55 distinct values, ranging 0 to 100.

**`CUES_ADJ_SCORE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 7% of 19,492 rows, 20 distinct values, ranging 0 to 5.

**`VideoDate`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 10% of 19,492 rows, 1,500 distinct values.

**`AssetStatus`** — *string*  
Where the asset sits in the capital planning cycle. Measured in the published file: Populated on 46% of 19,492 rows, 7 distinct values.

**`VerifiedDate`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 4% of 19,492 rows, 850 distinct values.

**`VerifiedBy`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 4% of 19,492 rows, 12 distinct values.

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

- `1` = Rule_1

**`STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

**`PipeCond` — Pipe Condition**

- `0` = 0 - New or Perfect Condition
- `1` = 1 - Excellent Condition
- `2` = 2 - Good Condition (Minor Defects Only)
- `3` = 3 - Fair Condition (Moderate Deterioration)
- `4` = 4 - Poor Condition (Significant Deterioration)
- `5` = 5 - Failing or Failed

**`PIPE_SHAPE` — Pipe Shape**

- `Arched` = Arched
- `Barrel` = Barrel
- `Circular` = Circular
- `Egg` = Egg-shaped
- `Horseshoe` = Horseshoe
- `Other` = Other
- `Oval` = Oval
- `Rectangle` = Rectangle
- `Square` = Square
- `Trapezoidal` = Trapezoidal
- `U-shaped with flat top` = U-shaped with flat top
- `Unknown` = Unknown

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-drain-pipes/storm-drain-pipes.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "OWNERSHIP", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-drain-pipes/storm-drain-pipes.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `City` — 8,573
- `Private` — 5,271
- `Other City` — 3,971
- `UDOT` — 1,133
- `County` — 301
- `City Facility` — 241

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/6](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/6?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
