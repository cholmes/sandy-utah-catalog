# Sandy City, Utah — Municipal Open Data

A cloud-native mirror of the public geospatial data published by Sandy City,
Utah. 42 collections covering parcels, zoning, addresses, boundaries, parks
and trails, public safety districts, water and storm infrastructure, roads
and transit.

Sandy City serves this data from a public ArcGIS Server and an ArcGIS Online
organisation. It runs no open data portal, publishes no bulk downloads, and
states no licence. Using any of it today means reverse-engineering REST query
URLs and paginating by hand. This catalog republishes the public-interest
subset as GeoParquet and PMTiles so it can be queried, joined and mapped
directly.

**Sandy City produced this data. This catalog is an independent mirror and is
not endorsed by or affiliated with the city.**

## What is here

| Subcatalog | Collections | Covers |
| --- | --- | --- |
| [Boundaries and Districts](./boundaries/) | 6 | City limits, annexation history back to incorporation, community areas, council districts, voting precincts |
| [Property and Land Use](./property-and-land-use/) | 7 | 106,087 parcels, zoning, subdivisions, 60,400 address points, future land use, short-term rentals |
| [Parks and Recreation](./parks-and-recreation/) | 6 | Parks, 1,127 trail segments, trailheads, golf courses, 11,695 cemetery graves, 7,966 public trees |
| [Public Safety](./public-safety/) | 9 | Fire and police districts and stations, fireworks restrictions, fault zones, landslide risk, floodplain |
| [Public Utilities](./public-utilities/) | 7 | Water mains, hydrants, storm drains, sewer mains, streams, street lights, the lead service line inventory |
| [Public Works and Transportation](./public-works/) | 7 | Maintained roads, speed limits, sidewalks, pavement condition, UTA transit, waste collection |

Each collection has its own README with its columns, its provenance and what
is known to be wrong with it. Start with the [agent guide](AGENTS.md) if you
are writing a query.

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page
on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS
Online organisation carries a licence statement. The data is a public record
under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html).
Reuse terms are unconfirmed.

Every collection therefore declares the SPDX identifier `other`. That records
the situation honestly rather than asserting a grant the city never made. If
you need certainty for a commercial use, ask the city.

Note that the statewide [UGRC CC BY 4.0 policy](https://gis.utah.gov/about/policy/license-disclaimer/)
covers UGRC, not Sandy City, and does not carry down to municipal data.

## Provenance

Every collection is a mirror and carries a `via` link to the exact upstream
service layer it came from, plus the attribution string that service
publishes. Most read `Sandy City GIS`; parcels read `Salt Lake County
Recorder` and the county-wide boundary layer reads `AGRC`.

The data was converted with
[gpio](https://github.com/geoparquet/geoparquet-io) using
`extract arcgis --output-crs native`, which preserves the city's own
projection, and tiled with
[tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## What was removed

This mirror is not byte-identical to the upstream services. Three classes of
column were dropped, and each affected collection says so in its own README:

- **Personal contact details.** The community areas layer published home
  addresses, personal mobile numbers and personal email addresses for named
  resident volunteers. Twelve columns were dropped.
- **A utility customer identifier.** `accountid` was dropped from the lead
  service line inventory.
- **Editing metadata.** `Editor`, `Creator` and `GlobalID` were dropped
  throughout. `EditDate` and `CreationDate` were kept, because they carry real
  provenance.

One collection lost rows: 31 of 7,997 public trees carried WGS84 degree
values in a coordinate system measured in feet, placing them off the coast of
Mexico. They were dropped rather than reprojected.

## Reading it

Everything is queryable in place, with no download:

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;

SELECT ZONE, LEGEND_COD, count(*) AS n
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/zoning/zoning.parquet'
GROUP BY 1, 2
ORDER BY n DESC
LIMIT 10;
```

The GeoParquet is in **EPSG:3566** (NAD83/HARN Utah Central, US survey feet),
which is what Sandy City publishes. Lengths and areas come out in feet. The
PMTiles are Web Mercator. See the [agent guide](AGENTS.md) before joining
across collections.
