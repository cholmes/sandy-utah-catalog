# AGENTS.md — Water Service Line Material Inventory

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:2850** (NAD83(HARN) / Utah Central). Linear units are **metres**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:2850', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/lead-service-lines/lead-service-lines.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:2850 too.

## Schema

47 columns, 26,213 rows.

| column | type |
| --- | --- |
| `address` | string |
| `location` | string |
| `sensitivepop` | string |
| `disadvantaged` | string |
| `utilassetid` | string |
| `utilmaterial` | string |
| `everlead` | string |
| `utilinstalldate` | timestamp[ms] |
| `utildiameter` | double |
| `utilsource` | string |
| `utilverified` | string |
| `utilverifmethod` | string |
| `utilverifdate` | timestamp[ms] |
| `utilstatus` | int16 |
| `utilnotes` | string |
| `custassetid` | string |
| `custmaterial` | string |
| `custinstalldate` | timestamp[ms] |
| `custdiameter` | double |
| `custsource` | string |
| `custverified` | string |
| `custverifmethod` | string |
| `custverifdate` | timestamp[ms] |
| `custstatus` | int16 |
| `custnotes` | string |
| `bothsidesstatus` | string |
| `leadconnector` | string |
| `leadsolder` | string |
| `otherfittings` | string |
| `buildingtype` | string |
| `pointofentry` | string |
| `copperwithlead` | string |
| `samplingsite` | string |
| `replacestatus` | string |
| `scheddate` | timestamp[ms] |
| `utilreplacedate` | timestamp[ms] |
| `custscheddate` | timestamp[ms] |
| `custreplacedate` | timestamp[ms] |
| `replacereason` | string |
| `custnotified` | string |
| `notifydate` | timestamp[ms] |
| `yearstructbuilt` | int16 |
| `CreationDate` | timestamp[ms] |
| `EditDate` | timestamp[ms] |
| `OBJECTID` | int64 |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`sensitivepop` — Sensitive Population**

- `Yes - School` = Yes - School
- `Yes - Day Care` = Yes - Day Care
- `Yes - Other` = Yes - Other
- `No` = No

**`disadvantaged` — Disadvantaged Neighborhood**

- `Yes` = Yes
- `No` = No
- `Unknown` = Unknown

**`utilmaterial` — Utility Material**

- `Unknown - Material Unknown` = Unknown - Material Unknown
- `Unknown - Likely Lead` = Unknown - Likely Lead
- `Unknown - Unlikely Lead` = Unknown - Unlikely Lead
- `Non-Lead - Other` = Non-Lead - Other
- `Non-Lead - Copper` = Non-Lead - Copper
- `Non-Lead - Plastic` = Non-Lead - Plastic
- `Galvanized` = Galvanized
- `Lead` = Lead
- `Lead-lined galvanized` = Lead-lined galvanized

**`everlead` — Ever Lead?**

- `Yes` = Yes
- `No` = No
- `Unknown` = Unknown

**`utildiameter` — Utility Diameter**

- `0` = Unknown
- `0.5` = 1/2"
- `0.625` = 5/8"
- `0.75` = 3/4"
- `1` = 1"
- `1.25` = 1 1/4"
- `1.5` = 1 1/2"
- `2` = 2"
- `2.25` = 2 1/4"
- `2.5` = 2 1/2"
- `3` = 3"
- `4` = 4"
- `4.5` = 4 1/2"
- `5.25` = 5 1/4"
- `6` = 6"
- `8` = 8"

**`utilsource` — Utility Source**

- `Installation record (e.g., tap card)` = Installation record (e.g., tap card)
- `Water sampling only with no records` = Water sampling only with no records
- `Field inspection only with no records` = Field inspection only with no records
- `Statistical analysis` = Statistical analysis
- `Previous materials evaluation` = Previous materials evaluation
- `Installation date is after the lead ban` = Installation date is after the lead ban
- `Service line diameter is greater than 2 inches` = Service line diameter is greater than 2 inches
- `Service line repair or replacement record` = Service line repair or replacement record
- `Other` = Other

**`utilverified` — Utility Side Verified**

- `Yes` = Yes
- `No` = No
- `Unknown` = Unknown

**`utilverifmethod` — Utility Verification Method**

- `Visual inspection at meter pit` = Visual inspection at meter pit
- `Customer self-identification` = Customer self-identification
- `CCTV Inspection at Curb Box - Internal` = CCTV Inspection at Curb Box - Internal
- `CCTV inspection at Curb Box - External` = CCTV inspection at Curb Box - External
- `Water Quality Sampling - Targeted` = Water Quality Sampling - Targeted
- `Water Quality Sampling - Flushed` = Water Quality Sampling - Flushed
- `Water Quality Sampling - Sequential` = Water Quality Sampling - Sequential
- `Water Quality Sampling - Other` = Water Quality Sampling - Other
- `Mechanical Excavation at 1 location` = Mechanical Excavation at 1 location
- `Mechanical Excavation at multiple locations` = Mechanical Excavation at multiple locations

**`utilstatus` — Utility Status**

- `0` = Unknown
- `1` = Lead
- `2` = Non-Lead
- `3` = Galvanized Requiring Replacement

**`custmaterial` — Customer Material**

- `Unknown - Material Unknown` = Unknown - Material Unknown
- `Unknown - Likely Lead` = Unknown - Likely Lead
- `Unknown - Unlikely Lead` = Unknown - Unlikely Lead
- `Non-Lead - Other` = Non-Lead - Other
- `Non-Lead - Copper` = Non-Lead - Copper
- `Non-Lead - Plastic` = Non-Lead - Plastic
- `Galvanized` = Galvanized
- `Lead` = Lead
- `Lead-lined galvanized` = Lead-lined galvanized

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/lead-service-lines/lead-service-lines.parquet' LIMIT 5;
```

Count by the column the default style uses:

```sql
SELECT "utilmaterial", count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/lead-service-lines/lead-service-lines.parquet'
GROUP BY 1 ORDER BY n DESC;
```

Measured on the published file:

- `Unknown - Material Unknown` — 19,070
- `Unknown - Unlikely Lead` — 6,415
- `Non-Lead - Copper` — 695
- `Galvanized` — 20
- `Non-Lead - Plastic` — 7
- `Non-Lead - Other` — 2

## Provenance

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/ServiceLine_viewing_7fe7c6729fd949afb34452df1ba78945/FeatureServer/0](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/ServiceLine_viewing_7fe7c6729fd949afb34452df1ba78945/FeatureServer/0) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
