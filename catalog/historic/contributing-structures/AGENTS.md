# AGENTS.md — Contributing Historic Structures (2026 Study)

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/historic/contributing-structures/contributing-structures.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

13 columns, 275 rows.

8 of 13 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`House__`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 275 rows, 223 distinct values, ranging 10 to 8984.

**`Dir`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 275 rows, 2 distinct values.

**`Street`** — *string*  
Street the feature lies on. Measured in the published file: Populated on 100% of 275 rows, 29 distinct values.

**`Eval_Code`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 275 rows, 1 distinct values.

**`Year_Built`** — *int32*  
Year the feature was built. Measured in the published file: Populated on 100% of 275 rows, 45 distinct values, ranging 1874 to 1959.

**`Individually_Listed`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 275 rows, 1 distinct values.

**`Address`** — *string*  
Street address of the feature. Measured in the published file: Populated on 100% of 275 rows, 273 distinct values.

**`X_Coord`** — *double*  
X coordinate copied into an attribute. The geometry column is authoritative. Measured in the published file: Populated on 100% of 275 rows, 274 distinct values, ranging 1.53193e+06 to 1.53665e+06.

**`Y_Coord`** — *double*  
Y coordinate copied into an attribute. The geometry column is authoritative. Measured in the published file: Populated on 100% of 275 rows, 273 distinct values, ranging 7.38329e+06 to 7.38626e+06.

**`Plaque`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Empty in all 275 rows of the published file.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/historic/contributing-structures/contributing-structures.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/2026_Contributing_Structures_Study/FeatureServer/0](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/2026_Contributing_Structures_Study/FeatureServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
