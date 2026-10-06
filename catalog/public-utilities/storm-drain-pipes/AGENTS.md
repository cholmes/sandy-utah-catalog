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

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `FacilityID` | string |
| `PIPE_TYPE` | string |
| `IRRIGATION` | int16 |
| `PIPE_SIZE` | double |
| `INVERT_IN` | double |
| `INVERT_OUT` | double |
| `DIP_IN` | double |
| `DIP_OUT` | double |
| `ACTIVE` | string |
| `RuleID` | int32 |
| `Comments` | string |
| `link` | string |
| `PROJECT` | string |
| `OWNERSHIP` | string |
| `DATEINSTALLED` | timestamp[ms] |
| `InvertNum` | int32 |
| `PRIORITY` | string |
| `STATUS` | string |
| `INVESTIGATE` | string |
| `CONDITION` | int32 |
| `CRITICALITY` | int32 |
| `Cond_Age` | int16 |
| `Cond_Inspection` | int16 |
| `Cond_Material` | int16 |
| `Crit_Size` | int16 |
| `Crit_Loc` | int16 |
| `Crit_Irr` | int16 |
| `Total_Score` | int16 |
| `InspDate` | timestamp[ms] |
| `PipeCond` | string |
| `MaintRating` | string |
| `MaintSched` | string |
| `InspectionZone` | int16 |
| `Shape__Length` | double |
| `PIPE_SHAPE` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `IrrigationLine` | string |
| `CUES_SCORE` | double |
| `CUES_ADJ_SCORE` | double |
| `VideoDate` | timestamp[ms] |
| `AssetStatus` | string |
| `VerifiedDate` | timestamp[ms] |
| `VerifiedBy` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

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

**`OWNERSHIP`**

- `City` = City
- `City Facility` = City Facility
- `Other City` = Other City
- `Private` = Private
- `UDOT` = UDOT
- `County` = County

**`STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

**`CONDITION`**

- `0` = 0
- `1` = 1
- `2` = 2
- `3` = 3
- `4` = 4
- `5` = 5

**`CRITICALITY`**

- `0` = 0
- `1` = 1
- `2` = 2
- `3` = 3
- `4` = 4
- `5` = 5

**`PipeCond` — Pipe Condition**

- `0` = 0 - New or Perfect Condition
- `1` = 1 - Excellent Condition
- `2` = 2 - Good Condition (Minor Defects Only)
- `3` = 3 - Fair Condition (Moderate Deterioration)
- `4` = 4 - Poor Condition (Significant Deterioration)
- `5` = 5 - Failing or Failed

**`MaintSched`**

- `Annually` = Annually
- `Quarterly` = Quarterly
- `Monthly` = Monthly
- `Other` = Other
- `5 Years` = 5 Years

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

**`AssetStatus`**

- `Acceptable` = Acceptable
- `CIP Assigned` = CIP Assigned
- `Future (0-1 Years)` = Future (0-1 Years)
- `Future (1-5 Years)` = Future (1-5 Years)
- `Future (5-10 Years)` = Future (5-10 Years)
- `Future (10-20 Years)` = Future (10-20 Years)
- `Future (20+ Years)` = Future (20+ Years)

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/6](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/6) on 2026-10-06T20:51:07Z.
Sandy City publishes no licence for this data; see the [README](README.md).
