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

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `FacilityID` | string |
| `NORTHING` | double |
| `EASTING` | double |
| `ELEVATION` | double |
| `PIPE_TYPE` | string |
| `OWNERSHIP` | string |
| `PIPE_SIZE` | double |
| `INVERT1` | double |
| `INVERT2` | double |
| `INVERT3` | double |
| `INVERT4` | double |
| `INVERT_OUT` | double |
| `GPSDATE` | timestamp[ms] |
| `BOX_DEPTH` | double |
| `ACTIVE` | string |
| `Comments` | string |
| `RuleID` | int32 |
| `LADDER_1` | string |
| `SANDTRAP` | string |
| `PROJECT` | string |
| `DATEINSTALLED` | timestamp[ms] |
| `Orifice` | int16 |
| `INVERT5` | int32 |
| `InvertNum` | int32 |
| `Terrain_ELEVATION` | double |
| `INVESTIGATE` | string |
| `COMMENT_SUMMARY` | string |
| `PRIORITY` | string |
| `STATUS` | string |
| `InspDate` | timestamp[ms] |
| `StructCond` | string |
| `FrameLid` | string |
| `FloorBenchCond` | string |
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

**`OWNERSHIP`**

- `City` = City
- `City Facility` = City Facility
- `Other City` = Other City
- `Private` = Private
- `UDOT` = UDOT
- `County` = County

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

**`MaintSched`**

- `Annually` = Annually
- `Quarterly` = Quarterly
- `Monthly` = Monthly
- `Other` = Other
- `5 Years` = 5 Years

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/storm-manholes/storm-manholes.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/1) on 2026-10-06T20:51:07Z.
Sandy City publishes no licence for this data; see the [README](README.md).
