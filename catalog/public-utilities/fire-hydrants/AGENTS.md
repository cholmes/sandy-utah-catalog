# AGENTS.md — Fire Hydrants

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/fire-hydrants/fire-hydrants.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

45 columns, 5,292 rows.

27 of 45 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`FACILITYID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 5,292 rows, 5,291 distinct values.

**`HYD_ID`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 5,292 rows, 5,135 distinct values, ranging 158 to 9856.

**`COMMENTS`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`GPS_DATE`** — *timestamp[ms]*  
Date the location was captured by GPS in the field. Measured in the published file: Populated on 75% of 5,292 rows, 542 distinct values.

**`NORTHING`** — *double*  
Y coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`EASTING`** — *double*  
X coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`PROVIDER`** — *string*  
Coded value. The source layer's domain allows: `Sandy`, `Other`, `Midvale`. Codes: `SANDY` = Sandy, `OTHER` = Other, `Midvale` = Midvale.

**`MAP_NO`** — *string*  
Sheet number of the paper map the feature was digitised from. Measured in the published file: Populated on 92% of 5,292 rows, 161 distinct values.

**`APADDRESS`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 5,292 rows, 4,684 distinct values.

**`LANDTIES`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 66% of 5,292 rows, 1,958 distinct values.

**`HYDSIZE`** — *double*  
Coded value. The source layer's domain allows: `4"`, `5.25"`. Codes: `4` = 4", `5.25` = 5.25".

**`HYD_TYPE`** — *string*  
One of. The source layer's domain allows: `SCISSORS`, `COMPRESSION`.

**`HYD_MANUF`** — *string*  
One of. The source layer's domain allows: `CLOW`, `IOWA`, `WATEROUS`, `PACIFIC STATES`, `KENNEDY`, `OTHER`, `MUELLER`, `EJ`.

**`MANUF_DATE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 82% of 5,292 rows, 74 distinct values.

**`VDEPTH`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 66% of 5,292 rows, 92 distinct values.

**`VLOCAT`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 74% of 5,292 rows, 375 distinct values.

**`VSIZE`** — *double*  
Coded value. The source layer's domain allows: `2"`, `4"`, `8"`, `10"`, `12"`, `14"`, `16"`, `20"`, `24"`, `30"`, and 3 more. Codes: `2` = 2", `4` = 4", `8` = 8", `10` = 10", `12` = 12", `14` = 14", `16` = 16", `20` = 20", `24` = 24", `30` = 30", `33` = 33", `36` = 36".

**`VTYPE`** — *string*  
Coded value. The source layer's domain allows: `GATE VALVE`, `BUTTERFLY VALVE`, `OTHER VALVE`, `UNKOWN VALVE`. Codes: `GATE` = GATE VALVE, `BUTTERFLY` = BUTTERFLY VALVE, `OTHER` = OTHER VALVE, `UNKNOWN` = UNKOWN VALVE.

**`VMAUF`** — *string*  
One of. The source layer's domain allows: `MUELLER`, `AFC`, `WATTEROUS`, `CLOW`, `PRATT`, `OTHER`, `KENNEDY`, `VAL-MATIC`, `EJ`, `AVTEK`, and 1 more.

**`VMAUNFDATE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 80% of 5,292 rows, 37 distinct values, ranging 0 to 20221.

**`INSTDATE`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 20% of 5,292 rows, 740 distinct values.

**`DATECOLT`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 77% of 5,292 rows, 1,091 distinct values.

**`COLLTBY`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 79% of 5,292 rows, 101 distinct values.

**`OTHER_INFO`** — *string*  
Free-text note carried from the source record. Measured in the published file: Populated on 69% of 5,292 rows, 646 distinct values.

**`ACAD_ANGLE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 84% of 5,292 rows, 3,272 distinct values, ranging 0 to 359.943.

**`ENABLED`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 5,292 rows, 2 distinct values, ranging 0 to 1.

**`ANCILLARYROLE`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 5,292 rows, 2 distinct values, ranging 0 to 2.

**`LOCATION`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 96% of 5,292 rows, 4,184 distinct values.

**`INSPDATE`** — *timestamp[ms]*  
Date of the most recent inspection. Measured in the published file: Populated on 97% of 5,292 rows, 5,078 distinct values.

**`RESIDPRESSURE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 3% of 5,292 rows, 56 distinct values, ranging 0 to 170.

**`STATICPRESSURE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 5% of 5,292 rows, 87 distinct values, ranging 47 to 240.

**`TWENTYPSIFLOW`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 3% of 5,292 rows, 145 distinct values, ranging 0 to 30352.

**`THIRTYPSIFLOW`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 3% of 5,292 rows, 147 distinct values, ranging 0 to 28438.

**`WATER_ENTITY`** — *string*  
Coded value. The source layer's domain allows: `Jordan Valley Water`, `Salt Lake City Water`, `Midvale Water`, `Sandy Water`, `Private Owner`, `White City Water`. Codes: `JVW` = Jordan Valley Water, `SLCW` = Salt Lake City Water, `MIDW` = Midvale Water, `Sandy` = Sandy Water, `Private` = Private Owner, `White City Water` = White City Water.

**`FIRE_INSP_DIST`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 94% of 5,292 rows, 15 distinct values.

**`CONST_STATUS`** — *string*  
Construction status of the asset. Measured in the published file: Populated on 100% of 5,292 rows, 1 distinct values.

**`STATUS`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 100% of 5,292 rows, 4 distinct values.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`AssetStatus`** — *string*  
Where the asset sits in the capital planning cycle. Measured in the published file: Populated on 52% of 5,292 rows, 5 distinct values.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`PROVIDER`**

- `SANDY` = Sandy
- `OTHER` = Other
- `Midvale` = Midvale

**`HYDSIZE`**

- `4` = 4"
- `5.25` = 5.25"

**`VSIZE`**

- `2` = 2"
- `4` = 4"
- `8` = 8"
- `10` = 10"
- `12` = 12"
- `14` = 14"
- `16` = 16"
- `20` = 20"
- `24` = 24"
- `30` = 30"
- `33` = 33"
- `36` = 36"
- `6` = 6"

**`VTYPE`**

- `GATE` = GATE VALVE
- `BUTTERFLY` = BUTTERFLY VALVE
- `OTHER` = OTHER VALVE
- `UNKNOWN` = UNKOWN VALVE

**`WATER_ENTITY`**

- `JVW` = Jordan Valley Water
- `SLCW` = Salt Lake City Water
- `MIDW` = Midvale Water
- `Sandy` = Sandy Water
- `Private` = Private Owner
- `White City Water` = White City Water

**`CONST_STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

**`STATUS`**

- `In Service` = In Service
- `Out of Service` = Out of Service
- `Needs Repair` = Needs Repair
- `Needs Inspection` = Needs Inspection
- `INS / Obstructed` = INS/Obstructed
- `Outside Service Area` = Outside Service Area
- `Low PSI - Never Insp` = Low PSI - Never Insp

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/fire-hydrants/fire-hydrants.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/1?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
