# Fire Stations

Fire Stations in and around Sandy City, Utah. 68 point features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 68 (Point)
- **Extent (WGS84)**: `-112.095736, 40.480028, -111.580749, 40.793871`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Fire_Stations/MapServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/Fire_Stations/MapServer/0)
- **Mirrored**: 2026-10-06T22:11:04Z
- **Attribution, as the service states it**: Sandy City GIS

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`fire-stations.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-stations/fire-stations.parquet) — GeoParquet, EPSG:3566
- [`fire-stations.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-stations/fire-stations.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/fire-stations/fire-stations.parquet';
```

## Known issues

- `Type` holds inconsistent values: `METRO` and `Metro` both appear, and one row reads `DFD\r\nDFD`. The shipped style normalises them for display; the data is left as the city published it.
