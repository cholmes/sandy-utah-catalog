#!/usr/bin/env python3
"""Refuse to publish a column that looks like personal contact data.

This exists because a sweep run by hand is a step, and a step gets skipped.
The first privacy pass on this catalog ran over 42 collections and caught
twelve contact columns on `communities`. Twenty-eight collections were added
later and the sweep was never repeated, so `neighborhood-watch` reached the
published catalog carrying home addresses, email addresses and four
telephone numbers for named resident volunteers.

Two passes, because either alone misses real cases:

  by name   a column whose name suggests a personal channel
  by value  a column whose VALUES look like emails or telephone numbers,
            whatever the column is called

A facility telephone number is not personal data, and a parcel's owner name
is public record under the county recorder. Those live in ALLOWED, each with
the reason it is there. Adding a name to that list is a decision about
publishing someone's data, so it needs a reason a reader can weigh.

Run: python3 tests/test_no_pii.py
It checks the GeoParquet named by each collection's `data` asset. Where the
data is not on disk, it checks the declared `table:columns` instead, which
still catches a name-based hit in CI.
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
def _data_dir() -> Path:
    """Where the staged GeoParquet lives, from the publish config.

    Reading data_dir rather than guessing a path keeps this in step with
    tools/upload_data.py. A guess silently checks nothing, which is how a
    gate passes while finding no data at all.
    """
    override = os.environ.get("PII_DATA_DIR")
    if override:
        return Path(override)
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        from publish import load_config
        configured = (load_config() or {}).get("data_dir")
    except Exception:
        configured = None
    if not configured:
        return ROOT / "_no_data_dir_configured"
    p = Path(configured)
    return p if p.is_absolute() else (ROOT / p).resolve()


DATA = _data_dir()

NAME_PAT = re.compile(
    r"(phone|email|e_mail|mobile|cell|contact|resident|occupant"
    r"|leader|birth|dob|ssn|account)",
    re.I,
)
# Search, not fullmatch. A telephone number hides inside a free-text note,
# and an anchored pattern cannot see it. Sixty-nine were sitting in the
# cemetery register's Comments field alongside the names of living
# relatives, under a whole-value check that reported one.
EMAIL_VAL = re.compile(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}")
PHONE_VAL = re.compile(r"(?<!\d)(?:1[-.\s])?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}(?!\d)")

# column -> why publishing it is acceptable
ALLOWED = {
    "Phone": "Facility telephone number for a park or golf course, not a person.",
    "Telephone": "Fire station telephone number, not a person.",
    "Mortuary_Phone": "Business number of a mortuary in the burial register.",
    "Monument_Co_Phone": "Business number of a monument company.",
    "Burial_Receipt_Num": "Receipt number. Some values match a phone pattern.",
    "BIRTH_MO": "Burial register field. Cemetery registers are public record.",
    "BIRTH_DAY": "Burial register field.",
    "BIRTH_YEAR": "Burial register field.",
    "BirthDate": "Burial register field.",
    "Birthplace": "Burial register field.",
    "AreaLeader": "Name of a neighbourhood watch leader, a civic role the "
                  "city publishes. Their contact details are dropped.",
    "LEADER_NAME": "Name of a community council chair, a civic role the city "
                   "publishes. Their contact details are dropped.",
    "EMERGENCY_PREPAREDNESS_LEADER": "Name in a civic role; contacts dropped.",
    "EMERGENCY_PREPAREDNESS_LEADER2": "Name in a civic role; contacts dropped.",
    "Council_Member": "Elected official, published by the city.",
    "own_name": "Property owner of record. Public record under the Salt Lake "
                "County Recorder, and kept out of the vector tiles.",
    "care_of": "Care-of line on an owner's mailing address. Public record.",
    "own_addr": "Owner's mailing address. Public record.",
    "own_apt_num": "Part of the owner's mailing address. Public record.",
    "own_citystate": "Part of the owner's mailing address. Public record.",
    "own_country_code": "Part of the owner's mailing address. Public record.",
    "own_zip": "Part of the owner's mailing address. Public record.",
    "own_zip_four": "Part of the owner's mailing address. Public record.",
    "contact": "Organisation contact, not a person.",
    "CH2MCELL": "Grid cell in a consultant's groundwater model. Not a phone.",
    "Snowmobile": "Trail use flag. Matches on 'mobile'.",
    "Prop_Subtype": "Property type classification.",
    "Legal_Description": "Recorded legal description. Its book-page "
                         "references, such as 7184-811-813, match a "
                         "telephone pattern and are not telephone numbers.",
}

findings: list[str] = []


def check_values(where, name, values):
    vals = [v for v in values if v not in (None, "", " ")][:3000]
    emails = sum(1 for v in vals if EMAIL_VAL.search(str(v)))
    phones = sum(1 for v in vals if PHONE_VAL.search(str(v)))
    hits = []
    if emails:
        hits.append(f"{emails} email values")
    if phones:
        hits.append(f"{phones} telephone values")
    if hits and name not in ALLOWED:
        findings.append(f"{where}: `{name}` holds {', '.join(hits)}")


def main() -> int:
    collections = sorted(CATALOG.glob("*/*/collection.json"))
    if not collections:
        print("no collections to check")
        return 0

    try:
        import pyarrow.parquet as pq
    except ImportError:
        pq = None

    checked_data = 0
    for path in collections:
        doc = json.loads(path.read_text())
        where = f"{path.parent.parent.name}/{path.parent.name}"

        declared = [c["name"] for c in doc.get("table:columns") or []]
        for name in declared:
            if NAME_PAT.search(name) and name not in ALLOWED:
                findings.append(
                    f"{where}: `{name}` reads as personal contact data. "
                    f"Drop it, or add it to ALLOWED with the reason.")

        parquet = DATA / where / f"{path.parent.name}.parquet"
        if pq is None or not parquet.is_file():
            continue
        checked_data += 1
        table = pq.read_table(parquet)
        for name in table.schema.names:
            if not str(table.schema.field(name).type).startswith("string"):
                continue
            check_values(where, name, table[name].to_pylist())

    scope = (f"{len(collections)} collections, {checked_data} with data on disk")
    if findings:
        print(f"Personal contact data found in {scope}:\n")
        for f in sorted(set(findings)):
            print(f"  error  {f}")
        print("\nA column belongs in ALLOWED only with a reason a reader can "
              "weigh. See tests/test_no_pii.py.")
        return 1

    print(f"OK: no unreviewed personal contact data ({scope})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
