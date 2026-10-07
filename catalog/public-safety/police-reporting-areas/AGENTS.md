# AGENTS.md — Police Reporting Areas

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-reporting-areas/police-reporting-areas.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

16 columns, 439 rows.

10 of 16 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`OLDAREA`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 93% of 439 rows, 383 distinct values.

**`CITY`** — *string*  
City the feature falls in. Measured in the published file: Populated on 100% of 439 rows, 1 distinct values.

**`CITYDESCR`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 439 rows, 1 distinct values.

**`DISP_AREA`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 439 rows, 4 distinct values.

**`DISP_AREA_`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 439 rows, 4 distinct values.

**`TYPE`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 100% of 439 rows, 9 distinct values.

**`TYPE_DESC`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 439 rows, 9 distinct values.

**`STATUS`** — *string*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 100% of 439 rows, 2 distinct values.

**`REPT_AREA`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 439 rows, 439 distinct values.

**`ACRES`** — *double*  
Area in acres. Measured in the published file: Populated on 100% of 439 rows, 426 distinct values, ranging 0 to 696.573.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-reporting-areas/police-reporting-areas.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "TYPE_DESC", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-reporting-areas/police-reporting-areas.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Residential` — 100
- `Commercial` — 88
- `Intersection` — 71
- `Apt, Condo, Hotel, Motel` — 62
- `Park, Cemetery, Forest` — 54
- `School, College` — 29
- `Moble/Twin homes` — 13
- `Freeway segment` — 12
- `TRAX or Rail Crossing` — 10

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Police_Reporting_Areas/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Police_Reporting_Areas/MapServer/1?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
