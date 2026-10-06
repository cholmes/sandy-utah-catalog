# AGENTS.md — Parcels

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566**, NAD83/HARN Utah Central, in **US survey feet**. `ST_Length` and `ST_Area` return feet and square feet, not metres. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/parcels/parcels.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

84 columns, 106,087 rows.

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `RECORDER_DATA_AS_OF` | string |
| `parcel_id` | string |
| `parent_parcel` | string |
| `num_old_prcls` | int32 |
| `source_doc` | string |
| `date_created` | string |
| `last_vesting` | int32 |
| `parcel_acres` | double |
| `own_name` | string |
| `multi_names` | int32 |
| `tax_dist` | string |
| `care_of` | string |
| `own_addr` | string |
| `own_apt_num` | string |
| `own_citystate` | string |
| `own_country_code` | string |
| `own_zip` | string |
| `own_zip_four` | string |
| `prop_location` | string |
| `HouseNum` | string |
| `PreDir` | string |
| `StreetName` | string |
| `StreetType` | string |
| `StreetDir` | string |
| `exempt_type` | string |
| `property_type` | string |
| `Property_Type_Desc` | string |
| `Property_Type_Simple_Desc` | string |
| `Community` | string |
| `Quadrant` | string |
| `CityCouncil` | string |
| `Abnormal` | string |
| `Mun_Tax_Agency` | string |
| `Township` | string |
| `Range` | string |
| `Section` | int16 |
| `Annexation` | string |
| `Lot` | string |
| `Subdivision` | string |
| `ASSESSOR_DATA_VALID_FOR` | string |
| `neighborhood_code` | int32 |
| `nbhrd_low_sale` | int32 |
| `nbhrd_high_sale` | int32 |
| `nbhrd_av_sale` | int32 |
| `new_growth_value` | int32 |
| `nbrhd_av_home_sf` | int32 |
| `abv_grnd_sf` | int32 |
| `multi_structure` | string |
| `tax_year` | string |
| `greenbelt_acres` | double |
| `full_mkt_prcl_total` | double |
| `full_mkt_total_land` | double |
| `adjusted_prcl_total` | double |
| `adjusted_total_land` | double |
| `full_mkt_total_bldg` | double |
| `adjusted_total_bldg` | double |
| `total_full_mkt` | double |
| `total_adjusted` | double |
| `total_assessed` | double |
| `taxable_value` | double |
| `year_built` | double |
| `total_sq_ft` | double |
| `num_housing_units` | double |
| `lot_use` | string |
| `zip_two` | string |
| `tax_class1` | string |
| `Tax_Class1_Desc` | string |
| `tax_class2` | string |
| `Tax_Class2_Desc` | string |
| `tax_class3` | string |
| `Tax_Class3_Desc` | string |
| `tax_rate` | double |
| `Garbage` | string |
| `Legal_Description` | string |
| `Shape__Area` | double |
| `Shape__Length` | double |
| `Tax_District_2022` | string |
| `Sensitive_Overlay` | string |
| `Historic_Tiers` | string |
| `Wildland_Interface` | string |
| `Floodplain` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

The upstream layer publishes no field domains, so no column in this collection has a documented code list. Where a column holds opaque codes, their meaning is unknown rather than omitted.

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/parcels/parcels.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0) on 2026-10-06T19:01:44Z.
Sandy City publishes no licence for this data; see the [README](README.md).
