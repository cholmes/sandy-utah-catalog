# AGENTS.md — Address Points

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/address-points/address-points.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

37 columns, 60,400 rows.


**Where these meanings come from.** Addresses are assembled by Sandy City from utility billing, subdivision plats and parcel data, which is what the source service states in its own description.

20 of 37 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`Parcel_Id`** — *string*  
County parcel number, joining to `parcels.parcel_id`. 54,000 of 60,400 address points match a parcel.

**`Address`** — *string*  
Full address string. Joins to `lead-service-lines.address` after upper-casing and trimming; 22,597 of 26,213 service lines match.

**`HSNO`** — *int32*  
House number component of the address.

**`DIR`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 97% of 60,400 rows, 9 distinct values.

**`STREET`** — *string*  
Street the feature lies on. Measured in the published file: Populated on 100% of 60,400 rows, 2,703 distinct values.

**`SFX`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 79% of 60,400 rows, 32 distinct values.

**`STREET_DIR`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 21% of 60,400 rows, 13 distinct values.

**`APT`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 16% of 60,400 rows, 2,326 distinct values.

**`Municipality`** — *string*  
Municipality the feature falls in. Several Sandy layers extend into neighbouring cities, so this is how to select Sandy's own. Measured in the published file: Populated on 100% of 60,400 rows, 9 distinct values.

**`Zip`** — *string*  
Postal ZIP code. Measured in the published file: Populated on 100% of 60,400 rows, 13 distinct values.

**`Zip_Four`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 44% of 60,400 rows, 5,173 distinct values.

**`InSandy`** — *string*  
Whether the address is inside the Sandy city limit. The layer covers neighbouring municipalities too, so filter on this to get Sandy only: 38,854 of 60,400 rows are inside.

**`Prop_Type`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 60,400 rows, 11 distinct values.

**`Prop_Subtype`** — *string*  
Coded value. The source layer's domain allows: `Apartment`, `Condominium`, `Duplex`, `Mobile Home`, `Elderly Housing`, `Commercial`, `Educational`, `Medical`, `Religious`, `Government`, and 8 more. Codes: `Apartment` = Apartment, `Condominium` = Condominium, `Duplex` = Duplex, `Mobile Home` = Mobile Home, `Elderly Housing` = Elderly Housing, `Commercial` = Commercial, `Educational` = Educational, `Medical` = Medical, `Religious` = Religious, `Government` = Government, `Land` = Land, `Townhome` = Townhome.

**`IsRental`** — *string*  
Whether the property is registered as a rental. Carries both Yes/No and 1/0 forms, so normalise before grouping.

**`Building_Units`** — *int16*  
Number of dwelling units at the address.

**`Complex_Name`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 39% of 60,400 rows, 660 distinct values.

**`Alias_ID`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 93% of 60,400 rows, 56,179 distinct values, ranging 1 to 83281.

**`Alias_Street`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 77% of 60,400 rows, 1,573 distinct values.

**`Alias_Suffix_Dir`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 77% of 60,400 rows, 3 distinct values.

**`Updated_Date`** — *timestamp[ms]*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 60,400 rows, 389 distinct values.

**`Updated_By`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 60,400 rows, 13 distinct values.

**`Year_Built`** — *string*  
Year the feature was built. Measured in the published file: Populated on 100% of 60,400 rows, 154 distinct values.

**`Comment`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`Source`** — *string*  
Where the record came from. Measured in the published file: Populated on 100% of 60,400 rows, 70 distinct values.

**`Placement`** — *string*  
Coded value. The source layer's domain allows: `Placed Photo Verified`, `Placed Field Verified`, `Empty Parcel`, `Unplaced`, `Unplaced Examined`, `Duplicate`. Codes: `0` = Placed Photo Verified, `1` = Placed Field Verified, `2` = Empty Parcel, `3` = Unplaced, `4` = Unplaced Examined, `5` = Duplicate.

**`X_Coord`** — *double*  
X coordinate copied into an attribute. The geometry column is authoritative. Measured in the published file: Populated on 100% of 60,400 rows, 58,854 distinct values, ranging 1.50894e+06 to 1.56345e+06.

**`Y_Coord`** — *double*  
Y coordinate copied into an attribute. The geometry column is authoritative. Measured in the published file: Populated on 100% of 60,400 rows, 58,989 distinct values, ranging 7.33612e+06 to 7.39852e+06.

**`Addy_ID`** — *int32*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 60,400 rows, 60,391 distinct values, ranging 1 to 66640.

**`Addy_ID_Text`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 100% of 60,400 rows, 60,391 distinct values.

**`PPH_Approx`** — *double*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 99% of 60,400 rows, 1,049 distinct values, ranging 0 to 48.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`Municipality_Code`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 89% of 60,400 rows, 11 distinct values.

**`New_Municipality_Code`** — *string*  
Sandy City publishes no definition for this column, and the source layer declares no coded-value domain for it. Measured in the published file: Populated on 89% of 60,400 rows, 7 distinct values.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Prop_Subtype`**

- `Apartment` = Apartment
- `Condominium` = Condominium
- `Duplex` = Duplex
- `Mobile Home` = Mobile Home
- `Elderly Housing` = Elderly Housing
- `Commercial` = Commercial
- `Educational` = Educational
- `Medical` = Medical
- `Religious` = Religious
- `Government` = Government
- `Land` = Land
- `Townhome` = Townhome
- `Other` = Other
- `Single Family` = Single Family Housing
- `Parking Lot` = Parking Lot
- `Landscaped` = Landscaped

**`IsRental`**

- `0` = No
- `1` = Yes

**`Placement`**

- `0` = Placed Photo Verified
- `1` = Placed Field Verified
- `2` = Empty Parcel
- `3` = Unplaced
- `4` = Unplaced Examined
- `5` = Duplicate

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/address-points/address-points.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Address_Points/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Address_Points/MapServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
