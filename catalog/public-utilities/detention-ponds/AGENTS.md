# AGENTS.md — Storm Detention Ponds

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/detention-ponds/detention-ponds.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

23 columns, 210 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `NAME` | string |
| `ADDRESS` | string |
| `Shape__Area` | double |
| `FACILITYID` | string |
| `OWNERSHIP` | string |
| `MaintRating` | string |
| `FrameGrate` | string |
| `StructCond` | string |
| `FloorBench` | string |
| `InspDate` | timestamp[ms] |
| `MaintSched` | string |
| `DamGopher` | string |
| `DamSinkHoles` | string |
| `SpillwayGopher` | string |
| `SpillwaySinkHoles` | string |
| `TYPE` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`MaintSched`**

- `Annually` = Annually
- `Quarterly` = Quarterly
- `Monthly` = Monthly
- `Other` = Other
- `5 Years` = 5 Years

**`TYPE` — Detention or Retention**

- `Detention` = Detention
- `Retention` = Retentioun
- `Underground Detention` = Underground Detention
- `Underground Retention` = Underground Retention

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/detention-ponds/detention-ponds.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/7](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/StormDrain/FeatureServer/7) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
