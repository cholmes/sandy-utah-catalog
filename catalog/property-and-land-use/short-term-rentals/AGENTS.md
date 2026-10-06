# AGENTS.md — Short-Term Rentals

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566**, NAD83/HARN Utah Central, in **US survey feet**. `ST_Length` and `ST_Area` return feet and square feet, not metres. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/short-term-rentals/short-term-rentals.parquet';
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
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/short-term-rentals/short-term-rentals.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2) on 2026-10-06T19:01:44Z.
Sandy City publishes no licence for this data; see the [README](README.md).
