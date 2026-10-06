# Zoning Districts

Sandy Zoning districts for consumption by SLCo. 454 multipolygon features, mirrored from the city's ArcGIS Server as GeoParquet in EPSG:3566 (NAD83/HARN Utah Central, US survey feet) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 454 (MultiPolygon)
- **Extent (WGS84)**: `-111.921268, 40.527839, -111.777212, 40.61822`
- **Coordinate system**: EPSG:3566, NAD83/HARN Utah Central, US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Common/Zoning_Ex/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Common/Zoning_Ex/FeatureServer/0)
- **Mirrored**: 2026-10-06T19:01:44Z
- **Attribution, as the service states it**: Sandy City GIS

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`zoning.parquet`](https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/zoning/zoning.parquet) — GeoParquet, EPSG:3566
- [`zoning.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/zoning/zoning.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-portolan/property-and-land-use/zoning/zoning.parquet';
```

## Known issues

- `Zone_Code` is null in all 454 rows. Use `LEGEND_COD` or `ZONE`.
- Columns dropped from the upstream layer before publication: `Editor`/`Creator` (the staff username that last edited the row) and `GlobalID` (an Esri replication identifier). `EditDate` and `CreationDate` are kept, because they carry real provenance.
