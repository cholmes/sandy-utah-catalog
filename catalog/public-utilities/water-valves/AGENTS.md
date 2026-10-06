# AGENTS.md — Water Valves

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-valves/water-valves.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

38 columns, 8,117 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `WVALVES_ID` | string |
| `FACILITYID` | string |
| `NORTHING` | double |
| `EASTING` | double |
| `ELEVATION` | double |
| `ENABLED` | int16 |
| `DATEINSPECTED` | timestamp[ms] |
| `INSPECTED_BY` | string |
| `COMMENTS` | string |
| `MAP_NO` | string |
| `ADDRESS` | string |
| `LAND_TIES` | string |
| `VALVE_SIZE` | int16 |
| `VALVE_DEPTH` | double |
| `VALVE_TYPE` | string |
| `VALVE_FUNCTION` | string |
| `VALVE_MANU` | string |
| `TURNS_TO_CLOSE` | double |
| `DIRECTION` | string |
| `INSTALL_DATE` | timestamp[ms] |
| `COLLECTED_BY` | string |
| `DATE_COLLECTED` | timestamp[ms] |
| `MANFAC_DATE` | int32 |
| `SHUT_DOWN` | string |
| `OTHER_INFO` | string |
| `PWTYPE` | string |
| `LOCATION` | string |
| `OPERATION_MODE` | string |
| `WATER_ENTITY` | string |
| `CONST_STATUS` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `GPS_DATE` | timestamp[ms] |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`ENABLED` — Enabled**

- `0` = False
- `1` = True

**`VALVE_SIZE` — Valve Size**

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

**`VALVE_TYPE` — Vavle Type**

- `GATE` = Gate Valve
- `BUTTERFLY` = Butterfly Valve
- `OTHER` = Other Valve
- `UNKNOWN` = Unknown Valve

**`VALVE_FUNCTION` — Valve Function**

- `Main` = Main Valve
- `Aux` = Aux Hyd Valve
- `MeterV` = Meter Valve
- `Fireline` = Fire Line Valve
- `ZB` = Zone Break Valve
- `SepV` = Seperation Valve

**`VALVE_MANU` — Valve Manufacturer**

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

**`DIRECTION` — Turn Direction**

- `R` = Right Hand
- `L` = Left Hand

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-valves/water-valves.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/0) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
