# AGENTS.md — Water Distribution Mains

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/public-utilities/water-distribution-mains/water-distribution-mains.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

17 columns, 15,249 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `DIAMETER` | int16 |
| `LINE_TYPE` | int16 |
| `YEAR_` | int16 |
| `FACILITYID` | string |
| `ENABLED` | int16 |
| `WATER_ENTITY` | string |
| `CONST_STATUS` | string |
| `Shape__Length` | double |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `TracerWire` | string |
| `AssetStatus` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`DIAMETER`**

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

**`LINE_TYPE`**

- `12` = HDPE
- `1` = DIP
- `2` = CIP
- `4` = TRANSITE
- `5` = BLUE BRUTE
- `6` = GALVANIZED
- `8` = STEEL
- `10` = PVC
- `11` = PVC C90 DR14
- `13` = POLY
- `14` = Copper

**`ENABLED` — Enabled**

- `0` = False
- `1` = True

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/public-utilities/water-distribution-mains/water-distribution-mains.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "WATER_ENTITY", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/public-utilities/water-distribution-mains/water-distribution-mains.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Sandy` — 14,855
- `Private` — 392
- `JVW` — 2

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/8](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/8) on 2026-10-06T19:24:57Z.
Sandy City publishes no licence for this data; see the [README](README.md).
