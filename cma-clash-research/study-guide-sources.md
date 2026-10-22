# Study guide sources

The study guides in `classquiz/seed/study_guides.py` cover every topic in the
catalog (`classquiz/seed/catalog.py`) — 45 topics across the NHA CCMA, EKG
technician, phlebotomy, CPR/BLS and clinical-skills certifications.

Each guide is a list of blocks. A block has:

| field     | purpose                                                        |
| --------- | -------------------------------------------------------------- |
| `title`   | the section heading shown on the study page                     |
| `summary` | a short paragraph (80–1200 characters) of the key content       |
| `bullets` | optional key points rendered as a list                          |
| `source`  | human-readable name of the official source                      |
| `url`     | a deep link to the source                                       |

## Source policy

Only official health-care sources are used:

- **Government agencies** — CDC (infection control, immunization, disease
  guidance, NIOSH worker safety), OSHA (bloodborne pathogens, PPE,
  ergonomics, hazard communication), FDA (drug safety, medication errors,
  CLIA waived testing, MedWatch), HHS (HIPAA Privacy and Security Rules),
  eCFR (the regulation text itself), NIH institutes and NLM/MedlinePlus,
  CMS/Medicare/Medicaid, AHRQ (care coordination, health literacy, patient
  safety, TeamSTEPPS) and the US Preventive Services Task Force.
- **Standards bodies and authorities** — CLSI (GP41/PRE02 venipuncture),
  the American Heart Association (CPR and ECC guidelines and algorithms), the
  American Red Cross, WHO (injection safety, hand hygiene, phlebotomy), the
  American Diabetes Association (Standards of Care) and the AMA Code of
  Medical Ethics.
- **The certifying body** — NHA (CCMA/CET/CPT certification pages).

`classquiz/seed/sources.py` holds the canonical list of links. The allowlist of
permitted domains is `OFFICIAL_SOURCE_DOMAINS` in the same module, and
`classquiz/tests/test_study_guides.py` enforces it:

- every catalog topic has a guide,
- every guide has at least four sections with substantive summaries,
- every section links to an allow-listed official domain over HTTPS,
- the source label matches the linked host,
- the library as a whole spans a broad set of official hosts.

## Link verification

All links were checked against the live sites (HTTP status and page title)
while the library was written. A few notes for future maintainers:

- `cdc.gov`, `hhs.gov` and `redcross.org` block scripted requests, so those
  links have to be verified in a real browser.
- CDC moved its vaccine pages: the old `/vaccines/hcp/admin/...` paths now
  return 404. The current locations are `/vaccines/hcp/administration/` and
  `/vaccines/hcp/storage-handling/`.
- CLSI renamed GP41 to PRE02; `https://clsi.org/shop/standards/pre02/` is the
  current product page, and the GP41 sample pages remain at
  `https://clsi.org/media/1372/gp41ed7_sample.pdf`.
- The old FDA links (`/drugs/medication-safety-program`,
  `/medical-devices/ivd-regulatory-assistance/clia-waived-tests`) are gone;
  use the drug-safety hub and the CLIA pages under `accessdata.fda.gov`.

## Storage

`topics.study_content` is a JSON column (see
`migrations/versions/b2c3d4e5f6a7_topic_study_content.py`). The seed writes
it from `STUDY_BY_TOPIC` on every deploy, so content updates ship with the
code.

The API serializes the guides through `StudyBlockOut` in
`classquiz/routers/clash.py`. `source` and `bullets` are optional so that rows
seeded before this expansion still serialize.
