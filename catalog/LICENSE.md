# Licence status

**Sandy City, Utah publishes no licence for this data.**

Every collection in this catalog therefore declares the SPDX identifier
`other`. This file is what the `rel: license` link on each collection points
at, because there is no upstream licence text to point at instead.

## What was checked

- `https://sandy.utah.gov/disclaimer` and `https://sandy.utah.gov/terms-of-use`
  both return HTTP 404.
- No layer on `gis.sandy.utah.gov/arcgis/rest/services` carries a licence
  statement. The services carry a `copyrightText` attribution string only,
  most commonly `Sandy City GIS`.
- No item in the city's ArcGIS Online organisation (`sandycity`,
  org id `IGYUtIzoA63tzE48`) carries a data licence. The only `licenseInfo`
  strings present are Esri's Apache-2.0 notice attached to the Lead Service
  Line solution templates, which licenses Esri's application code and not
  Sandy City's data.

## What that means

The data is a public record under the
[Utah Government Records Access and Management Act](https://le.utah.gov/xcode/Title63G/Chapter2/63G-2.html).
Utah has no statute placing municipal GIS output in the public domain, and the
city has granted no explicit reuse rights.

So: this data is public, and its reuse terms are **unconfirmed**. If you need
certainty, particularly for commercial use or redistribution, ask Sandy City
directly.

The statewide
[UGRC licence and disclaimer policy](https://gis.utah.gov/about/policy/license-disclaimer/)
applies CC BY 4.0 to UGRC's own data. It covers UGRC, not Sandy City, and does
not carry down to municipal data. It should not be assumed here.

## Attribution

Each collection records the attribution string its source service publishes.
Most read `Sandy City GIS`. The parcels collection reads
`Salt Lake County Recorder`, and the county-wide boundary collection reads
`AGRC`. Those strings are reproduced as the `producer` provider on each
collection.

## This catalog

This catalog is an independent mirror. It is not endorsed by or affiliated
with Sandy City. The metadata, documentation and styles written for it live in
[github.com/cholmes/sandy-utah-catalog](https://github.com/cholmes/sandy-utah-catalog)
and are offered under the repository's own licence. They do not extend any
grant over the underlying city data, which is not ours to license.

If Sandy City publishes licence terms, please
[open an issue](https://github.com/cholmes/sandy-utah-catalog/issues) so this can
be corrected.
