# AGENTS.md — Communities

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/communities/communities.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

22 columns, 30 rows.


**Where these meanings come from.** Sandy's community areas, the units its community councils are organised around. Population and household counts are carried on the layer by the city.

15 of 22 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`COMMUNITY_ID`** — *double*  
Sandy community area number, joining to the `communities` collection. Measured in the published file: Populated on 100% of 30 rows, 30 distinct values, ranging 1 to 30.

**`COMMUNITY_NAME`** — *string*  
Name of the community area. Some rows carry a number rather than a name.

**`LEADER_NAME`** — *string*  
Community council chair. Contact details for this person were removed before publication; see the README.

**`Color`** — *string*  
Cartographic fill index used so that neighbouring areas differ on the city's own maps. It carries no meaning about the area.

**`EMERGENCY_PREPAREDNESS_LEADER`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 40% of 30 rows, 12 distinct values.

**`EMERGENCY_PREPAREDNESS_LEADER2`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 17% of 30 rows, 5 distinct values.

**`LINK`** — *string*  
Link to a page about this feature on a city or partner website.

**`Sandy_HH`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 30 distinct values, ranging 0 to 2497.

**`Unicorp_HH`** — *int16*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 18 distinct values, ranging 0 to 938.

**`Sandy_Pop`** — *double*  
Population within the Sandy city limit.

**`Unicorp_Pop`** — *double*  
Population in the unincorporated part of the community area.

**`Total_HH`** — *int16*  
Total households in the community area.

**`Total_Pop`** — *double*  
Total population of the community area. Ranges 661 to 7,084 across the 30 areas.

**`Date_Updated`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 30 rows, 1 distinct values.

**`Sandy_PPH`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 30 rows, 29 distinct values, ranging 2.06286 to 3.33391.

**`Unincorp_PPH`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 60% of 30 rows, 17 distinct values, ranging 2 to 4.

**`Total_PPH`** — *double*  
Average persons per household, derived by the city from the population and household counts.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/boundaries/communities/communities.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Sandy_Communities/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Sandy_Communities/MapServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
