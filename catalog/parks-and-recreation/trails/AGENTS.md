# AGENTS.md — Trails

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/trails/trails.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

58 columns, 1,127 rows.


**Where these meanings come from.** Trail centrelines. The schema follows the recreational-trails model used across Utah datasets: a set of yes/no flags for the activities a trail permits, alongside the surface, difficulty and managing agency. `LWCFProt` refers to the [Land and Water Conservation Fund](https://www.nps.gov/subjects/lwcf/index.htm), whose Section 6(f) restriction prevents converting the land to another use.

57 of 58 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Name`** — *string*  
Name of the feature. Measured in the published file: Populated on 93% of 1,127 rows, 182 distinct values.

**`USAGE_`** — *string*  
Permitted use summary for the segment.

**`TrailID`** — *int32*  
Identifier of the trail segment.

**`SystemName`** — *string*  
Name of the trail system the segment belongs to.

**`SharedName`** — *string*  
Alternative name the segment is also known by.

**`SystemType`** — *string*  
Type of trail system.

**`ParkID`** — *string*  
Identifier of the park the feature belongs to, joining to the parks collection. Measured in the published file: Populated on 38% of 1,127 rows, 48 distinct values.

**`Park_ID`** — *double*  
Numeric identifier of the park the feature belongs to. Measured in the published file: Populated on 38% of 1,127 rows, 48 distinct values, ranging 2 to 70.

**`CityMuni`** — *string*  
Municipality the segment runs through. The layer extends beyond Sandy, so filter on this for Sandy's own trails: 788 of 1,127 segments.

**`County`** — *string*  
County the feature falls in. Sandy is in Salt Lake County. Measured in the published file: Populated on 100% of 1,127 rows, 2 distinct values.

**`State`** — *string*  
State the feature falls in. Measured in the published file: Populated on 100% of 1,127 rows, 1 distinct values.

**`Status`** — *string*  
Whether the segment is open, planned or proposed. Only the 920 open segments exist on the ground.

**`YearOpen`** — *int32*  
Year the segment opened.

**`Trails_JAKE_Temp_Length`** — *double*  
Length. Measured in the published file: Populated on 100% of 1,127 rows, 1,109 distinct values, ranging 4.96972 to 40097.9.

**`L_Units`** — *string*  
Unit the length value is in.

**`L_Source`** — *string*  
Where the length measurement came from.

**`TrlSurface`** — *string*  
Tread surface of the trail, such as hard surface or native material.

**`Width`** — *int32*  
Trail width, in the units given by `W_Units`.

**`W_Units`** — *string*  
Unit the `Width` value is in.

**`Rating`** — *string*  
Difficulty rating of the segment.

**`DesignUse`** — *string*  
Use the trail was designed and is managed for, which is narrower than the set of uses it permits.

**`UseComment`** — *string*  
Note qualifying the permitted uses.

**`Accessible`** — *string*  
Accessibility status of the segment.

**`Motorized`** — *string*  
Whether motorised use is permitted.

**`Hike`** — *string*  
Whether hiking is permitted.

**`RoadBike`** — *string*  
Whether road cycling is permitted.

**`MtnBike`** — *string*  
Whether mountain biking is permitted.

**`Equestrian`** — *string*  
Whether horse riding is permitted.

**`DogSled`** — *string*  
Whether dog sledding is permitted.

**`Snowmobile`** — *string*  
Whether snowmobiles are permitted.

**`Snowshoe`** — *string*  
Whether snowshoeing is permitted.

**`XCntrySki`** — *string*  
Whether cross-country skiing is permitted.

**`WCraft_Mtr`** — *string*  
Whether motorised watercraft are permitted, for a water trail.

**`WCraft_Non`** — *string*  
Whether non-motorised watercraft are permitted.

**`Portage`** — *string*  
Whether the segment is a portage between waterways.

**`ATV`** — *string*  
Whether all-terrain vehicles are permitted.

**`FourWD`** — *string*  
Whether four-wheel-drive vehicles are permitted.

**`Motorcycle`** — *string*  
Whether motorcycles are permitted.

**`ParkTrail`** — *string*  
Whether the segment lies within a park.

**`OnStreetBike`** — *string*  
Whether the segment is an on-street bicycle route.

**`AgencyName`** — *string*  
Organisation that manages the segment.

**`AgencyType`** — *string*  
Type of managing organisation, such as municipal or special district.

**`AcqSource`** — *string*  
Funding source the land was acquired with.

**`AcqMethod`** — *string*  
How the land was acquired, such as fee simple or easement.

**`AcqComment`** — *string*  
Note on the acquisition.

**`LWCFProt`** — *string*  
Whether the segment is protected by the Land and Water Conservation Fund, which restricts converting the land to another use.

**`OtherProt`** — *string*  
Other protection that applies to the land.

**`ResPrtCmnt`** — *string*  
Note on restrictions or protections.

**`EditDate`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`AssetID`** — *string*  
Identifier of the asset in the city's maintenance management system. Measured in the published file: Populated on 100% of 1,127 rows, 1,089 distinct values.

**`Address`** — *string*  
Street address of the feature. Measured in the published file: Populated on 70% of 1,127 rows, 137 distinct values.

**`Location`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 70% of 1,127 rows, 137 distinct values.

**`Shape_Length_1`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 0% of 1,127 rows, 2 distinct values, ranging 3951.35 to 10059.5.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/trails/trails.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Trails/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Trails/MapServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
