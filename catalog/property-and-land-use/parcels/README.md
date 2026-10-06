# Parcels

Parcels in and around Sandy City, Utah as of July, 2022. The service describes itself as current to July 2022, so it lags the county's live parcel fabric by more than three years. 106,087 multipolygon features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 106,087 (MultiPolygon)
- **Extent (WGS84)**: `-111.972924, 40.496643, -111.746465, 40.650177`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0)
- **Mirrored**: 2026-10-06T20:20:34Z
- **Attribution, as the service states it**: Salt Lake County Recorder

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`parcels.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/parcels/parcels.parquet) — GeoParquet, EPSG:3566
- [`parcels.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/parcels/parcels.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/parcels/parcels.parquet';
```

## Known issues

- The upstream service states the extract is current to July 2022.
- The GeoParquet carries all 84 columns the county publishes, including owner name and mailing address, which are public record under the Salt Lake County Recorder. The **vector tiles carry only seven display columns** (`parcel_id`, `prop_location`, `Property_Type_Simple_Desc`, `parcel_acres`, `year_built`, `total_sq_ft`, `Community`). Carrying all 84 pushed 56 of 106 full-zoom tiles past the 500 KB cap, and the tiler shed 37,706 parcels to fit. Query the GeoParquet for anything not in that list.
