# AGENTS.md — Zoning Districts

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/zoning/zoning.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

13 columns, 454 rows.

7 of 13 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`ZONE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 454 rows, 114 distinct values.

**`ZONE_ACREA`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 95% of 454 rows, 390 distinct values, ranging 0 to 2646.88.

**`LEGEND_COD`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 454 rows, 25 distinct values.

**`SD_ZONE`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 454 rows, 2 distinct values.

**`NAME`** — *string*  
Name of the feature. Measured in the published file: Populated on 6% of 454 rows, 3 distinct values.

**`Definition`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 454 rows, 76 distinct values.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`Editor_Date`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`Zone_Code`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Empty in all 454 rows of the published file.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/zoning/zoning.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "LEGEND_COD", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/zoning/zoning.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `R2` — 83
- `R3` — 66
- `MF2` — 40
- `R1` — 38
- `MF1` — 30
- `R4` — 28
- `OS1` — 25
- `MF4` — 24
- `PO1` — 22
- `R5` — 14
- `C3` — 11
- `C1` — 10

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Zoning_Ex/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Zoning_Ex/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
