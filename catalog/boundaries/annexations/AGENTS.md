# AGENTS.md — Annexations

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566**, NAD83/HARN Utah Central, in **US survey feet**. `ST_Length` and `ST_Area` return feet and square feet, not metres. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/boundaries/annexations/annexations.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

19 columns, 521 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Year` | double |
| `Name` | string |
| `Type` | string |
| `Governing_Jurisdiction` | string |
| `Old_Jurisdiction` | string |
| `Effective_Date` | timestamp[ms] |
| `Acres` | double |
| `SLCO_Map_Record_Numb` | string |
| `SLCO_Map_Book_Page` | string |
| `SLCO_Ord_Record_Numb` | string |
| `SLCO_Ord_Book_Page` | string |
| `Shape` | binary |
| `Eff_Date_Notes` | string |
| `Sandy_Ord_Num` | string |
| `Shape.area` | double |
| `Shape.len` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/boundaries/annexations/annexations.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Type", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/boundaries/annexations/annexations.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Annexation` — 516
- `Boundary Adjustment` — 3
- `Incorporation` — 1
- `Correction` — 1

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Annexations/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Annexations/MapServer/0) on 2026-10-06T19:01:44Z.
Sandy City publishes no licence for this data; see the [README](README.md).
