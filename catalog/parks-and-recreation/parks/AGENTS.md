# AGENTS.md — Parks

Every claim here is quoted from the upstream service or measured from the published file.

## The one thing that will trip you up

The GeoParquet is in **EPSG:3566** (NAD83(HARN) / Utah Central (ftUS)). Linear units are **US survey feet**, so `ST_Length` and `ST_Area` return that unit. The PMTiles are Web Mercator, because tiles have to be. Reproject before any distance comparison with another dataset:

```sql
SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/parks/parks.parquet';
```

There is a `bbox` struct column on every row, written by gpio for spatial pruning. It is in EPSG:3566 too.

## Schema

72 columns, 41 rows.


**Where these meanings come from.** Park inventory maintained by Sandy City Parks and Recreation. The amenity columns are counts or yes/no flags recorded per park. The `Acq`, `Dev`, `LWCF` and `Prot` columns follow the land-protection vocabulary used across US recreation datasets, where LWCF is the [Land and Water Conservation Fund](https://www.nps.gov/subjects/lwcf/index.htm): land bought with those funds carries a Section 6(f) restriction against conversion to other uses.

72 of 72 columns carry a definition. The rest say so rather than guess.

**`OBJECTID`** — *int64*  
Esri object identifier. A row number assigned by the source geodatabase and reassigned when the layer is republished. It is not a stable key and must not be used to join across collections or across refreshes.

**`NAME`** — *string*  
Name of the feature. Measured in the published file: Populated on 100% of 41 rows, 41 distinct values.

**`Address`** — *string*  
Street address of the feature. Measured in the published file: Populated on 100% of 41 rows, 41 distinct values.

**`Municipality`** — *string*  
Municipality the feature falls in. Several Sandy layers extend into neighbouring cities, so this is how to select Sandy's own. Measured in the published file: Populated on 100% of 41 rows, 1 distinct values.

**`Phone`** — *string*  
Public contact telephone number for the facility, not for an individual. Measured in the published file: Populated on 98% of 41 rows, 4 distinct values.

**`Type`** — *string*  
Type of feature. See the measured values below, because the source layer declares no code list for it. Measured in the published file: Populated on 100% of 41 rows, 1 distinct values.

**`Acres`** — *double*  
Area in acres. Measured in the published file: Populated on 98% of 41 rows, 40 distinct values, ranging 0.0875616 to 175.631.

**`Reservable`** — *string*  
Whether the park or its facilities can be reserved.

**`Indoor_Pavilion`** — *string*  
Whether the park has an indoor pavilion.

**`Outdoor_Pavilion`** — *string*  
Whether the park has an outdoor pavilion.

**`Restrooms`** — *string*  
Whether the park has public restrooms.

**`Parking_Stalls`** — *int16*  
Number of parking stalls at the park.

**`BBQ_Pit`** — *string*  
Whether the park has a barbecue pit.

**`Playground`** — *string*  
Whether the park has a playground.

**`Jogging_Path_Miles`** — *double*  
Length of jogging path within the park, in miles.

**`Baseball_Diamonds`** — *int16*  
Number of baseball diamonds.

**`Baseball_Lighting`** — *string*  
Whether the baseball diamonds are lit for evening play.

**`Basketball_Stands`** — *int16*  
Number of basketball standards, meaning hoops, rather than full courts.

**`Basketball_Lighting`** — *string*  
Whether the basketball courts are lit.

**`Soccer_Fields`** — *int16*  
Number of soccer fields.

**`Soccer_Lighting`** — *string*  
Whether the soccer fields are lit.

**`Softball_Diamonds`** — *int16*  
Number of softball diamonds.

**`Softball_Lighting`** — *string*  
Whether the softball diamonds are lit.

**`Tennis_Courts`** — *int16*  
Number of tennis courts.

**`Tennis_Lighting`** — *string*  
Whether the tennis courts are lit.

**`Volleyball_Courts`** — *int16*  
Number of volleyball courts.

**`Volleyball_Lighting`** — *string*  
Whether the volleyball courts are lit.

**`Electrical_Outlets`** — *string*  
Whether public electrical outlets are available.

**`Water_Outlets`** — *string*  
Whether public water outlets are available.

**`Notes`** — *string*  
Free-text note entered by city staff. Unstructured and inconsistently populated.

**`URL`** — *string*  
Link to a page about this feature on a city or partner website.

**`ParkID`** — *string*  
Identifier of the park the feature belongs to, joining to the parks collection. Measured in the published file: Populated on 100% of 41 rows, 41 distinct values.

**`Park_ID`** — *double*  
Numeric identifier of the park the feature belongs to. Measured in the published file: Populated on 100% of 41 rows, 41 distinct values, ranging 10 to 71.

**`County`** — *string*  
County the feature falls in. Sandy is in Salt Lake County. Measured in the published file: Populated on 100% of 41 rows, 1 distinct values.

**`State`** — *string*  
State the feature falls in. Measured in the published file: Populated on 100% of 41 rows, 1 distinct values.

**`StreetNum`** — *string*  
House number component of the address. Measured in the published file: Populated on 98% of 41 rows, 38 distinct values.

**`StreetName`** — *string*  
Street name component of the address. Measured in the published file: Populated on 98% of 41 rows, 33 distinct values.

**`StreetType`** — *string*  
Street type component of the address, such as ST or AVE. Measured in the published file: Populated on 98% of 41 rows, 11 distinct values.

**`Zip`** — *string*  
Postal ZIP code. Measured in the published file: Populated on 100% of 41 rows, 4 distinct values.

**`Reference`** — *string*  
Coded value. The source layer's domain allows: `Entrance`, `Center Point`, `Facility`, `Other`. Codes: `Entrance` = Entrance, `Center_Point` = Center Point, `Facility` = Facility, `Other` = Other.

**`RefComment`** — *string*  
Note on what the reference point represents.

**`Park_Acres`** — *double*  
Park area in acres as recorded by the department.

**`AcreSource`** — *string*  
One of. The source layer's domain allows: `Parcel`, `Deed`, `Survey`, `GIS Value`, `Other`.

**`YearOpen`** — *int32*  
Year the feature opened to the public. Empty in all 41 rows of the published file.

**`ParkStatus`** — *string*  
One of. The source layer's domain allows: `Open`, `Open_Fee`, `Open_Restricted`, `Closed`, `Decommissioned`, `Unknown`, `Planned`, `Proposed`.

**`StatusCmnt`** — *string*  
Note on the park's status.

**`ParkType`** — *string*  
Type of park, such as neighbourhood or regional.

**`ServicArea`** — *string*  
One of. The source layer's domain allows: `0-0.5 miles`, `0-5 miles`, `0-25 miles`, `0-100 miles`, `0-100 or more miles`.

**`MgtPriorty`** — *string*  
One of. The source layer's domain allows: `Active Park`, `Passive Park`, `Mixed-use Park`, `Natural Area`, `Historical/Cultural`, `Special Use Area`, `Corridor`.

**`Landowner`** — *string*  
Organisation that owns the land. Values are organisations, not individuals.

**`OwnerType`** — *string*  
One of. The source layer's domain allows: `Federal`, `State`, `County`, `Municipal`, `Special District`, `Private - NP`, `Private`, `Unknown`, `School`.

**`AgencyName`** — *string*  
Organisation that manages the park, which is not always the owner.

**`AgencyType`** — *string*  
One of. The source layer's domain allows: `Federal`, `State`, `County`, `Municipal`, `Special District`, `Private - NP`, `Private`, `Unknown`, `School`.

**`AcqSource`** — *string*  
Coded value. The source layer's domain allows: `Donation`, `Transfer`, `Bond`, `Capital Budget`, `Special Tax or assessment`, `Exactions`, `Federal Grant`, `State Grant`, `Other Grant`, `Other`, and 2 more. Codes: `Donation` = Donation, `Transfer` = Transfer, `Bond` = Bond, `Capital Budget` = Capital Budget, `Special tax or assessment` = Special Tax or assessment, `Exactions` = Exactions, `Federal Grant` = Federal Grant, `State Grant` = State Grant, `Other Grant` = Other Grant, `Other` = Other, `Multiple` = Multiple, `Partnership` = Partnership.

**`AcqMethod`** — *string*  
One of. The source layer's domain allows: `Fee simple`, `Easement`, `Lease`, `Eminent Domain`, `Land Exchange`, `Transfer`, `Donation`, `Other`.

**`AcqComment`** — *string*  
Note on how the land was acquired.

**`DevSource`** — *string*  
One of. The source layer's domain allows: `None`, `Donation`, `Bond`, `Capital Budget`, `Special tax or assessment`, `Exactions`, `Federal Grant`, `State Grant`, `Other Grant`, `Other`, and 2 more.

**`DevComment`** — *string*  
Note on how the park was developed.

**`Restricts`** — *string*  
One of. The source layer's domain allows: `None`, `Deed/Covenant`, `License`, `Easement`, `Lien`, `Zoning`, `Multiple`, `Other`.

**`LWCFProt`** — *string*  
One of. The source layer's domain allows: `Yes`, `No`.

**`OtherProt`** — *string*  
One of. The source layer's domain allows: `None`, `Federal Grant`, `State Specific`, `Conservation Easement`, `Trail Easement`, `Multiple`, `Railbank (Railtrail)`, `Unknown`.

**`ResPrtCmnt`** — *string*  
Note on restrictions or protections that apply to the land.

**`EditDate`** — *timestamp[ms]*  
Timestamp when the row was last edited, from the geodatabase editor tracking. It records the database edit, not a change in the world.

**`Unit`** — *string*  
Unit of the adjacent measurement column. Measured in the published file: Populated on 100% of 41 rows, 1 distinct values.

**`Unit_ID`** — *string*  
Identifier of the unit within the park.

**`Unit_Acres`** — *double*  
Area in acres of this unit of the park, where a park is split into units.

**`AddedTrails`** — *string*  
Trail mileage added within the park.

**`Shape`** — *binary*  
Residual Esri geometry field. It carries no coordinates here; the geometry is in the `geometry` column.

**`Shape.area`** — *double*  
Polygon area computed by the geodatabase, in the square units of the source coordinate system. Recompute it from the geometry rather than trusting it, because it is not updated when a shape is edited.

**`Shape.len`** — *double*  
Line length or polygon perimeter computed by the geodatabase, in the units of the source coordinate system. Recompute it from the geometry rather than trusting it.

**`geometry`** — *binary*  
Feature geometry, WKB encoded, in the collection's `proj:epsg` coordinate system.

**`bbox`** — *struct<xmin: double, ymin: double, xmax: double, ymax: double>*  
Per-row bounding box written by gpio, as a struct of `xmin`, `ymin`, `xmax`, `ymax`, in the same coordinate system as the geometry. Rows are in Hilbert order, so filtering on this column prunes row groups efficiently.

## Coded values

These are the code lists the ArcGIS layer publishes as field domains. They are the only column documentation Sandy City provides, and they are reproduced verbatim.

**`Reference`**

- `Entrance` = Entrance
- `Center_Point` = Center Point
- `Facility` = Facility
- `Other` = Other

**`AcqSource`**

- `Donation` = Donation
- `Transfer` = Transfer
- `Bond` = Bond
- `Capital Budget` = Capital Budget
- `Special tax or assessment` = Special Tax or assessment
- `Exactions` = Exactions
- `Federal Grant` = Federal Grant
- `State Grant` = State Grant
- `Other Grant` = Other Grant
- `Other` = Other
- `Multiple` = Multiple
- `Partnership` = Partnership

## A query that runs

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT * FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/parks/parks.parquet' LIMIT 5;
```

Count by the column the default style uses:

The default style is a single colour: no column in this collection has both low cardinality and enough population to carry a meaningful legend.

## Provenance

Mirrored from [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Parks/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Parks/MapServer/0?f=json) on 2026-10-07T21:00:33Z.
Sandy City publishes no licence for this data; see the [README](README.md).
