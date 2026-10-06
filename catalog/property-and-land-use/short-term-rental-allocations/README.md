# Short-Term Rental Allocations

Community Count for Short Term Rentals in Sandy City
This map contains a polygon layer of the Sandy City Communities. With attributes of the allocated short term rental space. This layer holds the per-community short-term-rental permit cap, not the location of individual rentals. Each of the 30 community areas carries `Max_STR` (the cap), `Current_STR` (permits issued) and `Open_STR` (permits still available). One community is at -1, meaning it is over its cap. 30 multipolygon features, mirrored as GeoParquet in EPSG:3566 (NAD83(HARN) / Utah Central (ftUS)) with Web Mercator vector tiles for display. See the [agent guide](AGENTS.md) for the schema, the coded-value lists and queries that run.

## Coverage

- **Features**: 30 (MultiPolygon)
- **Extent (WGS84)**: `-111.921268, 40.527841, -111.777212, 40.61822`
- **Coordinate system**: EPSG:3566, NAD83(HARN) / Utah Central (ftUS) — linear units are US survey feet

## Licence

Sandy City publishes no licence for this data. There is no terms-of-use page on the city's GIS site, and no layer on the city's ArcGIS Server or ArcGIS Online organisation carries a licence statement. The data is a public record under the [Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html). Reuse terms are unconfirmed. The `other` licence identifier records that honestly rather than asserting a grant the city never made.

## Provenance

This is a **mirror**. Sandy City produced the data; it is republished here unmodified except where noted below.

- **Source**: [https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2](https://services3.arcgis.com/IGYUtIzoA63tzE48/arcgis/rest/services/Short_Term_Rental_Allocations_Map/FeatureServer/2)
- **Mirrored**: 2026-10-06T20:37:26Z

Converted with [gpio](https://github.com/developmentseed/geoparquet-io) (`extract arcgis --output-crs native`, preserving the source projection) and tiled with [tylertoo](https://github.com/geoparquet-io/tylertoo) 0.7.1.

## Files

- [`short-term-rental-allocations.parquet`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet) — GeoParquet, EPSG:3566
- [`short-term-rental-allocations.pmtiles`](https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.pmtiles) — vector tiles, Web Mercator

## Reading it

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;
SELECT count(*) FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/short-term-rental-allocations/short-term-rental-allocations.parquet';
```
