# AGENTS.md — Fire Dispatch Subdistricts

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-subdistricts/fire-subdistricts.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

15 columns, 39 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `CITY` | string |
| `CITY_CODE` | string |
| `FireZoneID` | string |
| `Agency` | string |
| `ID` | int32 |
| `Stack_2_Deep` | string |
| `Stack_3_Deep` | string |
| `Stack_4_Deep` | string |
| `Stack_5_Deep` | string |
| `Shape` | binary |
| `Shape.STArea()` | double |
| `Shape.STLength()` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-subdistricts/fire-subdistricts.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "ID", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-subdistricts/fire-subdistricts.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `32` — 12
- `34` — 9
- `31` — 9
- `33` — 5
- `35` — 4

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Fire_Subdistricts/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Fire_Subdistricts/MapServer/1) on 2026-10-06T21:15:15Z.
Sandy City publishes no licence for this data; see the [README](README.md).
