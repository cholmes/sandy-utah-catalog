# AGENTS.md — Short-Term Rental Allocations

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

11 columns, 30 rows.

| column | type |
| --- | --- |
| `Alloted_Status` | string |
| `OBJECTID` | int64 |
| `COMMUNITY_ID` | double |
| `COMMUNITY_NAME` | string |
| `Max_STR` | int16 |
| `Current_STR` | int16 |
| `Open_STR` | int16 |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Alloted_Status` — Open**

- `Open` = Available STRs
- `Full` = FULL: Next application will be waitlisted.
- `Wait` = Waitlist has been placed.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Open_STR", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `8` — 5
- `0` — 5
- `6` — 3
- `4` — 3
- `2` — 2
- `3` — 2
- `7` — 2
- `10` — 1
- `16` — 1
- `11` — 1
- `13` — 1
- `5` — 1

## Provenance

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2) on 2026-10-06T20:37:26Z.
Sandy City publishes no licence for this data; see the [README](README.md).
