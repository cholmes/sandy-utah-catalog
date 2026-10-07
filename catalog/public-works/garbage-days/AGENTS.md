# AGENTS.md — Garbage Collection Days

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/garbage-days/garbage-days.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

8 columns, 5 rows.

8 of 8 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`WEEKDAY`** — *int16*  
Day of week as a number. Measured in the published file: Populated on 100% of 5 rows, 5 distinct values, ranging 1 to 5.

**`DAY_NAME`** — *string*  
Day of week as a name. Measured in the published file: Populated on 100% of 5 rows, 5 distinct values.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/garbage-days/garbage-days.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "DAY_NAME", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/garbage-days/garbage-days.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Tuesday` — 1
- `Friday` — 1
- `Wednesday` — 1
- `Thursday` — 1
- `Monday` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/GarbageDays/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/GarbageDays/MapServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
