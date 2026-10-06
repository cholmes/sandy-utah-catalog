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

| column | type |
| --- | --- |
| `OBJECTID` | int64 |
| `Parcel_Id` | string |
| `Address` | string |
| `HSNO` | int32 |
| `DIR` | string |
| `STREET` | string |
| `SFX` | string |
| `STREET_DIR` | string |
| `APT` | string |
| `Municipality` | string |
| `Zip` | string |
| `Zip_Four` | string |
| `InSandy` | string |
| `Prop_Type` | string |
| `Prop_Subtype` | string |
| `IsRental` | string |
| `Building_Units` | int16 |
| `Complex_Name` | string |
| `Alias_ID` | int32 |
| `Alias_Street` | string |
| `Alias_Suffix_Dir` | string |
| `Updated_Date` | timestamp[ms] |
| `Updated_By` | string |
| `Year_Built` | string |
| `Comment` | string |
| `Source` | string |
| `Placement` | string |
| `X_Coord` | double |
| `Y_Coord` | double |
| `Addy_ID` | int32 |
| `Addy_ID_Text` | string |
| `PPH_Approx` | double |
| `Shape` | binary |
| `Municipality_Code` | string |
| `New_Municipality_Code` | string |
| `geometry` | binary |
| `bbox` | struct<xmin: double, ymin: double, xmax: double, ymax: double> |

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Municipality`**

- `Cottonwood Heights` = Cottonwood Heights
- `Draper` = Draper
- `Holladay` = Holladay
- `Midvale` = Midvale
- `Murray` = Murray
- `Riverton` = Riverton
- `Sandy` = Sandy
- `South Jordan` = South Jordan
- `Taylorsville` = Taylorsville
- `West Jordan` = West Jordan
- `Unincorporated - Internal` = Unincorporated - Internal
- `Unincorporated - External` = Unincorporated - External

**`InSandy`**

- `Yes` = Yes
- `No` = No

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

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Address_Points/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Address_Points/MapServer/0) on 2026-10-06T22:11:04Z.
Sandy City publishes no licence for this data; see the [README](README.md).
