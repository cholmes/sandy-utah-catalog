# sandy-portolan

A git-backed [Portolan](https://www.portolan-sdi.org/) catalog mirroring the
public geospatial data of **Sandy City, Utah** — 42 collections covering
parcels, zoning, addresses, boundaries, parks and trails, public safety
districts, water and storm infrastructure, roads and transit.

Metadata lives in this repository and is validated by `rashid` on every pull
request. The data itself lives on Source Cooperative at
[portolan-mirrors/sandy-portolan](https://source.coop/portolan-mirrors/sandy-portolan).

**Sandy City produced this data. This catalog is an independent mirror and is
not endorsed by or affiliated with the city.**

## Why

Sandy City serves a large amount of geospatial data from a public ArcGIS
Server and an ArcGIS Online organisation. It runs no open data portal,
publishes no bulk downloads, and states no licence. Using any of it means
reverse-engineering REST query URLs and paginating by hand.

This catalog republishes the public-interest subset as GeoParquet and
PMTiles, documented well enough to query without guessing.

## Licence

Sandy City publishes no licence for this data. Every collection declares the
SPDX identifier `other`. See [catalog/LICENSE.md](catalog/LICENSE.md) for what
was checked and what that means for reuse.

## Layout

```
catalog/                     the published catalog; everything in it publishes
  catalog.json               root
  README.md  AGENTS.md       catalog-level documentation
  LICENSE.md                 licence status, linked by every collection
  <subcatalog>/              six, named for the city's own ArcGIS folders
    <collection>/
      collection.json
      README.md  AGENTS.md
      styles/default.json
tools/                       publish.py and upload_data.py
tests/                       the gates; run python3 tests/run_all.py
```

Data files are never committed. See [AGENTS.md](AGENTS.md) for the
contributor rules, including why this repository uses `tools/publish.py`
rather than `portolan push`, and how the PMTiles are built.

## Working on it

```bash
python3 tests/run_all.py          # all gates
rashid check catalog --schema --data-scope local
python3 tools/publish.py          # dry run
```

## Contributing

Found a wrong description, a mis-decoded column, or a licence statement from
the city that this catalog does not reflect? Open an issue or a pull request.
Metadata corrections are the reason this catalog lives in git.
