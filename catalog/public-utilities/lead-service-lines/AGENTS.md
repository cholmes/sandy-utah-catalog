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


**Where these meanings come from.** Field meanings follow the US EPA Lead and Copper Rule Revisions service line inventory, [40 CFR 141.84](https://www.ecfr.gov/current/title-40/section-141.84), as implemented by the Esri Lead Service Line Inventory solution. The rule's four material classifications are lead, galvanized requiring replacement, non-lead and unknown, which is exactly the domain this layer declares. See also EPA's [guidance on developing a service line inventory](https://www.epa.gov/ground-water-and-drinking-water/planning-and-developing-service-line-inventory).

47 of 47 columns carry a definition. The rest say so rather than guess.

**`address`** — *string*  
Street address of the service line. The rule requires the publicly accessible inventory to identify each service line by street address, or by another locational identifier where no address exists.

**`location`** — *string*  
Street address or place description of the feature. Measured in the published file: Populated on 100% of 26,213 rows, 26,135 distinct values.

**`sensitivepop`** — *string*  
Whether the service line serves a sensitive population, such as a school or a child care facility. EPA directs systems to prioritise these for replacement.

**`disadvantaged`** — *string*  
Whether the service line is in a neighbourhood the system has identified as disadvantaged, which affects prioritisation and funding eligibility.

**`utilassetid`** — *string*  
Utility Asset ID. Measured in the published file: Populated on 100% of 26,213 rows, 26,120 distinct values.

**`utilmaterial`** — *string*  
Material of the **utility-owned** portion of the service line, from the main to the property line.

**`everlead`** — *string*  
Whether the service line is known to have ever been lead, including a line since replaced.

**`utilinstalldate`** — *timestamp[ms]*  
Installation date of the utility-owned portion. A date after the local lead ban is itself accepted evidence of a non-lead line.

**`utildiameter`** — *double*  
Diameter of the utility-owned portion. A line over two inches is accepted evidence of a non-lead line.

**`utilsource`** — *string*  
Evidence the classification of the utility-owned portion rests on. The rule requires non-lead to rest on an evidence-based record, method or technique.

**`utilverified`** — *string*  
Whether the utility-owned material was verified rather than inferred.

**`utilverifmethod`** — *string*  
How the utility-owned material was verified.

**`utilverifdate`** — *timestamp[ms]*  
Utility Verification Date. Measured in the published file: Populated on 2% of 26,213 rows, 130 distinct values.

**`utilstatus`** — *int16*  
Classification of the utility-owned portion into the rule's four categories.

**`utilnotes`** — *string*  
Utility Side Notes. Measured in the published file: Populated on 2% of 26,213 rows, 107 distinct values.

**`custassetid`** — *string*  
Customer Asset ID. Measured in the published file: Populated on 0% of 26,213 rows, 1 distinct values.

**`custmaterial`** — *string*  
Material of the **customer-owned** portion of the service line, from the property line to the building. The rule requires both portions to be inventoried even where the system owns neither.

**`custinstalldate`** — *timestamp[ms]*  
Installation date of the customer-owned portion.

**`custdiameter`** — *double*  
Diameter of the customer-owned portion.

**`custsource`** — *string*  
Evidence the classification of the customer-owned portion rests on.

**`custverified`** — *string*  
Whether the customer-owned material was verified rather than inferred.

**`custverifmethod`** — *string*  
How the customer-owned material was verified.

**`custverifdate`** — *timestamp[ms]*  
Customer Verification Date. Measured in the published file: Populated on 4% of 26,213 rows, 362 distinct values.

**`custstatus`** — *int16*  
Classification of the customer-owned portion into the rule's four categories.

**`custnotes`** — *string*  
Customer Side Notes. Measured in the published file: Populated on 0% of 26,213 rows, 93 distinct values.

**`bothsidesstatus`** — *string*  
Classification of the service line as a whole. This is the field that determines replacement obligation.

**`leadconnector`** — *string*  
Whether a lead connector, also called a gooseneck or pigtail, is present. EPA defines a connector as a bendable segment of three feet or less; a documented lead segment longer than that is treated as a lead service line.

**`leadsolder`** — *string*  
Whether lead solder is known to be present at the connection.

**`otherfittings`** — *string*  
Other Fittings Containing Lead. Empty in all 26,213 rows of the published file.

**`buildingtype`** — *string*  
Type of building the service line serves.

**`pointofentry`** — *string*  
Whether a point-of-entry treatment device is installed.

**`copperwithlead`** — *string*  
Whether the line is copper with lead solder, which is not a lead service line but is a lead source.

**`samplingsite`** — *string*  
Whether this location is used as a tap sampling site for compliance monitoring.

**`replacestatus`** — *string*  
Where the line stands in the replacement programme.

**`scheddate`** — *timestamp[ms]*  
Utility Side Scheduled Replacement Date. Empty in all 26,213 rows of the published file.

**`utilreplacedate`** — *timestamp[ms]*  
Date the utility-owned portion was replaced.

**`custscheddate`** — *timestamp[ms]*  
Customer Side Scheduled Replacement Date. Empty in all 26,213 rows of the published file.

**`custreplacedate`** — *timestamp[ms]*  
Customer Side Replacement Date. Empty in all 26,213 rows of the published file.

**`replacereason`** — *string*  
Why the line is scheduled for replacement.

**`custnotified`** — *string*  
Whether the customer has been notified, which the rule requires for a lead, galvanized-requiring-replacement or unknown line.

**`notifydate`** — *timestamp[ms]*  
Notification Date. Empty in all 26,213 rows of the published file.

**`yearstructbuilt`** — *int16*  
Year the building was constructed. Used as evidence where no installation record survives.

**`CreationDate`** — *timestamp[ms]*  
Timestamp when the row was created, from the geodatabase editor tracking. It records the database edit, not when the feature was built in the world.

**`EditDate`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

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

**`utilstatus` — Utility Status**

- `0` = Unknown
- `1` = Lead
- `2` = Non-Lead
- `3` = Galvanized Requiring Replacement

**`custdiameter` — Customer Diameter**

- `0` = Unknown
- `0.5` = 1/2"
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
- `10` = 10"

**`custstatus` — Customer Status**

- `0` = Unknown
- `1` = Lead
- `2` = Non-Lead
- `3` = Galvanized Requiring Replacement

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

Mirrored from [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/ServiceLine_viewing_7fe7c6729fd949afb34452df1ba78945/FeatureServer/0](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/ServiceLine_viewing_7fe7c6729fd949afb34452df1ba78945/FeatureServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
