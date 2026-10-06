# AGENTS.md — Golf Courses

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/golf-courses/golf-courses.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

72 columns, 4 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `NAME` | string |
| `Address` | string |
| `Municipality` | string |
| `Phone` | string |
| `Type` | string |
| `Acres` | double |
| `Reservable` | string |
| `Indoor_Pavilion` | string |
| `Outdoor_Pavilion` | string |
| `Restrooms` | string |
| `Parking_Stalls` | int16 |
| `BBQ_Pit` | string |
| `Playground` | string |
| `Jogging_Path_Miles` | double |
| `Baseball_Diamonds` | int16 |
| `Baseball_Lighting` | string |
| `Basketball_Stands` | int16 |
| `Basketball_Lighting` | string |
| `Soccer_Fields` | int16 |
| `Soccer_Lighting` | string |
| `Softball_Diamonds` | int16 |
| `Softball_Lighting` | string |
| `Tennis_Courts` | int16 |
| `Tennis_Lighting` | string |
| `Volleyball_Courts` | int16 |
| `Volleyball_Lighting` | string |
| `Electrical_Outlets` | string |
| `Water_Outlets` | string |
| `Notes` | string |
| `URL` | string |
| `ParkID` | string |
| `Park_ID` | double |
| `County` | string |
| `State` | string |
| `StreetNum` | string |
| `StreetName` | string |
| `StreetType` | string |
| `Zip` | string |
| `Reference` | string |
| `RefComment` | string |
| `Park_Acres` | double |
| `AcreSource` | string |
| `YearOpen` | int32 |
| `ParkStatus` | string |
| `StatusCmnt` | string |
| `ParkType` | string |
| `ServicArea` | string |
| `MgtPriorty` | string |
| `Landowner` | string |
| `OwnerType` | string |
| `AgencyName` | string |
| `AgencyType` | string |
| `AcqSource` | string |
| `AcqMethod` | string |
| `AcqComment` | string |
| `DevSource` | string |
| `DevComment` | string |
| `Restricts` | string |
| `LWCFProt` | string |
| `OtherProt` | string |
| `ResPrtCmnt` | string |
| `EditDate` | timestamp[ms] |
| `Unit` | string |
| `Unit_ID` | string |
| `Unit_Acres` | double |
| `AddedTrails` | string |
| `Shape` | binary |
| `Shape.area` | double |
| `Shape.len` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Reference`**

- `Entrance` = Entrance
- `Center_Point` = Center Point
- `Facility` = Facility
- `Other` = Other

**`AcreSource`**

- `Parcel` = Parcel
- `Deed` = Deed
- `Survey` = Survey
- `GIS Value` = GIS Value
- `Other` = Other

**`ParkStatus`**

- `Open` = Open
- `Open_Fee` = Open_Fee
- `Open_Restricted` = Open_Restricted
- `Closed` = Closed
- `Decommissioned` = Decommissioned
- `Unknown` = Unknown
- `Planned` = Planned
- `Proposed` = Proposed

**`ServicArea`**

- `0-0.5 miles` = 0-0.5 miles
- `0-5 miles` = 0-5 miles
- `0-25 miles` = 0-25 miles
- `0-100 miles` = 0-100 miles
- `0-100 or more miles` = 0-100 or more miles

**`MgtPriorty`**

- `Active Park` = Active Park
- `Passive Park` = Passive Park
- `Mixed-use Park` = Mixed-use Park
- `Natural Area` = Natural Area
- `Historical/Cultural` = Historical/Cultural
- `Special Use Area` = Special Use Area
- `Corridor` = Corridor

**`OwnerType`**

- `Federal` = Federal
- `State` = State
- `County` = County
- `Municipal` = Municipal
- `Special District` = Special District
- `Private - NP` = Private - NP
- `Private` = Private
- `Unknown` = Unknown
- `School` = School

**`AgencyType`**

- `Federal` = Federal
- `State` = State
- `County` = County
- `Municipal` = Municipal
- `Special District` = Special District
- `Private - NP` = Private - NP
- `Private` = Private
- `Unknown` = Unknown
- `School` = School

**`AcqSource`**

- `Donation` = Donation
- `Transfer` = Transfer
- `Bond` = Bond
- `Capital Budget` = Capital Budget
- `Special tax or assessment` = Special Tax or assessment
- `Exactions` = Exactions
- `Federal Grant` = Federal Grant
- `State Grant` = State Grant
- `Other Grant` = Other Grant
- `Other` = Other
- `Multiple` = Multiple
- `Partnership` = Partnership

**`AcqMethod`**

- `Fee simple` = Fee simple
- `Easement` = Easement
- `Lease` = Lease
- `Eminent Domain` = Eminent Domain
- `Land Exchange` = Land Exchange
- `Transfer` = Transfer
- `Donation` = Donation
- `Other` = Other

**`DevSource`**

- `None` = None
- `Donation` = Donation
- `Bond` = Bond
- `Capital Budget` = Capital Budget
- `Special tax or assessment` = Special tax or assessment
- `Exactions` = Exactions
- `Federal Grant` = Federal Grant
- `State Grant` = State Grant
- `Other Grant` = Other Grant
- `Other` = Other
- `Multiple` = Multiple
- `Partnership` = Partnership

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/golf-courses/golf-courses.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Golf_Courses/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Golf_Courses/MapServer/1) on 2026-10-06T20:51:07Z.
Sandy City publishes no licence for this data; see the [README](README.md).
