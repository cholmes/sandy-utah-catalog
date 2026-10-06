# AGENTS.md — Sandy City Cemetery Graves

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/cemetery-graves/cemetery-graves.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

60 columns, 11,695 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Grave_ID` | int32 |
| `BurialID` | double |
| `Section` | string |
| `Section_Lot` | string |
| `Section_Lot_Grave` | string |
| `Status` | int16 |
| `Deceased` | string |
| `LastName` | string |
| `FirstMidName` | string |
| `Death_Place` | string |
| `Race` | string |
| `Birthplace` | string |
| `Father` | string |
| `Father_Nationality` | string |
| `Mother` | string |
| `Mother_Nationality` | string |
| `BIRTH_MO` | int16 |
| `BIRTH_DAY` | int16 |
| `BIRTH_YEAR` | int16 |
| `BirthDate` | timestamp[ms] |
| `DEATH_MO` | int16 |
| `DEATH_DAY` | int16 |
| `DEATH_YEAR` | int16 |
| `DeathDate` | timestamp[ms] |
| `BURIAL_MO` | int16 |
| `BURIAL_DAY` | int16 |
| `BURIAL_YEAR` | int16 |
| `BurialDate` | timestamp[ms] |
| `Burial_Receipt_Num` | string |
| `Burial_Amount_Paid` | double |
| `Social_Status_old` | string |
| `Social_Status` | int16 |
| `Gender` | string |
| `Cause_of_Death` | string |
| `Veteran` | int16 |
| `Service` | string |
| `Rank` | string |
| `Unit` | string |
| `Conflict` | string |
| `EnteredBy` | string |
| `Last_Update` | timestamp[ms] |
| `Comments` | string |
| `On_the_Headstone` | string |
| `Notes_Landmarks` | string |
| `Mortuary` | string |
| `Mortuary_Phone` | string |
| `Ownership` | string |
| `CremationFlag` | int16 |
| `Spouse` | string |
| `LocatedBy` | string |
| `VerifiedBy` | string |
| `Headstone_Mon_Placed_YN` | int16 |
| `Headstone_Mon_Placed_Date` | timestamp[ms] |
| `Monument_Co` | string |
| `Monument_Co_Phone` | string |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Status`**

- `1` = Available
- `2` = Sold
- `3` = Occupied
- `4` = Future
- `9` = Landscaping
- `8` = Obstructed
- `7` = Unknown-Fix

**`Social_Status`**

- `2` = Married
- `3` = Widow/Widower
- `4` = Divorced
- `5` = Child
- `6` = Infant
- `1` = Single
- `9` = Unknown

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/cemetery-graves/cemetery-graves.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "Status", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/cemetery-graves/cemetery-graves.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `3` — 6,159
- `1` — 2,903
- `2` — 2,204
- `9` — 299
- `8` — 116
- `7` — 9

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Sandy_Cemetery/FeatureServer/37](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Sandy_Cemetery/FeatureServer/37) on 2026-10-06T20:51:07Z.
Sandy City publishes no licence for this data; see the [README](README.md).
