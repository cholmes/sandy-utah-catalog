# Site Plan Review Applications

Site Plan Review Applications in Sandy City, Utah. The upstream service publishes no description for this layer. 1,549 multipolygon features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 1,549 (MultiPolygon)
- **Extent (WGS84)**: `-111.92115, 40.525347, -111.796476, 40.61705`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/SPR/FeatureServer/0](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/SPR/FeatureServer/0)
- **Mirrored**: 2026-10-06T22:11:04Z

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`site-plan-review.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/site-plan-review/site-plan-review.parquet) — GeoParquet, EPSG:3566
- [`site-plan-review.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/site-plan-review/site-plan-review.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/site-plan-review/site-plan-review.parquet';
```

## Known issues

- Four of the 1,549 rows published upstream carry no geometry. They stay in the GeoParquet, because the application record is still real, but they cannot appear in the vector tiles.
- The upstream service publishes no description for this layer, so this page describes only what the data contains.
