# AGENTS.md — Parcels

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/parcels/parcels.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

84 columns, 106,087 rows.


**Where these meanings come from.** Parcels are produced by the [Salt Lake County Recorder](https://slco.org/recorder/) and mirrored by Sandy City. The county publishes no field dictionary with the layer, so the descriptions below cover only columns whose meaning is unambiguous from the assessment roll they come from. The service states the extract is current to July 2022.

84 of 84 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`RECORDER_DATA_AS_OF`** — *string*  
Date the recorder's ownership data in this row was current.

**`parcel_id`** — *string*  
County parcel identification number. Unique across the 106,087 rows here, and the key that joins to `address-points.Parcel_Id`. Note the capitalisation differs between the two collections.

**`parent_parcel`** — *string*  
Parcel this one was split from, where it is a subdivision of an earlier parcel.

**`num_old_prcls`** — *int32*  
Number of earlier parcels merged into this one.

**`source_doc`** — *string*  
Recorded document the current ownership derives from.

**`date_created`** — *string*  
Date the parcel was created in the recorder's system.

**`last_vesting`** — *int32*  
Reference to the document that last vested title.

**`parcel_acres`** — *double*  
Parcel area in acres as carried on the assessment roll.

**`own_name`** — *string*  
Owner of record. Property ownership is public record under the county recorder. This column is in the GeoParquet and deliberately not in the vector tiles.

**`multi_names`** — *int32*  
Count of owners of record, where title is held jointly.

**`tax_dist`** — *string*  
Tax district code. A district is the unique overlap of taxing entities that applies to the parcel.

**`care_of`** — *string*  
Care-of line on the owner's mailing address.

**`own_addr`** — *string*  
Owner's mailing address, which is often not the property address. Public record, GeoParquet only.

**`own_apt_num`** — *string*  
Apartment or unit number in the owner's mailing address.

**`own_citystate`** — *string*  
City and state of the owner's mailing address.

**`own_country_code`** — *string*  
Country of the owner's mailing address. Blank for most rows; `USA` where set explicitly.

**`own_zip`** — *string*  
ZIP code of the owner's mailing address.

**`own_zip_four`** — *string*  
ZIP+4 extension of the owner's mailing address.

**`prop_location`** — *string*  
Situs address of the parcel itself.

**`HouseNum`** — *string*  
House number of the property address.

**`PreDir`** — *string*  
Directional prefix of the street name, such as S or E. Measured in the published file: Populated on 99% of 106,087 rows, 3 distinct values.

**`StreetName`** — *string*  
Street name component of the address. Measured in the published file: Populated on 99% of 106,087 rows, 4,941 distinct values.

**`StreetType`** — *string*  
Street type component of the address, such as ST or AVE. Measured in the published file: Populated on 73% of 106,087 rows, 19 distinct values.

**`StreetDir`** — *string*  
Directional component of the property street name.

**`exempt_type`** — *string*  
Exemption class, where the parcel is exempt from property tax.

**`property_type`** — *string*  
Assessment property-type code.

**`Property_Type_Desc`** — *string*  
Full assessment property-type description. `Property_Type_Simple_Desc` is the grouped form.

**`Property_Type_Simple_Desc`** — *string*  
Grouped property type: Residential, Commercial, Condos, Land or Other.

**`Community`** — *string*  
Sandy community area number, joining to the `communities` collection. Populated on 35% of rows.

**`Quadrant`** — *string*  
Sandy addressing and policing quadrant. Measured in the published file: Populated on 31% of 106,087 rows, 4 distinct values.

**`CityCouncil`** — *string*  
Sandy city council district the feature falls in. Measured in the published file: Populated on 31% of 106,087 rows, 4 distinct values.

**`Abnormal`** — *string*  
Marker the assessor sets on a parcel that does not fit normal valuation, such as an odd shape or a split use.

**`Mun_Tax_Agency`** — *string*  
Municipality that levies property tax on the parcel. The layer covers parcels around Sandy as well as in it, so this is how to select Sandy's own.

**`Township`** — *string*  
Township of the Public Land Survey System description.

**`Range`** — *string*  
Range of the Public Land Survey System description.

**`Section`** — *int16*  
Section of the Public Land Survey System description.

**`Annexation`** — *string*  
Annexation that brought the parcel into the city.

**`Lot`** — *string*  
Lot number within the recorded subdivision.

**`Subdivision`** — *string*  
Recorded subdivision the parcel lies in.

**`ASSESSOR_DATA_VALID_FOR`** — *string*  
Tax year the assessor's valuation columns apply to.

**`neighborhood_code`** — *int32*  
Assessor's neighbourhood code. Comparable sales are drawn from within a neighbourhood when valuing a parcel.

**`nbhrd_low_sale`** — *int32*  
Lowest comparable sale price in the assessor's neighbourhood, in dollars.

**`nbhrd_high_sale`** — *int32*  
Highest comparable sale price in the neighbourhood.

**`nbhrd_av_sale`** — *int32*  
Average comparable sale price in the neighbourhood.

**`new_growth_value`** — *int32*  
Value attributed to new construction in the assessment year, which a taxing entity may levy on outside its certified rate.

**`nbrhd_av_home_sf`** — *int32*  
Average home floor area in the neighbourhood, in square feet.

**`abv_grnd_sf`** — *int32*  
Above-ground floor area in square feet, excluding basements.

**`multi_structure`** — *string*  
Marker for a parcel carrying more than one structure.

**`tax_year`** — *string*  
Tax year the valuation columns apply to.

**`greenbelt_acres`** — *double*  
Acres assessed under Utah's Farmland Assessment Act, which values qualifying agricultural land on its productive value rather than its market value.

**`full_mkt_prcl_total`** — *double*  
Full market value of the parcel, land and buildings, in dollars.

**`full_mkt_total_land`** — *double*  
Full market value of the land alone.

**`adjusted_prcl_total`** — *double*  
Parcel value after adjustments such as the residential exemption.

**`adjusted_total_land`** — *double*  
Land value after adjustments.

**`full_mkt_total_bldg`** — *double*  
Full market value of the buildings alone.

**`adjusted_total_bldg`** — *double*  
Building value after adjustments.

**`total_full_mkt`** — *double*  
Total full market value carried on the roll.

**`total_adjusted`** — *double*  
Total adjusted value carried on the roll.

**`total_assessed`** — *double*  
Assessed value in dollars before exemptions.

**`taxable_value`** — *double*  
Taxable value in dollars for the stated tax year, after exemptions.

**`year_built`** — *double*  
Year the principal building was constructed. Zero or null where the parcel carries no building.

**`total_sq_ft`** — *double*  
Building floor area in square feet, where a building is assessed on the parcel.

**`num_housing_units`** — *double*  
Number of dwelling units on the parcel.

**`lot_use`** — *string*  
Assessor's land-use code for the lot.

**`zip_two`** — *string*  
Secondary ZIP code, where the parcel spans two.

**`tax_class1`** — *string*  
Primary tax class code.

**`Tax_Class1_Desc`** — *string*  
Description of the primary tax class.

**`tax_class2`** — *string*  
Second tax class code, where a parcel carries more than one.

**`Tax_Class2_Desc`** — *string*  
Description of the second tax class.

**`tax_class3`** — *string*  
Third tax class code.

**`Tax_Class3_Desc`** — *string*  
Description of the third tax class.

**`tax_rate`** — *double*  
Combined tax rate applied to the parcel.

**`Garbage`** — *string*  
Whether the parcel receives Sandy City garbage collection.

**`Legal_Description`** — *string*  
Recorded legal description of the parcel.

**`Shape__Area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape__Length`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`Tax_District_2022`** — *string*  
Tax district as of the 2022 roll.

**`Sensitive_Overlay`** — *string*  
Whether the parcel falls in the Sensitive Area Overlay zone, which constrains development on the mountain front.

**`Historic_Tiers`** — *string*  
Historic designation tier applying to the parcel.

**`Wildland_Interface`** — *string*  
Whether the parcel falls in the wildland urban interface, where wildfire risk governs building standards.

**`Floodplain`** — *string*  
Whether the parcel intersects the mapped floodplain.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/parcels/parcels.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0?f=json) on 2026-10-07T21:32:21Z.
Sandy City publishes no licence for this data; see the [README](README.md).
