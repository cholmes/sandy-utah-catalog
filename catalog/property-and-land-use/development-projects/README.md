# Development Projects

Development Projects in Sandy City, Utah. The upstream service publishes no description for this layer. 64 multipolygon features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 64 (MultiPolygon)
- **Extent (WGS84)**: `-111.912695, 40.537123, -111.787165, 40.613476`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Development_Projects/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Works/Development_Projects/FeatureServer/0)
- **Mirrored**: 2026-10-06T20:20:34Z

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`development-projects.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/development-projects/development-projects.parquet) — GeoParquet, EPSG:3566
- [`development-projects.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/development-projects/development-projects.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/development-projects/development-projects.parquet';
```

## Known issues

- The upstream service publishes no description for this layer, so this page describes only what the data contains.
