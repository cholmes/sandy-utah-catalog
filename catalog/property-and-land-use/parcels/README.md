# Parcels

Parcels in and around Sandy City, Utah as of July, 2022. The service describes itself as current to July 2022, so it lags the county's live parcel fabric by more than three years. 106,087 multipolygon features, mirrored from the city's ArcGIS Server as GeoParquet in EPSG:3566 (NAD83/HARN Utah Central, US survey feet) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 106,087 (MultiPolygon)
- **Extent (WGS84)**: `-111.972924, 40.496643, -111.746465, 40.650177`
- **Coordinate system**: EPSG:3566, NAD83/HARN Utah Central, US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Parcels/FeatureServer/0)
- **Mirrored**: 2026-10-06T19:01:44Z
- **Attribution, as the service states it**: Salt Lake County Recorder

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`parcels.parquet`](https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/parcels/parcels.parquet) — GeoParquet, EPSG:3566
- [`parcels.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/parcels/parcels.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/parcels/parcels.parquet';
```

## Known issues

- The upstream service states the extract is current to July 2022.
