# AGENTS.md — Voting Precincts

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/voting-precincts/voting-precincts.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

15 columns, 102 rows.

7 of 15 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Precinct`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 102 distinct values.

**`Congress`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 2 distinct values, ranging 3 to 4.

**`StateHouse`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 5 distinct values, ranging 39 to 45.

**`StateSenate`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 2 distinct values, ranging 15 to 19.

**`StateSchool`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 2 distinct values, ranging 7 to 9.

**`CountyCoun`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 1 distinct values.

**`LocalSchool`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 6 distinct values.

**`Municipality`** — *string*  
Municipality the feature falls in. Several Sandy layers extend into neighbouring cities, so this is how to select Sandy's own. Measured in the published file: Populated on 100% of 102 rows, 1 distinct values.

**`CityCouncil`** — *string*  
Sandy city council district the feature falls in. Measured in the published file: Populated on 100% of 102 rows, 4 distinct values.

**`Shape_Leng`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 102 rows, 102 distinct values, ranging 405.082 to 53903.7.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape__Length`** — *double*  
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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/voting-precincts/voting-precincts.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "CityCouncil", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/voting-precincts/voting-precincts.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Sandy 3` — 29
- `Sandy 2` — 27
- `Sandy 4` — 23
- `Sandy 1` — 23

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Voting_Precincts/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Voting_Precincts/FeatureServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
