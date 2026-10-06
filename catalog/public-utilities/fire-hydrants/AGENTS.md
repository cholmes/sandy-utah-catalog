# AGENTS.md — Fire Hydrants

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/fire-hydrants/fire-hydrants.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

45 columns, 5,292 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `FACILITYID` | string |
| `HYD_ID` | int32 |
| `COMMENTS` | string |
| `GPS_DATE` | timestamp[ms] |
| `NORTHING` | double |
| `EASTING` | double |
| `PROVIDER` | string |
| `MAP_NO` | string |
| `APADDRESS` | string |
| `LANDTIES` | string |
| `HYDSIZE` | double |
| `HYD_TYPE` | string |
| `HYD_MANUF` | string |
| `MANUF_DATE` | string |
| `VDEPTH` | string |
| `VLOCAT` | string |
| `VSIZE` | double |
| `VTYPE` | string |
| `VMAUF` | string |
| `VMAUNFDATE` | double |
| `INSTDATE` | timestamp[ms] |
| `DATECOLT` | timestamp[ms] |
| `COLLTBY` | string |
| `OTHER_INFO` | string |
| `ACAD_ANGLE` | double |
| `ENABLED` | int16 |
| `ANCILLARYROLE` | int16 |
| `LOCATION` | string |
| `INSPDATE` | timestamp[ms] |
| `RESIDPRESSURE` | double |
| `STATICPRESSURE` | double |
| `TWENTYPSIFLOW` | double |
| `THIRTYPSIFLOW` | double |
| `WATER_ENTITY` | string |
| `FIRE_INSP_DIST` | string |
| `CONST_STATUS` | string |
| `STATUS` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `AssetStatus` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`PROVIDER`**

- `SANDY` = Sandy
- `OTHER` = Other
- `Midvale` = Midvale

**`HYDSIZE`**

- `4` = 4"
- `5.25` = 5.25"

**`HYD_TYPE`**

- `SCISSORS` = SCISSORS
- `COMPRESSION` = COMPRESSION

**`HYD_MANUF`**

- `CLOW` = CLOW
- `IOWA` = IOWA
- `WATEROUS` = WATEROUS
- `PACIFIC STATES` = PACIFIC STATES
- `KENNEDY` = KENNEDY
- `OTHER` = OTHER
- `MUELLER` = MUELLER
- `EJ` = EJ

**`VSIZE`**

- `2` = 2"
- `4` = 4"
- `8` = 8"
- `10` = 10"
- `12` = 12"
- `14` = 14"
- `16` = 16"
- `20` = 20"
- `24` = 24"
- `30` = 30"
- `33` = 33"
- `36` = 36"
- `6` = 6"

**`VTYPE`**

- `GATE` = GATE VALVE
- `BUTTERFLY` = BUTTERFLY VALVE
- `OTHER` = OTHER VALVE
- `UNKNOWN` = UNKOWN VALVE

**`VMAUF`**

- `MUELLER` = MUELLER
- `AFC` = AFC
- `WATTEROUS` = WATTEROUS
- `CLOW` = CLOW
- `PRATT` = PRATT
- `OTHER` = OTHER
- `KENNEDY` = KENNEDY
- `VAL-MATIC` = VAL-MATIC
- `EJ` = EJ
- `AVTEK` = AVTEK
- `N/A` = N/A

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

**`STATUS`**

- `In Service` = In Service
- `Out of Service` = Out of Service
- `Needs Repair` = Needs Repair
- `Needs Inspection` = Needs Inspection
- `INS / Obstructed` = INS/Obstructed
- `Outside Service Area` = Outside Service Area
- `Low PSI - Never Insp` = Low PSI - Never Insp

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/fire-hydrants/fire-hydrants.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/1) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
