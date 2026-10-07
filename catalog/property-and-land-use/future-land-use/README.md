# Future Land Use

Future Land Use Map from Sandy City General Plan. 979 multipolygon features, mirrored as GeoParquet in EPSG:3857 (WGS 84 / Pseudo-Mercator) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 979 (MultiPolygon)
- **Extent (WGS84)**: `-111.921593, 40.528075, -111.77701, 40.618004`
- **Coordinate system**: EPSG:3857, WGS 84 / Pseudo-Mercator — linear units are Mercator metres, which are not ground distances away from the equator

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Sandy_Future_Land_Use_Map_WFL1/FeatureServer/12](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Sandy_Future_Land_Use_Map_WFL1/FeatureServer/12?f=json) (the city's server answers 403 on the plain endpoint, so this links the `f=json` form it does serve)
- **Mirrored**: 2026-10-07T21:32:21Z

Converted with [gpio](https://github.com/geoparquet/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`future-land-use.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/future-land-use/future-land-use.parquet) — GeoParquet, EPSG:3566
- [`future-land-use.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/future-land-use/future-land-use.pmtiles) — vector tiles, Web Mercator

## Columns

The [agent guide](AGENTS.md) documents every column, with the source of each definition. Columns Sandy City does not define say so, rather than carrying a guess.

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/future-land-use/future-land-use.parquet';
```
