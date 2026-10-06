# Crime Incidents

Crime Incidents in Sandy City, Utah. The upstream service publishes no description for this layer. 29,572 point features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 29,572 (Point)
- **Extent (WGS84)**: `-112.184857, 40.433108, -111.70137, 40.808153`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCrimeData/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Pub_Safety/PoliceCrimeData/FeatureServer/0)
- **Mirrored**: 2026-10-06T20:51:07Z

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`crime-incidents.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/crime-incidents/crime-incidents.parquet) — GeoParquet, EPSG:3566
- [`crime-incidents.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/crime-incidents/crime-incidents.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-safety/crime-incidents/crime-incidents.parquet';
```

## Known issues

- Three columns were dropped before publication: `officer` and `officer_d`, which name the responding officer, and `apartment`, which gives the unit within a building. The street-level `location` is kept. `gps_latitude` and `gps_longitude` were dropped because the geometry column carries the same information.
- The extract covers 2023 to 2026. It is a mirror of what the service returned on the sync date and is not a certified record. Use the Sandy City Police Department for anything official.
- The upstream service publishes no description for this layer, so this page describes only what the data contains.
