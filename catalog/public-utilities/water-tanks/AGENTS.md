# AGENTS.md — Water Tanks

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-tanks/water-tanks.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

36 columns, 9 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `PubUtils.PU.SandyTanks_Points.AREA` | double |
| `PERIMETER` | double |
| `SANDY_TANKS_` | int32 |
| `SANDY_TANKS_ID` | int32 |
| `TANK_NAME` | string |
| `LOCATION` | string |
| `CAPACITY` | string |
| `FLOOR_EL` | double |
| `GROUND_EL` | double |
| `OVER_EL` | double |
| `OVER_DEPTH` | double |
| `DIMENSIONS` | string |
| `ZONE_` | double |
| `CONST_TYPE` | string |
| `YEAR_CONST` | double |
| `MGCAPACITY` | double |
| `ENGINEER` | string |
| `CONTRACTOR` | string |
| `MAINT_DATE` | timestamp[ms] |
| `MAINT_TYPE` | string |
| `X_COORD` | double |
| `Y_COORD` | double |
| `FACILITYID` | string |
| `POLYGONID` | int32 |
| `SCALE` | double |
| `ANGLE` | double |
| `Enabled` | int16 |
| `AncillaryRole` | int16 |
| `CONST_STATUS` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Enabled`**

- `0` = False
- `1` = True

**`AncillaryRole`**

- `0` = None
- `1` = Source
- `2` = Sink

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-tanks/water-tanks.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SandyTank_and_Well_Points/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SandyTank_and_Well_Points/FeatureServer/1) on 2026-10-06T20:37:26Z.
Sandy City publishes no licence for this data; see the [README](README.md).
