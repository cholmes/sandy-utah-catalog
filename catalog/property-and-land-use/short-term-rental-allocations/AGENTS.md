# AGENTS.md — Short-Term Rental Allocations

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

11 columns, 30 rows.

7 of 11 columns carry a definition. The rest say so rather than guess.

**`Alloted_Status`** — *string*  
Open. Coded value. The source layer's domain allows: `Available STRs`, `FULL: Next application will be waitlisted.`, `Waitlist has been placed.`. Codes: `Open` = Available STRs, `Full` = FULL: Next application will be waitlisted., `Wait` = Waitlist has been placed..

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`COMMUNITY_ID`** — *double*  
Sandy community area number, joining to the `communities` collection. Measured in the published file: Populated on 100% of 30 rows, 30 distinct values, ranging 1 to 30.

**`COMMUNITY_NAME`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 30 distinct values.

**`Max_STR`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 15 distinct values, ranging 2 to 23.

**`Current_STR`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 13 distinct values, ranging 0 to 14.

**`Open_STR`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 15 distinct values, ranging -1 to 16.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Alloted_Status` — Open**

- `Open` = Available STRs
- `Full` = FULL: Next application will be waitlisted.
- `Wait` = Waitlist has been placed.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Open_STR", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `8` — 5
- `0` — 5
- `6` — 3
- `4` — 3
- `2` — 2
- `3` — 2
- `7` — 2
- `10` — 1
- `16` — 1
- `11` — 1
- `13` — 1
- `5` — 1

## Provenance

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
