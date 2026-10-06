# AGENTS.md — Speed Limits

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/speed-limits/speed-limits.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

50 columns, 5,072 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `L_F_ADD` | double |
| `L_T_ADD` | double |
| `R_F_ADD` | double |
| `R_T_ADD` | double |
| `PRE_DIR` | string |
| `S_NAME` | string |
| `S_TYPE` | string |
| `SUF_DIR` | string |
| `ACS_ALIAS` | string |
| `ACS_STREET` | string |
| `ACS_SUFDIR` | string |
| `LABEL` | string |
| `L_CITYCD` | string |
| `R_CITYCD` | string |
| `LS_ZONE` | string |
| `FS_ZONE` | string |
| `LZIP` | string |
| `RZIP` | string |
| `ONE_WAY` | int32 |
| `SPEED_LIMIT` | int32 |
| `COMMENTS` | string |
| `VECCOMMENTS` | string |
| `UNIQUE_ID` | int32 |
| `EXCLUDE` | string |
| `S_DATE` | timestamp[ms] |
| `M_DATE` | timestamp[ms] |
| `SOURCE` | string |
| `S_SURF` | int32 |
| `L_JURIS` | int32 |
| `R_JURIS` | int32 |
| `S_ROW` | int32 |
| `S_ACCESS` | string |
| `S_USE` | string |
| `S_ACCUR` | int32 |
| `CFCC` | string |
| `ALT_NAME` | string |
| `STREET` | string |
| `LOW` | double |
| `HIGH` | double |
| `MAINTENANCE` | string |
| `FUNCTIONAL_CLASS` | string |
| `CARTO_CODE` | string |
| `DATA_DATE` | timestamp[ms] |
| `DATA_EDITOR` | string |
| `RuleID` | int32 |
| `Shape` | binary |
| `Shape.STLength()` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`PRE_DIR`**

- `N` = N
- `E` = E
- `W` = W
- `S` = S

**`S_TYPE`**

- `ALY` = ALY
- `AVE` = AVE
- `BAY` = BAY
- `BLVD` = BLVD
- `CIR` = CIR
- `COL` = COL
- `CON` = CON
- `CT` = CT
- `CTR` = CTR
- `CV` = CV
- `CYN` = CYN
- `DR` = DR
- `EXPY` = EXPY
- `FORK` = FORK
- `FWY` = FWY
- `GTWY` = GTWY

**`SUF_DIR`**

- `N` = N
- `E` = E
- `W` = W
- `S` = S

**`ACS_SUFDIR`**

- `N` = N
- `E` = E
- `W` = W
- `S` = S

**`L_CITYCD` — Lcitycd**

- `ALT` = ALT
- `BLU` = BLU
- `COP` = COP
- `COT` = COT
- `DRA` = DRA
- `HER` = HER
- `HOL` = HOL
- `INT` = INT
- `KEA` = KEA
- `MAG` = MAG
- `MID` = MID
- `MUR` = MUR
- `RIV` = RIV
- `SAN` = SAN
- `SCO` = SCO
- `SJC` = SJC

**`R_CITYCD` — Rcitycd**

- `ALT` = ALT
- `BLU` = BLU
- `COP` = COP
- `COT` = COT
- `DRA` = DRA
- `HER` = HER
- `HOL` = HOL
- `INT` = INT
- `KEA` = KEA
- `MAG` = MAG
- `MID` = MID
- `MUR` = MUR
- `RIV` = RIV
- `SAN` = SAN
- `SCO` = SCO
- `SJC` = SJC

**`ONE_WAY`**

- `0` = 0
- `1` = 1
- `2` = 2

**`RuleID`**

- `1` = All other values
- `2` = Freeways
- `3` = Major Roads
- `4` = Gravel;Private;Streets
- `5` = Ramps
- `6` = Do Not Display

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/speed-limits/speed-limits.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "SPEED_LIMIT", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/speed-limits/speed-limits.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `25` — 4,064
- `35` — 431
- `30` — 381
- `40` — 94
- `45` — 83
- `15` — 15
- `10` — 3
- `5` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Speed_Limits/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Speed_Limits/MapServer/1) on 2026-10-06T19:54:13Z.
Sandy City publishes no licence for this data; see the [README](README.md).
