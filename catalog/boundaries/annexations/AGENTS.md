# AGENTS.md — Annexations

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/annexations/annexations.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

19 columns, 521 rows.

9 of 19 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Year`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 521 rows, 68 distinct values, ranging 1893 to 2026.

**`Name`** — *string*  
Name of the feature. Measured in the published file: Populated on 100% of 521 rows, 517 distinct values.

**`Type`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 100% of 521 rows, 4 distinct values.

**`Governing_Jurisdiction`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 521 rows, 2 distinct values.

**`Old_Jurisdiction`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 521 rows, 5 distinct values.

**`Effective_Date`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 521 rows, 367 distinct values.

**`Acres`** — *double*  
Area in acres. Measured in the published file: Populated on 100% of 521 rows, 515 distinct values, ranging 0.0165 to 1304.19.

**`SLCO_Map_Record_Numb`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 521 rows, 517 distinct values.

**`SLCO_Map_Book_Page`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 521 rows, 517 distinct values.

**`SLCO_Ord_Record_Numb`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 92% of 521 rows, 469 distinct values.

**`SLCO_Ord_Book_Page`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 93% of 521 rows, 473 distinct values.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`Eff_Date_Notes`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 521 rows, 12 distinct values.

**`Sandy_Ord_Num`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 521 rows, 260 distinct values.

**`Shape.area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape.len`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/annexations/annexations.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Type", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/annexations/annexations.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Annexation` — 516
- `Boundary Adjustment` — 3
- `Incorporation` — 1
- `Correction` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Annexations/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Annexations/MapServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
