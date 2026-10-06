# Sandy City Cemetery Graves

Provides access to the Sandy City, Utah Cemetery data. 11,695 multipolygon features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 11,695 (MultiPolygon)
- **Extent (WGS84)**: `-111.875163, 40.585733, -111.872348, 40.587933`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Sandy_Cemetery/FeatureServer/37](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Sandy_Cemetery/FeatureServer/37)
- **Mirrored**: 2026-10-06T19:24:57Z
- **Attribution, as the service states it**: Sandy City Parks & Rec

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`cemetery-graves.parquet`](https://data.source.coop/portolan-mirrors/sandy-portolan/parks-and-recreation/cemetery-graves/cemetery-graves.parquet) — GeoParquet, EPSG:3566
- [`cemetery-graves.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-portolan/parks-and-recreation/cemetery-graves/cemetery-graves.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/parks-and-recreation/cemetery-graves/cemetery-graves.parquet';
```

## Known issues

- The vector tiles carry four display columns; the GeoParquet carries all 60.
