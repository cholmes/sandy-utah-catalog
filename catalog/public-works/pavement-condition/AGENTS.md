# AGENTS.md — Pavement Condition

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/pavement-condition/pavement-condition.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

37 columns, 2,165 rows.


**Where these meanings come from.** Pavement management segments. `GASB_` columns support reporting under Governmental Accounting Standards Board Statement 34, which lets a government report infrastructure using a condition assessment instead of depreciation.

16 of 37 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Location`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 100% of 2,165 rows, 2,165 distinct values.

**`PMA_TXT`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 2,165 distinct values.

**`Section_Num`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 2,165 distinct values.

**`Municipality`** — *string*  
Municipality the feature falls in. Several Sandy layers extend into neighbouring cities, so this is how to select Sandy's own. Measured in the published file: Populated on 100% of 2,165 rows, 1 distinct values.

**`PWA`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 20 distinct values, ranging 1 to 20.

**`Council_District`** — *string*  
Sandy city council district the segment falls in.

**`Quadrant`** — *string*  
Sandy addressing and policing quadrant. Measured in the published file: Populated on 100% of 2,165 rows, 9 distinct values.

**`Street_Name`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 1,652 distinct values.

**`From_Location`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 994 distinct values.

**`To_Location`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 842 distinct values.

**`FunctionClass`** — *string*  
Functional classification of the road segment.

**`GIS_Length`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 2,165 rows, 2,137 distinct values, ranging 73.6454 to 7483.64.

**`GIS_Width`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 2,165 rows, 70 distinct values, ranging 13 to 90.

**`Avg_SectionWidth`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 81 distinct values, ranging 0 to 240.

**`RM_Length`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 995 distinct values, ranging 78 to 7484.

**`RM_Width`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 70 distinct values, ranging 13 to 90.

**`RM_Area`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 1,489 distinct values, ranging 2500 to 264272.

**`Pavement_Type`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 2 distinct values.

**`AADT_Count`** — *int32*  
Annual average daily traffic assigned to the segment. The values are banded rather than measured per segment.

**`AADT_Date`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 372 distinct values.

**`Lanes`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 5 distinct values, ranging 1 to 5.

**`One_Way`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 2,165 rows, 2 distinct values, ranging 0 to 1.

**`PQI`** — *double*  
Pavement Quality Index, the condition score the city's pavement management system assigns to the segment.

**`PQI_Date`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 33 distinct values.

**`Year_Built`** — *string*  
Year the feature was built. Measured in the published file: Populated on 97% of 2,165 rows, 56 distinct values.

**`Cost_Window`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 1 distinct values.

**`Costs_SqFt`** — *double*  
Unit treatment cost in dollars per square foot used in the city's budget model.

**`Road_Value`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 1,534 distinct values, ranging 11700 to 2.38972e+06.

**`GASB_Class`** — *string*  
Road class used for GASB 34 reporting: Arterial, Collector or Secondary.

**`GASB_Cond_Group`** — *string*  
Condition band used for GASB 34 reporting: Good, Fair or Poor.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`Date_Built_Annexed`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 2,165 rows, 7 distinct values.

**`Road_Source`** — *string*  
One of. The source layer's domain allows: `Annexation`, `Developer`, `City`, `Other`.

**`Maintenance_District`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 2,165 rows, 20 distinct values.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/pavement-condition/pavement-condition.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "GASB_Cond_Group", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/pavement-condition/pavement-condition.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Good` — 1,543
- `Fair` — 540
- `Poor` — 48

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/PMA_Segments/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/PMA_Segments/FeatureServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
