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


**Where these meanings come from.** Burial register of the Sandy City Cemetery, which the city maintains as a public record. Cemetery registers are routinely published for genealogical use. Code lists below are the coded-value domains the source layer declares.

60 of 60 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Grave_ID`** — *int32*  
Identifier of the grave plot within the cemetery.

**`BurialID`** — *double*  
Identifier of the burial record.

**`Section`** — *string*  
Cemetery section the plot lies in.

**`Section_Lot`** — *string*  
Section and lot, concatenated.

**`Section_Lot_Grave`** — *string*  
Full plot address as section, lot and grave.

**`Status`** — *int16*  
Operational status of the feature. See the measured values below, because the source layer declares no code list. Measured in the published file: Populated on 100% of 11,695 rows, 6 distinct values, ranging 1 to 9.

**`Deceased`** — *string*  
Name of the person buried, as recorded in the register.

**`LastName`** — *string*  
Surname of the person buried.

**`FirstMidName`** — *string*  
Given and middle names of the person buried.

**`Death_Place`** — *string*  
Place of death, as recorded.

**`Race`** — *string*  
Race as written in the register. This is a historical record and reflects the categories and language of the time it was written, not current usage. Populated on 65% of rows.

**`Birthplace`** — *string*  
Place of birth, as recorded.

**`Father`** — *string*  
Father's name, as recorded.

**`Father_Nationality`** — *string*  
Father's nationality, as recorded.

**`Mother`** — *string*  
Mother's name, as recorded.

**`Mother_Nationality`** — *string*  
Mother's nationality, as recorded.

**`BIRTH_MO`** — *int16*  
Month of birth as a number. Zero where unrecorded.

**`BIRTH_DAY`** — *int16*  
Day of birth. Zero where unrecorded.

**`BIRTH_YEAR`** — *int16*  
Year of birth. Zero where the register does not record it; 4,889 of 11,695 rows carry a usable year, ranging 1800 to 2015.

**`BirthDate`** — *timestamp[ms]*  
Date of birth as a single value, where the register records a complete date.

**`DEATH_MO`** — *int16*  
Month of death as a number. Zero where unrecorded.

**`DEATH_DAY`** — *int16*  
Day of death. Zero where unrecorded.

**`DEATH_YEAR`** — *int16*  
Year of death. Zero where unrecorded.

**`DeathDate`** — *timestamp[ms]*  
Date of death as a single value.

**`BURIAL_MO`** — *int16*  
Month of burial as a number. Zero where unrecorded.

**`BURIAL_DAY`** — *int16*  
Day of burial. Zero where unrecorded.

**`BURIAL_YEAR`** — *int16*  
Year of burial. Zero where unrecorded.

**`BurialDate`** — *timestamp[ms]*  
Date of burial as a single value.

**`Burial_Receipt_Num`** — *string*  
Receipt number for the burial fee. Some values resemble telephone numbers; they are receipt numbers.

**`Burial_Amount_Paid`** — *double*  
Fee paid for the burial, in dollars.

**`Social_Status_old`** — *string*  
Earlier value of the status field, kept from a previous version of the register.

**`Social_Status`** — *int16*  
Marital or family status at death.

**`Gender`** — *string*  
Sex of the person buried, as recorded.

**`Cause_of_Death`** — *string*  
Cause of death, as written in the register.

**`Veteran`** — *int16*  
Veteran marker. 1 indicates a veteran burial, 0 indicates not, and -1 indicates the register does not say. Populated on 67% of rows.

**`Service`** — *string*  
Branch of military service, where the person served.

**`Rank`** — *string*  
Military rank, where recorded.

**`Unit`** — *string*  
Unit of the adjacent measurement column. Measured in the published file: Populated on 0% of 11,695 rows, 44 distinct values.

**`Conflict`** — *string*  
Conflict the person served in, where recorded.

**`EnteredBy`** — *string*  
Staff member who entered the record.

**`Last_Update`** — *timestamp[ms]*  
When the register row was last updated.

**`Comments`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`On_the_Headstone`** — *string*  
Inscription transcribed from the headstone.

**`Notes_Landmarks`** — *string*  
Note describing how to find the plot on the ground.

**`Mortuary`** — *string*  
Mortuary that handled the burial.

**`Mortuary_Phone`** — *string*  
Business telephone number of the mortuary.

**`Ownership`** — *string*  
Who owns the asset. Sandy's utility layers include assets owned by other cities, the county, UDOT and private parties. Empty in all 11,695 rows of the published file.

**`CremationFlag`** — *int16*  
Whether the interment is a cremation.

**`Spouse`** — *string*  
Spouse's name, as recorded.

**`LocatedBy`** — *string*  
Staff member who located the plot on the ground.

**`VerifiedBy`** — *string*  
Staff member who verified the record.

**`Headstone_Mon_Placed_YN`** — *int16*  
Whether a headstone or monument has been placed on the plot.

**`Headstone_Mon_Placed_Date`** — *timestamp[ms]*  
Date the headstone or monument was placed.

**`Monument_Co`** — *string*  
Company that supplied the headstone or monument.

**`Monument_Co_Phone`** — *string*  
Business telephone number of that company.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Sandy_Cemetery/FeatureServer/37](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Sandy_Cemetery/FeatureServer/37?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
