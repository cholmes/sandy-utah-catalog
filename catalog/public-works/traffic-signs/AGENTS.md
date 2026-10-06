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

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `AssetID` | string |
| `Address` | string |
| `Location` | string |
| `STREET_ON` | string |
| `STREET_AT` | string |
| `District` | string |
| `PMA_ID` | int16 |
| `REMARKS` | string |
| `RETIRED` | timestamp[ms] |
| `Type` | string |
| `MUTCD` | string |
| `MUTCD_Desc` | string |
| `ARROW` | string |
| `SPEED_LIMIT` | string |
| `FACE_POSIT` | string |
| `SIZE_` | string |
| `MATERIAL` | string |
| `CONDITION` | string |
| `LastInspection` | timestamp[ms] |
| `LastInspFY` | string |
| `InspectionNeeded` | string |
| `SignGraphic` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Type`**

- `Regulatory` = Regulatory
- `Guidance` = Guidance
- `Warning` = Warning

**`MUTCD`**

- `D11-1` = D11-1
- `D13` = D13
- `D19` = D19
- `D3` = D3
- `D9-2` = D9-2
- `DFBS` = DFBS
- `HazardMarker` = HazardMarker
- `I-7` = I-7
- `M1-4` = M1-4
- `M3-1` = M3-1
- `M5-1L` = M5-1L
- `M5-1R` = M5-1R
- `M6-1L` = M6-1L
- `M6-1R` = M6-1R
- `M6-3Grn` = M6-3Grn
- `M6-3Wt` = M6-3Wt

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

**`ARROW`**

- `Left` = Left
- `Right` = Right
- `Double` = Double
- `None` = None

**`SPEED_LIMIT`**

- `5` = 5
- `10` = 10
- `15` = 15
- `20` = 20
- `25` = 25
- `30` = 30
- `35` = 35
- `40` = 40
- `45` = 45
- `50` = 50
- `55` = 55

**`FACE_POSIT`**

- `North` = North
- `North/South` = North/South
- `South` = South
- `East` = East
- `East/West` = East/West
- `West` = West

**`MATERIAL`**

- `High Intensity` = High Intensity
- `Engineering Grade` = Engineering Grade

**`CONDITION`**

- `Excellent` = Excellent
- `Good` = Good
- `Good - Tree Trim` = Good - Tree Trim
- `Good - Rivet` = Good - Rivet
- `Poor` = Poor
- `Poor - Burnt` = Poor - Burnt
- `Poor - Bent` = Poor - Bent

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sign_Locatons/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sign_Locatons/FeatureServer/0) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
