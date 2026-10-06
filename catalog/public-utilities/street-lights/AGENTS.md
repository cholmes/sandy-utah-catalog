# AGENTS.md — Street Lights

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/street-lights/street-lights.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

34 columns, 8,727 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `POLE_NUM` | double |
| `COMMENTS` | string |
| `GPS_DATE` | timestamp[ms] |
| `NORTHING` | double |
| `EASTING` | double |
| `JURISDICTI` | string |
| `FIXTURE_TY` | string |
| `LAMP_TYPE` | string |
| `WATTS` | double |
| `LUMEN` | double |
| `NUM_HEADS` | int32 |
| `RATE` | string |
| `POLE_TYPES` | string |
| `FEATURE_ID` | double |
| `DATE_INSTA` | timestamp[ms] |
| `POLESUFFIX` | int32 |
| `LOCATION` | string |
| `EPOLE_NUM` | string |
| `FacilityID` | string |
| `FIXTURE_INSTALL` | timestamp[ms] |
| `SANDY_NUMBER` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `STATUS` | string |
| `LampInstall` | timestamp[ms] |
| `PoleReplace` | timestamp[ms] |
| `WATTS_2` | double |
| `Lamp_Temperature` | string |
| `POLE_OWNER` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`STATUS`**

- `Existing` = Existing Feature
- `Construction` = Under Construction
- `Retired` = Retired
- `Abandoned` = Abandoned In Place
- `Proposed` = Planned/Proposed
- `Unknown` = Unknown/Needs Verification

**`Lamp_Temperature` — Lamp Temperature**

- `4000K` = 4000K
- `3000K` = 3000K
- `NA` = NA

**`POLE_OWNER`**

- `Sandy City` = Sandy City
- `RMP` = Rocky Mountain Power
- `Private` = Private
- `UDOT` = UDOT
- `Salt Lake County` = Salt Lake County
- `Communications` = Communications

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/street-lights/street-lights.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StreetLights/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StreetLights/FeatureServer/0) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
