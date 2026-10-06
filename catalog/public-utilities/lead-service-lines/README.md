# Water Service Line Material Inventory

Water Service Line Material Inventory in Sandy City, Utah. The upstream service publishes no description for this layer. Published by Sandy City to meet the service line inventory requirement of the US EPA Lead and Copper Rule Revisions. The inventory is incomplete: most lines are still classified Unknown. 26,213 point features, mirrored from the city's ArcGIS Server as GeoParquet in EPSG:3566 (NAD83/HARN Utah Central, US survey feet) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 26,213 (Point)
- **Extent (WGS84)**: `-111.916932, 40.528258, -111.778039, 40.616166`
- **Coordinate system**: EPSG:3566, NAD83/HARN Utah Central, US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/ServiceLine_viewing_7fe7c6729fd949afb34452df1ba78945/FeatureServer/0](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/ServiceLine_viewing_7fe7c6729fd949afb34452df1ba78945/FeatureServer/0)
- **Mirrored**: 2026-10-06T19:01:44Z

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`lead-service-lines.parquet`](https://data.source.coop/portolan-mirrors/sandy-portolan/public-utilities/lead-service-lines/lead-service-lines.parquet) — GeoParquet, EPSG:3566
- [`lead-service-lines.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-portolan/public-utilities/lead-service-lines/lead-service-lines.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/public-utilities/lead-service-lines/lead-service-lines.parquet';
```

## Known issues

- `accountid`, a utility customer identifier, was dropped before publication.
- Columns dropped from the upstream layer before publication: `Editor`/`Creator` (the staff username that last edited the row) and `GlobalID` (an Esri replication identifier). `EditDate` and `CreationDate` are kept, because they carry real provenance.
- The upstream service publishes no description for this layer, so this page describes only what the data contains.
