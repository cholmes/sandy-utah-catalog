# AGENTS.md — Fire Dispatch Subdistricts

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-subdistricts/fire-subdistricts.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

15 columns, 39 rows.

9 of 15 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`CITY`** — *string*  
City the feature falls in. Measured in the published file: Populated on 100% of 39 rows, 1 distinct values.

**`CITY_CODE`** — *string*  
Short code for the municipality. Measured in the published file: Populated on 100% of 39 rows, 1 distinct values.

**`FireZoneID`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Empty in all 39 rows of the published file.

**`Agency`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 39 rows, 1 distinct values.

**`ID`** — *int32*  
Identifier assigned by the source layer. Measured in the published file: Populated on 100% of 39 rows, 5 distinct values, ranging 31 to 35.

**`Stack_2_Deep`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 39 rows, 13 distinct values.

**`Stack_3_Deep`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 39 rows, 16 distinct values.

**`Stack_4_Deep`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 39 rows, 16 distinct values.

**`Stack_5_Deep`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 39 rows, 17 distinct values.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`Shape.STArea()`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape.STLength()`** — *double*  
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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-subdistricts/fire-subdistricts.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "ID", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-subdistricts/fire-subdistricts.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `32` — 12
- `34` — 9
- `31` — 9
- `33` — 5
- `35` — 4

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Fire_Subdistricts/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Fire_Subdistricts/MapServer/1?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
