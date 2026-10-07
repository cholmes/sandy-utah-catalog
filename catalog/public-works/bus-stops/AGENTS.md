# AGENTS.md — UTA Bus Stops

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/bus-stops/bus-stops.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

12 columns, 3,195 rows.

12 of 12 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`stopabbr_j`** — *string*  
Abbreviated stop name used by the transit operator. Measured in the published file: Populated on 100% of 3,195 rows, 3,194 distinct values.

**`uta_stopid`** — *int32*  
Utah Transit Authority stop identifier. UTA is the regional transit operator; this is their key, not Sandy's. Measured in the published file: Populated on 100% of 3,195 rows, 3,187 distinct values, ranging 0 to 198709.

**`avgboard`** — *int32*  
Average daily boardings recorded at the stop. Measured in the published file: Populated on 87% of 3,195 rows, 111 distinct values, ranging 0 to 406.

**`avgalight`** — *int32*  
Average daily alightings, meaning passengers getting off, recorded at the stop. Measured in the published file: Populated on 87% of 3,195 rows, 106 distinct values, ranging 0 to 384.

**`route`** — *string*  
Routes Served. Measured in the published file: Populated on 100% of 3,195 rows, 171 distinct values.

**`mode`** — *string*  
Transit mode served at this stop. Measured in the published file: Populated on 100% of 3,195 rows, 3 distinct values.

**`county`** — *string*  
County the feature falls in. Sandy is in Salt Lake County. Measured in the published file: Populated on 100% of 3,195 rows, 1 distinct values.

**`city`** — *string*  
City the feature falls in. Measured in the published file: Populated on 100% of 3,195 rows, 23 distinct values.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/bus-stops/bus-stops.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/UTA_Routes/MapServer/2](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/UTA_Routes/MapServer/2?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
