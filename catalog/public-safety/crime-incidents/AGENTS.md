# AGENTS.md — Crime Incidents

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/crime-incidents/crime-incidents.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

42 columns, 29,572 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `evt_reference` | string |
| `jurisdiction` | string |
| `evt_date` | timestamp[ms] |
| `evt_time` | int16 |
| `location` | string |
| `zone` | string |
| `grid` | string |
| `occ_date` | timestamp[ms] |
| `occ_time` | int16 |
| `to_occ_date` | timestamp[ms] |
| `to_occ_time` | int16 |
| `week_day_d` | string |
| `week_day` | int16 |
| `rucr` | string |
| `rext` | string |
| `rucr_ext_d` | string |
| `rucr_ext_exp_d` | string |
| `location_code` | string |
| `location_code_d` | string |
| `weapon_type1` | string |
| `weapon_type1_d` | string |
| `ibr_code` | string |
| `operational_code` | string |
| `operational_code_d` | string |
| `sort_order` | int32 |
| `evt_date_time_text` | string |
| `occ_date_time_text` | string |
| `to_occ_date_time_text` | string |
| `hour` | int32 |
| `month` | int32 |
| `day` | int32 |
| `year` | int32 |
| `unique_id` | double |
| `ORIG_FID` | int32 |
| `CATEGORY` | string |
| `DESCRIPTION` | string |
| `TYPE` | string |
| `Extension` | string |
| `TimeOfDay` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/crime-incidents/crime-incidents.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "TimeOfDay", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/crime-incidents/crime-incidents.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Afternoon` — 8,386
- `Mid-Day` — 7,259
- `Evening` — 5,954
- `Morning` — 3,823
- `Late Night` — 3,031
- `Overnight` — 1,119

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCrimeData/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCrimeData/FeatureServer/0) on 2026-10-06T21:15:15Z.
Sandy City publishes no licence for this data; see the [README](README.md).
