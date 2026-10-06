# AGENTS.md — Sandy City, Utah — Municipal Open Data

Guidance for AI agents and automated clients working with this catalog.

**One rule survives every edit to this file.** Every claim here is either
quoted from a source or measured from the data. If you cannot point at where a
fact came from, it does not belong in this file. An agent acting on an
invented join key or an invented column name produces a confident wrong
answer, and nothing downstream catches it.

## What this catalog holds

42 collections mirrored from Sandy City, Utah, grouped into six subcatalogs
that follow the city's own ArcGIS folder names: `boundaries`,
`property-and-land-use`, `parks-and-recreation`, `public-safety`,
`public-utilities`, `public-works`.

Public root:
`https://data.source.coop/portolan-mirrors/sandy-utah-catalog/catalog.json`

Every collection ships two data assets — a GeoParquet (`data` role) and a
PMTiles archive (`visual` role) — plus its own `README.md` and `AGENTS.md`.
Read the collection's own agent guide before querying it: that is where the
schema and the coded-value lists are.

## The projection, which is the most common way to get this wrong

**40 of the 42 collections are EPSG:3566**, NAD83(HARN) / Utah Central, in
**US survey feet**. This is what Sandy City publishes and it is deliberately
preserved rather than reprojected.

**Two are not, and assuming otherwise gives wrong distances:**

| Collection | `proj:epsg` | Linear unit |
| --- | --- | --- |
| `public-utilities/lead-service-lines` | 2850 | **metres** (same projection, metric) |
| `property-and-land-use/future-land-use` | 3857 | Mercator metres, not ground distance |

Both came from the city's ArcGIS Online organisation rather than its own
server, which is why they differ. **Read `proj:epsg` off the collection before
computing any length or area.** Do not assume the catalog is uniform.

Consequences:

- `ST_Length` and `ST_Area` return the collection's own unit, not metres by
  default.
- You cannot compare coordinates against a WGS84 dataset without transforming
  first.
- `ST_MakeEnvelope` with degree arguments will match nothing.

```sql
INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;

SELECT ST_Transform(geometry, 'EPSG:3566', 'EPSG:4326') AS geom_wgs84
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/parks-and-recreation/trails/trails.parquet'
LIMIT 5;   -- trails is 3566; check proj:epsg for the collection you query
```

The PMTiles are Web Mercator, because tiles have to be. Their asset carries
`proj:epsg: 3857`, which overrides the collection-level `proj:epsg` wherever
the two differ.

Every row carries a `bbox` struct column (`xmin`, `ymin`, `xmax`, `ymax`)
written by gpio for spatial pruning. It is in the collection's own CRS, like
the geometry.
Rows are in Hilbert order, so a bbox filter prunes row groups efficiently.

## Join keys

**`parcels` to `address-points`** — the capitalisation differs between the two
collections, which is the trap:

```sql
SELECT a.Address, p.parcel_id, p.parcel_acres
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/address-points/address-points.parquet' a
JOIN 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/parcels/parcels.parquet' p
  ON a.Parcel_Id = p.parcel_id;
```

Measured: `parcel_id` is unique in `parcels` (no duplicate values across
106,087 rows), and **54,000 of 60,400** address points join a parcel. The
other 6,400 do not, so use a left join if you need every address.

**`lead-service-lines` to `address-points`** — a string join on the address
text, so it needs normalising and it is lossy:

```sql
SELECT s.bothsidesstatus, s.utilmaterial, a.Parcel_Id
FROM 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/public-utilities/lead-service-lines/lead-service-lines.parquet' s
JOIN 'https://data.source.coop/portolan-mirrors/sandy-utah-catalog/property-and-land-use/address-points/address-points.parquet' a
  ON upper(trim(s.address)) = upper(trim(a.Address));
```

Measured: **22,597 of 26,213** service lines match an address point.

**Everything else joins spatially, not by key.** `zoning` carries no parcel
identifier — only `OBJECTID`, which is an Esri row number and is not stable
across refreshes. Never join on `OBJECTID` between collections.

## Quirks that produce silently wrong answers

- **`parcels` is current to July 2022**, per the upstream service's own
  description. It lags the Salt Lake County Recorder's live fabric by over
  three years. Do not present it as current ownership.
- **The lead service line inventory is mostly unresolved.** 18,992 of 26,213
  lines are `bothsidesstatus = 'Unknown'`; 7,221 are `Non-Lead`. There are
  **no** confirmed `Lead` rows. A map of this data shows where the city has
  not yet looked, not where lead is absent.
- **`zoning.Zone_Code` is null in all 454 rows.** Use `LEGEND_COD` or `ZONE`.
- **`fire-stations.Type` has dirty values**: `METRO` and `Metro` both occur,
  and one row reads `DFD\r\nDFD`. Normalise before grouping.
- **`OBJECTID` is not a stable identifier.** It is an Esri row number,
  reassigned on republish. It is kept because it is what the city publishes,
  not because it means anything.
- **Several collections extend well beyond Sandy.** `slco-city-borders`,
  `bus-stops`, `bus-routes`, `flood-100yr`, `fault-zones`, `landslide-risk`
  and `no-fireworks-zone` are regional layers. Clip to the city boundary if
  you want Sandy only.
- **Two datasets are published twice by the city.** The tree inventory appears
  as both `Grounds_and_Forestry` and `ParksDeptTrees`; hydrants appear under
  both Public Safety (5,047) and Public Utilities (5,292). This catalog
  mirrors one of each and says which.

## Columns that were removed

This mirror is not byte-identical to upstream. `Editor`, `Creator` and
`GlobalID` were dropped throughout; `EditDate` and `CreationDate` were kept.
Personal contact columns were dropped from `communities`, and `accountid` from
`lead-service-lines`. 31 rows with corrupt coordinates were dropped from
`street-trees`. Each collection's README lists what its own drops were.

## Licence

Sandy City publishes no licence. Every collection declares `other`. See the
[README](README.md) before redistributing.

## Structure

Data asset hrefs are absolute, because the bytes live on Source Cooperative
and are not in the metadata repository. Styles and documentation use relative
hrefs. The root catalog carries an absolute `self` link recording its
canonical location.
