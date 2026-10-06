# AGENTS.md — Property and Land Use

7 collections. Most GeoParquet here is **EPSG:3566** (NAD83(HARN) / Utah Central, US survey feet), but not all of it: `future-land-use` is EPSG:3857 (Mercator metres, which are not ground distances away from the equator). Check `proj:epsg` on the collection before computing any length or area. Each collection's own `AGENTS.md` carries its schema, its coded-value lists and a query that runs.

- [Address Points](./address-points/) — see its README for columns and caveats
- [Future Land Use](./future-land-use/) — see its README for columns and caveats
- [Parcels](./parcels/) — see its README for columns and caveats
- [Sensitive Area Overlay Zone](./sensitive-overlay-zone/) — see its README for columns and caveats
- [Short-Term Rental Allocations](./short-term-rental-allocations/) — see its README for columns and caveats
- [Subdivisions](./subdivisions/) — see its README for columns and caveats
- [Zoning Districts](./zoning/) — see its README for columns and caveats

Sandy City publishes no licence for this data. See the [catalog agent guide](../AGENTS.md).
