# AGENTS.md — Sandy Water Wells

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/wells/wells.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

33 columns, 24 rows.

5 of 33 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`SYSNUM`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 2 distinct values, ranging 0 to 18028.

**`SORNUM`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 19 distinct values, ranging 0 to 28.

**`EPAID`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 88% of 24 rows, 17 distinct values.

**`SOWN`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 92% of 24 rows, 1 distinct values.

**`SNAM`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 92% of 24 rows, 22 distinct values.

**`GPM3`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 15 distinct values, ranging 0 to 3000.

**`STYP`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 88% of 24 rows, 1 distinct values.

**`DIAM`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 3 distinct values, ranging 0 to 2.

**`CODE`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 2 distinct values, ranging 0 to 6.

**`LABEL`** — *string*  
Short label used on the city's own maps. Measured in the published file: Populated on 96% of 24 rows, 22 distinct values.

**`STATE_ID`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 75% of 24 rows, 16 distinct values.

**`DESCR`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Empty in all 24 rows of the published file.

**`OLD_LABEL`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 88% of 24 rows, 19 distinct values.

**`NEW_LABEL`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 24 distinct values.

**`UHDID`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 92% of 24 rows, 20 distinct values.

**`GREG_`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 20 distinct values, ranging 0 to 235.

**`GREG_ID`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 20 distinct values, ranging 0 to 323.

**`HDDWS_ALL_`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 20 distinct values, ranging 0 to 243.

**`HDDWS_ALL1`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 1 distinct values.

**`COMMENT`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`CH2MGRID_`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 20 distinct values, ranging 0 to 110042.

**`CH2MGRID_I`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 20 distinct values, ranging 0 to 110041.

**`CH2MCELL`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 20 distinct values, ranging 0 to 110041.

**`CH2MROW`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 17 distinct values, ranging 0 to 401.

**`CH2MCOL`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 19 distinct values, ranging 0 to 261.

**`CH2MAREA`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 5 distinct values, ranging 0 to 9287.09.

**`OWNER`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 24 rows, 1 distinct values.

**`Q_`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Empty in all 24 rows of the published file.

**`Q_COMMENT`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 4% of 24 rows, 1 distinct values.

**`TC_COMMENT`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 4% of 24 rows, 1 distinct values.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/wells/wells.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SourceProtectionWells/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SourceProtectionWells/FeatureServer/1?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
