# AGENTS.md — Trails

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566**, NAD83/HARN Utah Central, in **US survey feet**. `ST_Length` and `ST_Area` return feet and square feet, not metres. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/parks-and-recreation/trails/trails.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

58 columns, 1,127 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Name` | string |
| `USAGE_` | string |
| `TrailID` | int32 |
| `SystemName` | string |
| `SharedName` | string |
| `SystemType` | string |
| `ParkID` | string |
| `Park_ID` | double |
| `CityMuni` | string |
| `County` | string |
| `State` | string |
| `Status` | string |
| `YearOpen` | int32 |
| `Trails_JAKE_Temp_Length` | double |
| `L_Units` | string |
| `L_Source` | string |
| `TrlSurface` | string |
| `Width` | int32 |
| `W_Units` | string |
| `Rating` | string |
| `DesignUse` | string |
| `UseComment` | string |
| `Accessible` | string |
| `Motorized` | string |
| `Hike` | string |
| `RoadBike` | string |
| `MtnBike` | string |
| `Equestrian` | string |
| `DogSled` | string |
| `Snowmobile` | string |
| `Snowshoe` | string |
| `XCntrySki` | string |
| `WCraft_Mtr` | string |
| `WCraft_Non` | string |
| `Portage` | string |
| `ATV` | string |
| `FourWD` | string |
| `Motorcycle` | string |
| `ParkTrail` | string |
| `OnStreetBike` | string |
| `AgencyName` | string |
| `AgencyType` | string |
| `AcqSource` | string |
| `AcqMethod` | string |
| `AcqComment` | string |
| `LWCFProt` | string |
| `OtherProt` | string |
| `ResPrtCmnt` | string |
| `EditDate` | timestamp[ms] |
| `AssetID` | string |
| `Address` | string |
| `Location` | string |
| `Shape_Length_1` | double |
| `Shape` | binary |
| `Shape.STLength()` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/parks-and-recreation/trails/trails.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Trails/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Trails/MapServer/0) on 2026-10-06T19:01:44Z.
Sandy City publishes no licence for this data; see the [README](README.md).
