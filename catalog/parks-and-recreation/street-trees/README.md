# Street and Park Trees

An inventory of trees in Sandy City, Utah. The same tree inventory is published twice by the city, as `Parks/Grounds_and_Forestry` and as `Pub_Works/ParksDeptTrees`, both reporting the same feature count. This mirrors the Parks copy. 7,966 point features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 7,966 (Point)
- **Extent (WGS84)**: `-111.917739, 40.529528, -111.803488, 40.617339`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Grounds_and_Forestry/FeatureServer/0](https://gis.sandy.utah.gov/arcgis/rest/services/Parks/Grounds_and_Forestry/FeatureServer/0)
- **Mirrored**: 2026-10-06T20:20:34Z
- **Attribution, as the service states it**: Sandy City GIS

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`street-trees.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/street-trees/street-trees.parquet) — GeoParquet, EPSG:3566
- [`street-trees.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/street-trees/street-trees.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/street-trees/street-trees.parquet';
```

## Known issues

- 31 of the 7,997 rows published upstream carried WGS84 degree values in a coordinate system measured in US survey feet, which placed them off the coast of Mexico. They are dropped here rather than reprojected, because recovering them means asserting an interpretation of the city's data that the city has not confirmed. This mirror holds 7,966 rows.
