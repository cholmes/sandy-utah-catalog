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

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `PMA` | string |
| `PWA` | string |
| `CityCouncil` | string |
| `Description` | string |
| `Width` | int16 |
| `ApproxSqFt` | int32 |
| `Miles` | double |
| `PubRightofWay` | string |
| `Jurisdiction` | string |
| `MaintainedBy` | string |
| `SideOfStreet` | string |
| `ApproxSections` | int16 |
| `OverallCondition` | double |
| `CrackedSections_1` | int16 |
| `CrackedSections_2` | int16 |
| `CrackedSections_3` | int16 |
| `CrackedSections_4` | int16 |
| `SpallingSections_1` | int16 |
| `SpallingSections_2` | int16 |
| `SpallingSections_3` | int16 |
| `SpallingSections_4` | int16 |
| `SunkSections_1` | int16 |
| `SunkSections_2` | int16 |
| `SunkSections_3` | int16 |
| `SunkSections_4` | int16 |
| `RaisedSections_1` | int16 |
| `RaisedSections_2` | int16 |
| `RaisedSections_3` | int16 |
| `RaisedSections_4` | int16 |
| `QualityRating` | double |
| `EstReplacementCost` | double |
| `Comments` | string |
| `Shape` | binary |
| `Shape.STLength()` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sidewalks/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Sidewalks/MapServer/0) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
