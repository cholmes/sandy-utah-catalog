# AGENTS.md — Water Distribution Mains

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-distribution-mains/water-distribution-mains.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

17 columns, 15,249 rows.

15 of 17 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`DIAMETER`** — *int16*  
Nominal diameter, in inches. Measured in the published file: Populated on 100% of 15,249 rows, 13 distinct values, ranging 2 to 36.

**`LINE_TYPE`** — *int16*  
Coded value. The source layer's domain allows: `HDPE`, `DIP`, `CIP`, `TRANSITE`, `BLUE BRUTE`, `GALVANIZED`, `STEEL`, `PVC`, `PVC C90 DR14`, `POLY`, and 1 more. Codes: `12` = HDPE, `1` = DIP, `2` = CIP, `4` = TRANSITE, `5` = BLUE BRUTE, `6` = GALVANIZED, `8` = STEEL, `10` = PVC, `11` = PVC C90 DR14, `13` = POLY, `14` = Copper.

**`YEAR_`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 93% of 15,249 rows, 71 distinct values, ranging 1950 to 20183.

**`FACILITYID`** — *string*  
Identifier of the asset in the city's maintenance management system. Stable within that system, and the key field crews use. Measured in the published file: Populated on 100% of 15,249 rows, 15,247 distinct values.

**`ENABLED`** — *int16*  
Coded value. The source layer's domain allows: `False`, `True`. Codes: `0` = False, `1` = True.

**`WATER_ENTITY`** — *string*  
Coded value. The source layer's domain allows: `Jordan Valley Water`, `Salt Lake City Water`, `Midvale Water`, `Sandy Water`, `Private Owner`, `White City Water`. Codes: `JVW` = Jordan Valley Water, `SLCW` = Salt Lake City Water, `MIDW` = Midvale Water, `Sandy` = Sandy Water, `Private` = Private Owner, `White City Water` = White City Water.

**`CONST_STATUS`** — *string*  
Construction status of the asset. Measured in the published file: Populated on 100% of 15,249 rows, 1 distinct values.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`TracerWire`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 15,249 rows, 4 distinct values.

**`AssetStatus`** — *string*  
Where the asset sits in the capital planning cycle. Measured in the published file: Populated on 1% of 15,249 rows, 1 distinct values.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`DIAMETER`**

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

**`LINE_TYPE`**

- `12` = HDPE
- `1` = DIP
- `2` = CIP
- `4` = TRANSITE
- `5` = BLUE BRUTE
- `6` = GALVANIZED
- `8` = STEEL
- `10` = PVC
- `11` = PVC C90 DR14
- `13` = POLY
- `14` = Copper

**`ENABLED` — Enabled**

- `0` = False
- `1` = True

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-distribution-mains/water-distribution-mains.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "WATER_ENTITY", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-distribution-mains/water-distribution-mains.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Sandy` — 14,855
- `Private` — 392
- `JVW` — 2

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/8](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/8?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
