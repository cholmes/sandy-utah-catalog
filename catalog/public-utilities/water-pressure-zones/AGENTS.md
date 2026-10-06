# AGENTS.md — Water Pressure Zones

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-pressure-zones/water-pressure-zones.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

17 columns, 17 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `PubUtils.PU.PressureZones.AREA` | double |
| `PERIMETER` | double |
| `PRESSUREZONES_` | int32 |
| `PRESSUREZONES_ID` | int32 |
| `ZONE_` | string |
| `ELEV_ZONE` | string |
| `SOURCES` | string |
| `created_user` | string |
| `created_date` | timestamp[ms] |
| `last_edited_user` | string |
| `last_edited_date` | timestamp[ms] |
| `ZONE_NAME` | string |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/water-pressure-zones/water-pressure-zones.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/46](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/WaterSystem/FeatureServer/46) on 2026-10-06T20:37:26Z.
Sandy City publishes no licence for this data; see the [README](README.md).
