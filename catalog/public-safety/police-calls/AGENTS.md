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


**Where these meanings come from.** Calls for service from the Sandy City Police Department computer aided dispatch system. A call for service is not a confirmed offence; many close with no crime found.

46 of 46 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`evt_rin`** — *string*  
Dispatch record identifier.

**`evt_reference`** — *string*  
Case reference number, which joins a call to an offence record in `crime-incidents` where one was written.

**`jurisdiction`** — *string*  
Agency code for the responding jurisdiction.

**`evt_date`** — *timestamp[ms]*  
Date of the call.

**`location`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 100% of 185,647 rows, 29,425 distinct values.

**`zone`** — *string*  
Police zone the call falls in.

**`grid`** — *string*  
Police reporting grid cell, joining to `police-reporting-areas`.

**`week_day`** — *int16*  
Day of week as a number.

**`week_day_d`** — *string*  
Day of week as a name.

**`received_dt`** — *timestamp[ms]*  
Time dispatch received the call.

**`dispatch_dt`** — *timestamp[ms]*  
Time a unit was dispatched.

**`enroute_dt`** — *timestamp[ms]*  
Time the unit started travelling.

**`at_scene_dt`** — *timestamp[ms]*  
Time the unit arrived.

**`clear_dt`** — *timestamp[ms]*  
Time the unit cleared the call.

**`case_type`** — *string*  
Initial call-type code assigned by the dispatcher.

**`case_type_d`** — *string*  
Call type as first coded by the dispatcher.

**`priority`** — *int16*  
Dispatch priority. 1 is the most urgent. Priority 9 is the largest group at 69,639 rows and covers routine and administrative calls.

**`how_received`** — *string*  
Code for how the call reached dispatch. `how_received_d` is the readable form.

**`how_received_d`** — *string*  
How the call reached dispatch: by telephone, through the 911 system, or on view, meaning an officer observed it directly.

**`cleared_by`** — *string*  
Code for how the call was closed.

**`cleared_by_d`** — *string*  
How the call was closed.

**`final_case_type`** — *string*  
Final call-type code after the officer cleared the call.

**`final_case_type_d`** — *string*  
Call type after the officer cleared the call. This differs from the initial type whenever the reported problem was not what was found.

**`agg_time_to_dispatch`** — *int32*  
Elapsed seconds from receipt to dispatch.

**`agg_travel_time`** — *int32*  
Elapsed seconds from dispatch to arrival.

**`agg_response_time`** — *int32*  
Elapsed seconds from receipt to arrival. Negative values occur in the source data and should be filtered before use.

**`agg_time_on_scene`** — *int32*  
Elapsed seconds on scene.

**`agg_service_time`** — *int32*  
Elapsed seconds from receipt to the unit clearing.

**`report_year`** — *int16*  
Year the call was reported, as carried by the records system.

**`year`** — *int32*  
Year of the call.

**`month`** — *int32*  
Month of the call as a number.

**`hour`** — *int32*  
Hour of the call, 0 to 23.

**`agg_time_to_dispatch_minutes`** — *double*  
Time to dispatch, in minutes.

**`agg_travel_time_minutes`** — *double*  
Travel time in minutes.

**`agg_response_time_minutes`** — *double*  
Response time in minutes, the same measure as `agg_response_time` divided by sixty.

**`agg_service_time_minutes`** — *double*  
Total service time, in minutes.

**`received_date_text`** — *string*  
Receipt timestamp as text, kept from the export.

**`dispatch_date_text`** — *string*  
Dispatch timestamp as text.

**`enroute_date_text`** — *string*  
En-route timestamp as text.

**`at_scene_date_text`** — *string*  
Arrival timestamp as text.

**`clear_date_text`** — *string*  
Clear timestamp as text.

**`clear_date_text2`** — *string*  
Second clear timestamp as text, kept from the export.

**`ORIG_FID`** — *int32*  
Row identifier from the table this layer was built from.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCallData/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCallData/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
