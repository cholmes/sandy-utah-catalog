# AGENTS.md — Police Calls for Service

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-calls/police-calls.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

46 columns, 185,647 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `evt_rin` | string |
| `evt_reference` | string |
| `jurisdiction` | string |
| `evt_date` | timestamp[ms] |
| `location` | string |
| `zone` | string |
| `grid` | string |
| `week_day` | int16 |
| `week_day_d` | string |
| `received_dt` | timestamp[ms] |
| `dispatch_dt` | timestamp[ms] |
| `enroute_dt` | timestamp[ms] |
| `at_scene_dt` | timestamp[ms] |
| `clear_dt` | timestamp[ms] |
| `case_type` | string |
| `case_type_d` | string |
| `priority` | int16 |
| `how_received` | string |
| `how_received_d` | string |
| `cleared_by` | string |
| `cleared_by_d` | string |
| `final_case_type` | string |
| `final_case_type_d` | string |
| `agg_time_to_dispatch` | int32 |
| `agg_travel_time` | int32 |
| `agg_response_time` | int32 |
| `agg_time_on_scene` | int32 |
| `agg_service_time` | int32 |
| `report_year` | int16 |
| `year` | int32 |
| `month` | int32 |
| `hour` | int32 |
| `agg_time_to_dispatch_minutes` | double |
| `agg_travel_time_minutes` | double |
| `agg_response_time_minutes` | double |
| `agg_service_time_minutes` | double |
| `received_date_text` | string |
| `dispatch_date_text` | string |
| `enroute_date_text` | string |
| `at_scene_date_text` | string |
| `clear_date_text` | string |
| `clear_date_text2` | string |
| `ORIG_FID` | int32 |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-calls/police-calls.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "how_received_d", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-calls/police-calls.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `TELEPHONE` — 88,777
- `ON VIEW` — 57,323
- `911 SYSTEM` — 38,912
- `RECURRING CALL` — 618
- `REMOTE CAD` — 14
- `TRAFFIC STOP` — 1
- `EXTERNAL` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCallData/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCallData/FeatureServer/0) on 2026-10-06T21:15:15Z.
Sandy City publishes no licence for this data; see the [README](README.md).
