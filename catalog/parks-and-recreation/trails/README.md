# Trails

Trails in Sandy City, Utah area. 1,127 multilinestring features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 1,127 (MultiLineString)
- **Extent (WGS84)**: `-111.924048, 40.482076, -111.716849, 40.640341`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Trails/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Trails/MapServer/0?f=json) (the city's server answers 403 on the plain endpoint, so this links the `f=json` form it does serve)
- **Mirrored**: 2026-10-07T21:32:21Z
- **Attribution, as the service states it**: Sandy City GIS

Converted with [gpio](https://github.com/geoparquet/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`trails.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/trails/trails.parquet) — GeoParquet, EPSG:3566
- [`trails.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/trails/trails.pmtiles) — vector tiles, Web Mercator

## Columns

The [agent guide](AGENTS.md) documents every column, with the source of each definition. Columns Sandy City does not define say so, rather than carrying a guess.

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/trails/trails.parquet';
```

## Known issues

- Columns dropped from the upstream layer before publication: `Editor`/`Creator` (the staff username that last edited the row) and `GlobalID` (an Esri replication identifier). `EditDate` and `CreationDate` are kept, because they carry real provenance.
