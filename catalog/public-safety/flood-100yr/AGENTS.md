# AGENTS.md — Approximate 100-Year Floodplain

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/flood-100yr/flood-100yr.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

25 columns, 828 rows.


**Where these meanings come from.** Flood hazard areas on FEMA's Digital Flood Insurance Rate Map schema, the database design behind the [National Flood Hazard Layer](https://www.fema.gov/flood-maps/national-flood-hazard-layer). The column names are FEMA's, not Sandy's.

25 of 25 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`DFIRM_ID`** — *string*  
Identifier of the Digital Flood Insurance Rate Map study this polygon belongs to.

**`VERSION_ID`** — *string*  
Version of the FEMA database schema the record follows.

**`FLD_AR_ID`** — *string*  
Identifier of the flood area polygon within the study.

**`STUDY_TYP`** — *string*  
Type of flood study the mapping rests on.

**`FLD_ZONE`** — *string*  
FEMA flood zone designation. Zone A and AE are the one-percent-annual-chance floodplain, commonly called the 100-year floodplain.

**`ZONE_SUBTY`** — *string*  
Zone subtype. `FLOODWAY` marks the channel plus the adjoining land that must stay clear to carry the one-percent flood without raising its level.

**`SFHA_TF`** — *string*  
Whether the polygon is a Special Flood Hazard Area. Federally backed mortgages on property here require flood insurance.

**`STATIC_BFE`** — *double*  
Base flood elevation, the height the one-percent flood is expected to reach, where a single value applies.

**`V_DATUM`** — *string*  
Vertical datum the elevation is measured against.

**`DEPTH`** — *double*  
Flood depth where the zone is mapped by depth rather than elevation.

**`LEN_UNIT`** — *string*  
Unit the elevation and depth values are in.

**`VELOCITY`** — *double*  
Flood velocity, where measured.

**`VEL_UNIT`** — *string*  
Unit the velocity is in.

**`AR_REVERT`** — *string*  
Zone the area reverts to if a flood control structure is restored, for a Zone AR area behind one under repair.

**`AR_SUBTRV`** — *string*  
Zone subtype the area reverts to.

**`BFE_REVERT`** — *double*  
Base flood elevation the area reverts to.

**`DEP_REVERT`** — *double*  
Depth the area reverts to.

**`DUAL_ZONE`** — *string*  
Whether the area carries two zone designations.

**`SOURCE_CIT`** — *string*  
Citation pointing to the study the mapping came from, within FEMA's own source table.

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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/flood-100yr/flood-100yr.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "ZONE_SUBTY", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/flood-100yr/flood-100yr.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- ` ` — 692
- `FLOODWAY` — 136

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Hazards/MapServer/5](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Hazards/MapServer/5?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
