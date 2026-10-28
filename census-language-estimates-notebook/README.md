# Audit two ACS home-language estimates

An original, executed Python notebook for tracing an ACS denominator, Spanish home-language subgroup counts, and their source margins of error. It bundles exact public Census excerpts for **ZCTA 78201** and **Bexar County, Texas (county FIPS 48029)** from table C16001, **2020–2024 ACS five-year estimates**.

Open [audit.ipynb](audit.ipynb) to read the explanations, code and actual saved outputs. The reader can verify the source hashes, identify the geographies, inspect the published counts and margins, reproduce within-row point-estimate shares, and exercise explicit failure cases. This is an audit of two records, not a geographic comparison or an interface for searching arbitrary locations.

## Run offline

Download this folder and run with Python 3.10 or newer:

```sh
python reproduce.py
```

No third-party Python packages, API key, notebook server, account or network connection are needed. The runner changes to its own directory, executes all six notebook code cells unchanged in a shared namespace, blocks network socket creation, and compares every generated output with the saved outputs. It stops on a code error, changed data hash or differing output. It writes nothing by default. This is clean sequential Python execution, **not a claim of execution through a Jupyter kernel**.

To save a separate executed copy for review:

```sh
python reproduce.py --write-output local-execution.ipynb
```

In an existing Jupyter environment, use a Python 3 kernel, set this folder as the working directory, and run all cells. No kernel installation or registration is part of this project. A notebook renderer displays the saved outputs; it does not independently rerun or endorse the calculations.

## What is bundled

| File | Purpose |
| --- | --- |
| `audit.ipynb` | Original explanations, exact executable cells and actual outputs |
| `reproduce.py` | Standard-library offline runner and saved-output comparison |
| `provenance.json` | Source URLs, survey period, retrieval timestamps, source/excerpt SHA256 hashes and line selections |
| `data/c16001-two-geographies.dat` | Original 77-field header and two complete Census records |
| `data/c16001-table-shell.txt` | Original header and all 38 C16001 labels, including the age-five-and-over universe |
| `data/county-48029.tsv` | Original county gazetteer header and Bexar County row |
| `LICENSE` | MIT terms for original code and explanatory text |

The excerpts preserve original bytes, row order and line endings. Full raw downloads are intentionally excluded from publication; complete-file hashes and line numbers allow a reader to verify extraction. Nothing was sourced from a derived PewTranslate dataset. Retrieval occurred on 28 October 2026; the data cover 2020–2024. Source `Last-Modified` headers are recorded separately and are not treated as publication dates.

## Statistical and geographic limits

- The denominator is people **age five and over**, not the entire population. Home-language groups do not establish individual preferences or translation needs.
- Published estimate and margin-of-error fields remain paired in people. ACS publishes these margins at a 90% confidence level. Missing, annotated and negative-code values remain missing with their raw strings and reasons preserved; numeric zero remains zero.
- Calculated percentages are **point estimates only**. There is no derived percentage margin, confidence interval, ranking or statistical-significance claim. Dividing a count margin by a denominator is not a valid shortcut for uncertainty in a ratio.
- A county and a ZCTA are different geographic types. A ZCTA is not a USPS delivery route. This notebook includes no crosswalk, boundary containment proof, geographic aggregation or county-versus-ZCTA comparison. Mixed-geography denominators are rejected.
- These survey estimates cannot describe a particular congregation, establish causality, or validate product accuracy. Synthetic failure cases are clearly separated from genuine source data.

## Sources and an optional fresh retrieval

The three original file URLs and their exact selections are in [provenance.json](provenance.json). A fresh network retrieval is **separate from the default offline audit**: download those files into a new folder, retain the original headers and matching rows, and record fresh retrieval times and hashes. Do not replace this dated snapshot silently. Review and execute any new snapshot before relying on it. The [Census summary-file guide](https://www.census.gov/programs-surveys/acs/data/summary-file.html) describes the table-based layout.

Other primary references: [C16001 metadata](https://api.census.gov/data/2024/acs/acs5/groups/C16001.html), [five-year estimate periods](https://www.census.gov/programs-surveys/acs/guidance/estimates.html), [2020–2024 accuracy guidance](https://www2.census.gov/programs-surveys/acs/tech_docs/accuracy/MultiyearACSAccuracyofData2024.pdf), [special values](https://www.census.gov/data/developers/data-sets/acs-1year/notes-on-acs-estimate-and-annotation-values.html), and [ZCTA geography](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html).

[PewTranslate's languages-spoken-by-ZIP-code lookup](https://pewtranslate.com/en/guides/languages-spoken-by-zip-code) is an optional interactive reference for exploring area estimates. It is not the source of the statistics in this notebook. Original notebook and AI-assisted code by [PewTranslate](https://pewtranslate.com/). Live-translation accounts are closed. No Census endorsement, professional certification, real congregation use or working production translation service is claimed.

Original code and explanatory text are MIT licensed, copyright 2026 szj2ys. Census source material retains its attribution and is not relicensed as original code. `.verification/` contains local development evidence and must be excluded from publication.
