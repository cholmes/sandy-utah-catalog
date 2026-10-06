# AGENTS.md — Sandy Water Wells

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/wells/wells.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

33 columns, 24 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `SYSNUM` | int32 |
| `SORNUM` | int16 |
| `EPAID` | string |
| `SOWN` | string |
| `SNAM` | string |
| `GPM3` | int32 |
| `STYP` | string |
| `DIAM` | int16 |
| `CODE` | int16 |
| `LABEL` | string |
| `STATE_ID` | string |
| `DESCR` | string |
| `OLD_LABEL` | string |
| `NEW_LABEL` | string |
| `UHDID` | string |
| `GREG_` | double |
| `GREG_ID` | double |
| `HDDWS_ALL_` | double |
| `HDDWS_ALL1` | double |
| `COMMENT` | string |
| `CH2MGRID_` | double |
| `CH2MGRID_I` | double |
| `CH2MCELL` | int32 |
| `CH2MROW` | int16 |
| `CH2MCOL` | int16 |
| `CH2MAREA` | double |
| `OWNER` | int32 |
| `Q_` | string |
| `Q_COMMENT` | string |
| `TC_COMMENT` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/wells/wells.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SourceProtectionWells/FeatureServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Utils/SourceProtectionWells/FeatureServer/1) on 2026-10-06T20:20:34Z.
Sandy City publishes no licence for this data; see the [README](README.md).
