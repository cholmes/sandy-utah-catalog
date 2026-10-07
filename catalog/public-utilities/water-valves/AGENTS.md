# AGENTS.md — Water Valves

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-valves/water-valves.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

38 columns, 8,117 rows.

27 of 38 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`WVALVES_ID`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 94% of 8,117 rows, 7,648 distinct values.

**`FACILITYID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 8,117 rows, 8,115 distinct values.

**`NORTHING`** — *double*  
Y coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`EASTING`** — *double*  
X coordinate copied into an attribute. The geometry column is authoritative; this copy is not always consistent with it.

**`ELEVATION`** — *double*  
Elevation of the feature. Measured in the published file: Populated on 95% of 8,117 rows, 7,617 distinct values, ranging 0 to 5447.02.

**`ENABLED`** — *int16*  
Coded value. The source layer's domain allows: `False`, `True`. Codes: `0` = False, `1` = True.

**`DATEINSPECTED`** — *timestamp[ms]*  
Inspection Date. Measured in the published file: Populated on 77% of 8,117 rows, 4,454 distinct values.

**`INSPECTED_BY`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 77% of 8,117 rows, 20 distinct values.

**`COMMENTS`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`MAP_NO`** — *string*  
Sheet number of the paper map the feature was digitised from. Measured in the published file: Populated on 84% of 8,117 rows, 174 distinct values.

**`ADDRESS`** — *string*  
Street address of the feature. Measured in the published file: Populated on 94% of 8,117 rows, 5,250 distinct values.

**`LAND_TIES`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 77% of 8,117 rows, 5,861 distinct values.

**`VALVE_SIZE`** — *int16*  
Coded value. The source layer's domain allows: `4"`, `6"`, `8"`, `10"`, `12"`, `24"`, `30"`, `36"`, `15"`, `18"`, and 15 more. Codes: `4` = 4", `6` = 6", `8` = 8", `10` = 10", `12` = 12", `24` = 24", `30` = 30", `36` = 36", `15` = 15", `18` = 18", `48` = 48", `60` = 60".

**`VALVE_DEPTH`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 63% of 8,117 rows, 89 distinct values, ranging 0 to 3035.

**`VALVE_TYPE`** — *string*  
Vavle Type. Coded value. The source layer's domain allows: `Gate Valve`, `Butterfly Valve`, `Other Valve`, `Unknown Valve`. Codes: `GATE` = Gate Valve, `BUTTERFLY` = Butterfly Valve, `OTHER` = Other Valve, `UNKNOWN` = Unknown Valve.

**`VALVE_FUNCTION`** — *string*  
Coded value. The source layer's domain allows: `Main Valve`, `Aux Hyd Valve`, `Meter Valve`, `Fire Line Valve`, `Zone Break Valve`, `Seperation Valve`. Codes: `Main` = Main Valve, `Aux` = Aux Hyd Valve, `MeterV` = Meter Valve, `Fireline` = Fire Line Valve, `ZB` = Zone Break Valve, `SepV` = Seperation Valve.

**`VALVE_MANU`** — *string*  
Valve Manufacturer. One of. The source layer's domain allows: `MUELLER`, `AFC`, `WATTEROUS`, `CLOW`, `PRATT`, `OTHER`, `KENNEDY`, `VAL-MATIC`, `EJ`, `AVTEK`, and 1 more.

**`TURNS_TO_CLOSE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 63% of 8,117 rows, 55 distinct values, ranging 0 to 67.

**`DIRECTION`** — *string*  
Turn Direction. Coded value. The source layer's domain allows: `Right Hand`, `Left Hand`. Codes: `R` = Right Hand, `L` = Left Hand.

**`INSTALL_DATE`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 36% of 8,117 rows, 1,304 distinct values.

**`COLLECTED_BY`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 82% of 8,117 rows, 151 distinct values.

**`DATE_COLLECTED`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 80% of 8,117 rows, 1,738 distinct values.

**`MANFAC_DATE`** — *int32*  
Manufacture Date. Measured in the published file: Populated on 89% of 8,117 rows, 45 distinct values, ranging 0 to 20202.

**`SHUT_DOWN`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 7% of 8,117 rows, 291 distinct values.

**`OTHER_INFO`** — *string*  
Free-text note carried from the source record. Measured in the published file: Populated on 45% of 8,117 rows, 1,023 distinct values.

**`PWTYPE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 69% of 8,117 rows, 3 distinct values.

**`LOCATION`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 91% of 8,117 rows, 5,978 distinct values.

**`OPERATION_MODE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 92% of 8,117 rows, 7 distinct values.

**`WATER_ENTITY`** — *string*  
Coded value. The source layer's domain allows: `Jordan Valley Water`, `Salt Lake City Water`, `Midvale Water`, `Sandy Water`, `Private Owner`, `White City Water`. Codes: `JVW` = Jordan Valley Water, `SLCW` = Salt Lake City Water, `MIDW` = Midvale Water, `Sandy` = Sandy Water, `Private` = Private Owner, `White City Water` = White City Water.

**`CONST_STATUS`** — *string*  
Construction status of the asset. Measured in the published file: Populated on 100% of 8,117 rows, 1 distinct values.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`GPS_DATE`** — *timestamp[ms]*  
Date the location was captured by GPS in the field. Measured in the published file: Populated on 19% of 8,117 rows, 1,550 distinct values.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`ENABLED` — Enabled**

- `0` = False
- `1` = True

**`VALVE_SIZE` — Valve Size**

- `4` = 4"
- `6` = 6"
- `8` = 8"
- `10` = 10"
- `12` = 12"
- `24` = 24"
- `30` = 30"
- `36` = 36"
- `15` = 15"
- `18` = 18"
- `48` = 48"
- `60` = 60"
- `21` = 21"
- `42` = 42"
- `54` = 54"
- `66` = 66"

**`VALVE_TYPE` — Vavle Type**

- `GATE` = Gate Valve
- `BUTTERFLY` = Butterfly Valve
- `OTHER` = Other Valve
- `UNKNOWN` = Unknown Valve

**`VALVE_FUNCTION` — Valve Function**

- `Main` = Main Valve
- `Aux` = Aux Hyd Valve
- `MeterV` = Meter Valve
- `Fireline` = Fire Line Valve
- `ZB` = Zone Break Valve
- `SepV` = Seperation Valve

**`DIRECTION` — Turn Direction**

- `R` = Right Hand
- `L` = Left Hand

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

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-valves/water-valves.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
