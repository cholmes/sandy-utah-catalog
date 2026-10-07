# AGENTS.md — Sidewalks

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/sidewalks/sidewalks.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

37 columns, 8,586 rows.


**Where these meanings come from.** Sidewalk inventory with a condition survey. The `_1` to `_4` suffixed columns count sections at each severity level for that defect, so a higher suffix is a worse defect.

21 of 37 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`PMA`** — *string*  
Pavement management area the segment belongs to.

**`PWA`** — *string*  
Public works area the segment belongs to.

**`CityCouncil`** — *string*  
Sandy city council district the feature falls in. Measured in the published file: Populated on 100% of 8,586 rows, 4 distinct values.

**`Description`** — *string*  
Description of the feature, entered by city staff. Measured in the published file: Populated on 100% of 8,586 rows, 5 distinct values.

**`Width`** — *int16*  
Sidewalk width, in feet.

**`ApproxSqFt`** — *int32*  
Approximate surface area, in square feet.

**`Miles`** — *double*  
Segment length, in miles.

**`PubRightofWay`** — *string*  
Whether the sidewalk sits in the public right of way.

**`Jurisdiction`** — *string*  
Jurisdiction the sidewalk falls in.

**`MaintainedBy`** — *string*  
Who maintains the sidewalk.

**`SideOfStreet`** — *string*  
Which side of the street the segment runs along.

**`ApproxSections`** — *int16*  
Approximate number of concrete sections in the segment.

**`OverallCondition`** — *double*  
Overall condition assigned at the last survey.

**`CrackedSections_1`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`CrackedSections_2`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`CrackedSections_3`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`CrackedSections_4`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SpallingSections_1`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SpallingSections_2`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SpallingSections_3`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SpallingSections_4`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SunkSections_1`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SunkSections_2`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SunkSections_3`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`SunkSections_4`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`RaisedSections_1`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`RaisedSections_2`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`RaisedSections_3`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`RaisedSections_4`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 8,586 rows, 1 distinct values.

**`QualityRating`** — *double*  
Quality rating derived from the defect counts.

**`EstReplacementCost`** — *double*  
Estimated replacement cost, in dollars.

**`Comments`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/sidewalks/sidewalks.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Description", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/sidewalks/sidewalks.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `4' Sidewalk` — 6,073
- `5' Sidewalk` — 1,149
- `No Sidewalk` — 795
- `Wider than 5' Sidewalk` — 557
- `Asphalt Path` — 12

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sidewalks/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sidewalks/MapServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
