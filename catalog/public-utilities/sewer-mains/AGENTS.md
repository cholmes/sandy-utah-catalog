# AGENTS.md — Sewer Mains

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-mains/sewer-mains.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

21 columns, 16,250 rows.

12 of 21 columns carry a definition. The rest say so rather than guess.

**`Agency`** — *string*  
One of. The source layer's domain allows: `Cottonwood Improvement District`, `Midvale City`, `Midvalley Improvement District`, `Sandy Suburban Improvement District`, `South Valley Sewer District`, `Other/Unknown`.

**`PipeDiam`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 16,250 rows, 24 distinct values, ranging 0 to 99.

**`PipeType`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 98% of 16,250 rows, 25 distinct values.

**`Type`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 68% of 16,250 rows, 11 distinct values.

**`InstYear`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 44% of 16,250 rows, 89 distinct values, ranging 0 to 44670.

**`ID`** — *string*  
Identifier assigned by the source layer. Measured in the published file: Populated on 98% of 16,250 rows, 12,676 distinct values.

**`SLOPE`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 35% of 16,250 rows, 4,950 distinct values, ranging -28.0633 to 319.96.

**`FROM_INV`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 35% of 16,250 rows, 4,628 distinct values, ranging 0 to 43777.3.

**`TO_INV`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 35% of 16,250 rows, 4,032 distinct values, ranging 0 to 5354.18.

**`Up_MH`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 34% of 16,250 rows, 4,055 distinct values.

**`Down_Mh`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 34% of 16,250 rows, 3,423 distinct values.

**`NumConnect`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 23% of 16,250 rows, 18 distinct values, ranging 0 to 18.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`created_user`** — *string*  
Username of the staff member who created the row, from the geodatabase editor tracking.

**`created_date`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`last_edited_user`** — *string*  
Username of the staff member who last edited the row, from the geodatabase editor tracking.

**`last_edited_date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`Shape.len`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-mains/sewer-mains.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Agency", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-mains/sewer-mains.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `South Valley Sewer District` — 5,378
- `Cottonwood Improvement District` — 5,263
- `Sandy Suburban Improvement District` — 3,766
- `Midvalley Improvement District` — 1,843

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/2](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/2?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
