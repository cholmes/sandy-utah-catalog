# AGENTS.md — Sewer Manholes

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-manholes/sewer-manholes.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

19 columns, 16,020 rows.

11 of 19 columns carry a definition. The rest say so rather than guess.

**`Agency`** — *string*  
One of. The source layer's domain allows: `Cottonwood Improvement District`, `Midvale City`, `Midvalley Improvement District`, `Sandy Suburban Improvement District`, `South Valley Sewer District`, `Other/Unknown`.

**`DIAMETER`** — *double*  
Nominal diameter, in inches. Measured in the published file: Populated on 68% of 16,020 rows, 10 distinct values, ranging 0 to 60.

**`RIM_ELEV`** — *double*  
Elevation of the structure rim at ground level. Measured in the published file: Populated on 100% of 16,020 rows, 14,444 distinct values, ranging 0 to 4.89188e+06.

**`X`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 16,020 rows, 13,767 distinct values, ranging -111.898 to 7.38729e+06.

**`Y`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 16,020 rows, 14,029 distinct values, ranging -111.884 to 7.63885e+06.

**`DepthToFlo`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 56% of 16,020 rows, 3,560 distinct values, ranging 0 to 1911.

**`NumPipesIn`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 24% of 16,020 rows, 5 distinct values, ranging 0 to 5.

**`InSizes`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 24% of 16,020 rows, 18 distinct values.

**`OutSize`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 24% of 16,020 rows, 12 distinct values.

**`MH_ID`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 16,020 rows, 14,969 distinct values.

**`NumLateral`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 24% of 16,020 rows, 5 distinct values, ranging 0 to 15.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/sewer-manholes/sewer-manholes.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/Sewer/MapServer/1?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
