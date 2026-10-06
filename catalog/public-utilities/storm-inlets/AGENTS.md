# AGENTS.md — Storm Drain Inlets

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-inlets/storm-inlets.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

42 columns, 12,312 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `FACILITYID` | string |
| `NORTHING` | double |
| `EASTING` | double |
| `ELEVATION` | double |
| `CURB_INLET` | string |
| `BOX_DEPTH` | double |
| `PIPE_TYPE` | string |
| `INVERT1` | double |
| `INVERT2` | double |
| `INVERT3` | double |
| `INVERT4` | double |
| `INVERT_OUT` | double |
| `PIPE_SIZE` | int16 |
| `GPSDATE` | timestamp[ms] |
| `ACTIVE` | string |
| `Comments` | string |
| `RuleID` | int32 |
| `SCOUTS` | int16 |
| `PROJECT` | string |
| `OWNERSHIP` | string |
| `DATEINSTALLED` | timestamp[ms] |
| `ORIFICE` | int16 |
| `INVERT5` | int32 |
| `InvertNum` | int32 |
| `INVESTIGATE` | string |
| `COMMENT_SUMMARY` | string |
| `PRIORITY` | string |
| `STATUS` | string |
| `InspDate` | timestamp[ms] |
| `StructCond` | string |
| `FrameGrate` | string |
| `FloorBench` | string |
| `MaintRating` | string |
| `MaintSched` | string |
| `InspectionZone` | int16 |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
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

**`MaintSched`**

- `Annually` = Annually
- `Quarterly` = Quarterly
- `Monthly` = Monthly
- `Other` = Other
- `5 Years` = 5 Years

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-inlets/storm-inlets.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/0) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
