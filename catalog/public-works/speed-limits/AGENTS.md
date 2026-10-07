# AGENTS.md — Speed Limits

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/speed-limits/speed-limits.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

50 columns, 5,072 rows.


**Where these meanings come from.** Road centrelines carrying the posted speed limit. The `L_`/`R_` prefixes mean the left and right side of the segment in its direction of digitising, which is how a centreline carries different values per side.

50 of 50 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`L_F_ADD`** — *double*  
fromleft. Measured in the published file: Populated on 100% of 5,072 rows, 1,839 distinct values, ranging 0 to 12231.

**`L_T_ADD`** — *double*  
toleft. Measured in the published file: Populated on 100% of 5,072 rows, 1,994 distinct values, ranging 0 to 12339.

**`R_F_ADD`** — *double*  
fromright. Measured in the published file: Populated on 100% of 5,072 rows, 1,816 distinct values, ranging 0 to 12230.

**`R_T_ADD`** — *double*  
toright. Measured in the published file: Populated on 100% of 5,072 rows, 2,070 distinct values, ranging 0 to 12338.

**`PRE_DIR`** — *string*  
One of. The source layer's domain allows: `N`, `E`, `W`, `S`.

**`S_NAME`** — *string*  
Street name of the segment.

**`S_TYPE`** — *string*  
One of. The source layer's domain allows: `ALY`, `AVE`, `BAY`, `BLVD`, `CIR`, `COL`, `CON`, `CT`, `CTR`, `CV`, and 26 more.

**`SUF_DIR`** — *string*  
One of. The source layer's domain allows: `N`, `E`, `W`, `S`.

**`ACS_ALIAS`** — *string*  
Address system alias for the street.

**`ACS_STREET`** — *string*  
Address system street name.

**`ACS_SUFDIR`** — *string*  
One of. The source layer's domain allows: `N`, `E`, `W`, `S`.

**`LABEL`** — *string*  
Short label used on the city's own maps. Measured in the published file: Populated on 100% of 5,072 rows, 1,414 distinct values.

**`L_CITYCD`** — *string*  
One of. The source layer's domain allows: `ALT`, `BLU`, `COP`, `COT`, `DRA`, `HER`, `HOL`, `INT`, `KEA`, `MAG`, and 11 more.

**`R_CITYCD`** — *string*  
One of. The source layer's domain allows: `ALT`, `BLU`, `COP`, `COT`, `DRA`, `HER`, `HOL`, `INT`, `KEA`, `MAG`, and 11 more.

**`LS_ZONE`** — *string*  
Speed zone on the left side.

**`FS_ZONE`** — *string*  
Speed zone on the right side.

**`LZIP`** — *string*  
ZIP code on the left side of the segment.

**`RZIP`** — *string*  
ZIP code on the right side.

**`ONE_WAY`** — *int32*  
One of. The source layer's domain allows: `0`, `1`, `2`.

**`SPEED_LIMIT`** — *int32*  
Posted speed limit, in miles per hour. 25 mph covers 4,064 of 5,072 segments.

**`COMMENTS`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`VECCOMMENTS`** — *string*  
Free-text note on the segment.

**`UNIQUE_ID`** — *int32*  
Identifier of the segment in the source road network.

**`EXCLUDE`** — *string*  
Flag marking a segment the city excludes from its own analyses.

**`S_DATE`** — *timestamp[ms]*  
Date the segment record was created.

**`M_DATE`** — *timestamp[ms]*  
Date the segment record was last modified.

**`SOURCE`** — *string*  
Where the record came from. Measured in the published file: Populated on 99% of 5,072 rows, 10 distinct values.

**`S_SURF`** — *int32*  
Surface type of the segment.

**`L_JURIS`** — *int32*  
Jurisdiction code on the left side.

**`R_JURIS`** — *int32*  
Jurisdiction code on the right side.

**`S_ROW`** — *int32*  
Right-of-way width.

**`S_ACCESS`** — *string*  
Access class of the segment.

**`S_USE`** — *string*  
Use class of the segment.

**`S_ACCUR`** — *int32*  
Positional accuracy class of the centreline.

**`CFCC`** — *string*  
Census Feature Class Code, the US Census classification of the road type, carried over from TIGER line data.

**`ALT_NAME`** — *string*  
Alternative name the street is also known by.

**`STREET`** — *string*  
Street the feature lies on. Measured in the published file: Populated on 100% of 5,072 rows, 1,624 distinct values.

**`LOW`** — *double*  
Lowest address number on the segment.

**`HIGH`** — *double*  
Highest address number on the segment.

**`MAINTENANCE`** — *string*  
Who maintains the segment. `SANPV` is Sandy, `SHARE` is shared, `SANG` is a further Sandy class.

**`FUNCTIONAL_CLASS`** — *string*  
Functional classification of the road.

**`CARTO_CODE`** — *string*  
Cartographic class controlling how the segment draws on the city's own maps.

**`DATA_DATE`** — *timestamp[ms]*  
Date of the data load this row came from.

**`DATA_EDITOR`** — *string*  
Editor of the data load.

**`RuleID`** — *int32*  
Esri symbology rule identifier. It selects a renderer class in the city's own map documents and carries no meaning about the feature itself.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`Shape.STLength()`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`RuleID`**

- `1` = All other values
- `2` = Freeways
- `3` = Major Roads
- `4` = Gravel;Private;Streets
- `5` = Ramps
- `6` = Do Not Display

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/speed-limits/speed-limits.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "SPEED_LIMIT", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-works/speed-limits/speed-limits.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `25` — 4,064
- `35` — 431
- `30` — 381
- `40` — 94
- `45` — 83
- `15` — 15
- `10` — 3
- `5` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Speed_Limits/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Speed_Limits/MapServer/1?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
