# AGENTS.md — Public Utilities

7 collections. Most GeoParquet here is **EPSG:3566** (NAD83(HARN) / Utah Central, US survey feet), but not all of it: `lead-service-lines` is EPSG:2850 (metres). Check `proj:epsg` on the collection before computing any length or area. Each collection's own `AGENTS.md` carries its schema, its coded-value lists and a query that runs.

- [Fire Hydrants](./fire-hydrants/) — see its README for columns and caveats
- [Water Service Line Material Inventory](./lead-service-lines/) — see its README for columns and caveats
- [Sewer Mains](./sewer-mains/) — see its README for columns and caveats
- [Storm Drain Pipes](./storm-drain-pipes/) — see its README for columns and caveats
- [Streams](./streams/) — see its README for columns and caveats
- [Street Lights](./street-lights/) — see its README for columns and caveats
- [Water Distribution Mains](./water-distribution-mains/) — see its README for columns and caveats

Sandy City publishes no licence for this data. See the [catalog agent guide](../AGENTS.md).
