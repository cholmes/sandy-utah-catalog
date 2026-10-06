# Police Reporting Areas

Police reporting areas in Sandy City, Utah. 439 multipolygon features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 439 (MultiPolygon)
- **Extent (WGS84)**: `-111.921268, 40.527841, -111.777212, 40.61822`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Police_Reporting_Areas/MapServer/1](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Police_Reporting_Areas/MapServer/1)
- **Mirrored**: 2026-10-06T20:51:07Z
- **Attribution, as the service states it**: Sandy City GIS

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`police-reporting-areas.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-reporting-areas/police-reporting-areas.parquet) — GeoParquet, EPSG:3566
- [`police-reporting-areas.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-reporting-areas/police-reporting-areas.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/police-reporting-areas/police-reporting-areas.parquet';
```
