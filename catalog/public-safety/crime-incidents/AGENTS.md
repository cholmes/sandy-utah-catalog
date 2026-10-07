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


**Where these meanings come from.** Offence records exported from the Sandy City Police Department records system. `rucr` and `ibr_code` are National Incident-Based Reporting System classifications; see the Bureau of Justice Statistics on the [National Incident-Based Reporting System](https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs).

20 of 42 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`evt_reference`** — *string*  
Case reference number in the police records system.

**`jurisdiction`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 1 distinct values.

**`evt_date`** — *timestamp[ms]*  
Date the event was reported.

**`evt_time`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 1,437 distinct values, ranging 0 to 2359.

**`location`** — *string*  
Street-level address of the incident. The unit or apartment number was removed before publication.

**`zone`** — *string*  
Police zone the incident falls in.

**`grid`** — *string*  
Police reporting grid cell, joining to the `police-reporting-areas` collection.

**`occ_date`** — *timestamp[ms]*  
Date the offence is believed to have occurred, which can precede the report date.

**`occ_time`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 1,436 distinct values, ranging 0 to 2359.

**`to_occ_date`** — *timestamp[ms]*  
End of the window the offence is believed to have occurred in, where the exact time is unknown.

**`to_occ_time`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 11% of 29,572 rows, 702 distinct values, ranging 0 to 2359.

**`week_day_d`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 7 distinct values.

**`week_day`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 7 distinct values, ranging 1 to 7.

**`rucr`** — *string*  
Offence code in the agency's records system.

**`rext`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 50 distinct values.

**`rucr_ext_d`** — *string*  
Offence description, the readable form of `rucr`.

**`rucr_ext_exp_d`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 245 distinct values.

**`location_code`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 29,572 rows, 43 distinct values.

**`location_code_d`** — *string*  
Type of place the offence occurred at.

**`weapon_type1`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 10% of 29,572 rows, 16 distinct values.

**`weapon_type1_d`** — *string*  
Weapon involved, where one is recorded.

**`ibr_code`** — *string*  
NIBRS offence code reported to the FBI.

**`operational_code`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 13 distinct values.

**`operational_code_d`** — *string*  
Case disposition, such as closed by arrest.

**`sort_order`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 1 distinct values.

**`evt_date_time_text`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 29,049 distinct values.

**`occ_date_time_text`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 28,725 distinct values.

**`to_occ_date_time_text`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 11% of 29,572 rows, 3,239 distinct values.

**`hour`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 24 distinct values, ranging 0 to 23.

**`month`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 12 distinct values, ranging 1 to 12.

**`day`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 31 distinct values, ranging 1 to 31.

**`year`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 4 distinct values, ranging 2023 to 2026.

**`unique_id`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 29,572 distinct values, ranging 1 to 38649.

**`ORIG_FID`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 29,572 rows, 1 distinct values.

**`CATEGORY`** — *string*  
Grouped offence category.

**`DESCRIPTION`** — *string*  
Description of the feature, entered by city staff. Measured in the published file: Populated on 58% of 29,572 rows, 61 distinct values.

**`TYPE`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 18% of 29,572 rows, 2 distinct values.

**`Extension`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 6% of 29,572 rows, 1 distinct values.

**`TimeOfDay`** — *string*  
Band the event time falls in, derived by the city.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCrimeData/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCrimeData/FeatureServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
