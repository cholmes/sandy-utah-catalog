# Police Calls for Service

Police Calls for Service in Sandy City, Utah. The upstream service publishes no description for this layer. 185,647 point features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 185,647 (Point)
- **Extent (WGS84)**: `-116.049189, 20.524344, -111.642928, 40.821874`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCallData/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCallData/FeatureServer/0)
- **Mirrored**: 2026-10-06T20:51:07Z

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`police-calls.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-calls/police-calls.parquet) — GeoParquet, EPSG:3566
- [`police-calls.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-calls/police-calls.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-calls/police-calls.parquet';
```

## Known issues

- Three columns were dropped before publication: `reporting_officer1` and `rep_officer1_d`, which name the reporting officer, and `apartment`. `gps_latitude` and `gps_longitude` were dropped because the geometry column carries the same information.
- A call for service is not a confirmed offence. Many calls close with no crime found. Do not read this as a crime count; `crime-incidents` is the offence record.
- The upstream service publishes no description for this layer, so this page describes only what the data contains.
