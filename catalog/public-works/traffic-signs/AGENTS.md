# AGENTS.md — Traffic Signs

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/traffic-signs/traffic-signs.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

29 columns, 8,403 rows.

19 of 29 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`AssetID`** — *string*  
Identifier of the asset in the city's maintenance management system. Measured in the published file: Populated on 100% of 8,403 rows, 8,386 distinct values.

**`Address`** — *string*  
Street address of the feature. Measured in the published file: Populated on 100% of 8,403 rows, 7,770 distinct values.

**`Location`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 100% of 8,403 rows, 7,769 distinct values.

**`STREET_ON`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 8,403 rows, 1,542 distinct values.

**`STREET_AT`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 8,403 rows, 3,033 distinct values.

**`District`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 96% of 8,403 rows, 21 distinct values.

**`PMA_ID`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 8,403 rows, 1,685 distinct values, ranging 0 to 7899.

**`REMARKS`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 87% of 8,403 rows, 2,296 distinct values.

**`RETIRED`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Empty in all 8,403 rows of the published file.

**`Type`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 100% of 8,403 rows, 3 distinct values.

**`MUTCD`** — *string*  
One of. The source layer's domain allows: `D11-1`, `D13`, `D19`, `D3`, `D9-2`, `DFBS`, `HazardMarker`, `I-7`, `M1-4`, `M3-1`, and 131 more.

**`MUTCD_Desc`** — *string*  
Coded value. The source layer's domain allows: `Bike Route`, `Entrance Only`, `Exit Only`, `Street Name`, `Hospital (symbol)`, `DFBS`, `Hazard Marker`, `Train Station`, `US Numbered Route (2 digit)`, `North`, and 133 more. Codes: `D11-1` = Bike Route, `D13` = Entrance Only, `D19` = Exit Only, `D3` = Street Name, `D9-2` = Hospital (symbol), `DFBS` = DFBS, `HazardMarker` = Hazard Marker, `I-7` = Train Station, `M1-4` = US Numbered Route (2 digit), `M3-1` = North, `M5-1L` = Advance Turn Arrow Auxiliary (90 degree) (left), `M5-1R` = Advance Turn Arrow Auxiliary (90 degree) (right).

**`ARROW`** — *string*  
One of. The source layer's domain allows: `Left`, `Right`, `Double`, `None`.

**`SPEED_LIMIT`** — *string*  
One of. The source layer's domain allows: `5`, `10`, `15`, `20`, `25`, `30`, `35`, `40`, `45`, `50`, and 1 more.

**`FACE_POSIT`** — *string*  
One of. The source layer's domain allows: `North`, `North/South`, `South`, `East`, `East/West`, `West`.

**`SIZE_`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,403 rows, 80 distinct values.

**`MATERIAL`** — *string*  
One of. The source layer's domain allows: `High Intensity`, `Engineering Grade`.

**`CONDITION`** — *string*  
One of. The source layer's domain allows: `Excellent`, `Good`, `Good - Tree Trim`, `Good - Rivet`, `Poor`, `Poor - Burnt`, `Poor - Bent`.

**`LastInspection`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,403 rows, 4,700 distinct values.

**`LastInspFY`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 8,403 rows, 6 distinct values.

**`InspectionNeeded`** — *string*  
Coded value. The source layer's domain allows: `Yes`, `No`. Codes: `Y` = Yes, `N` = No.

**`SignGraphic`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 8,403 rows, 98 distinct values.

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

**`MUTCD_Desc`**

- `D11-1` = Bike Route
- `D13` = Entrance Only
- `D19` = Exit Only
- `D3` = Street Name
- `D9-2` = Hospital (symbol)
- `DFBS` = DFBS
- `HazardMarker` = Hazard Marker
- `I-7` = Train Station
- `M1-4` = US Numbered Route (2 digit)
- `M3-1` = North
- `M5-1L` = Advance Turn Arrow Auxiliary (90 degree) (left)
- `M5-1R` = Advance Turn Arrow Auxiliary (90 degree) (right)
- `M6-1L` = Arrow Auxiliary (left)
- `M6-1R` = Arrow Auxiliary (right)
- `M6-3Grn` = Straight Arrow Auxiliary - GRN
- `M6-3Wt` = Straight Arrow Auxiliary - WT

**`InspectionNeeded`**

- `Y` = Yes
- `N` = No

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/traffic-signs/traffic-signs.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Type", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/traffic-signs/traffic-signs.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Regulatory` — 3,479
- `Guidance` — 2,810
- `Warning` — 2,100

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sign_Locatons/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sign_Locatons/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
