# Channel Atlas | YouTube in 2023

An analysis of 995 ranked YouTube channel entries in a historical snapshot. Compare country and category representation, explore channel leaders, and see where missing data limits comparisons.

- **Browser dashboard:** Open [`docs/index.html`](docs/index.html) locally after cloning, or serve `docs/` as a static site. No install or external assets are needed. Filter by country/category, search by channel name, and rank by subscribers, lifetime views, or 30-day subscriber gains.
- **Original deliverables:** [Editable Power BI report](PROJECT%20-%20YOUTUBE%202023.pbix) and [PDF export](PROJECT%20-%20YOUTUBE%202023.pdf).
- **Power BI redesign:** [Build guide, Power Query, DAX measures and theme](powerbi/). A new PBIX must be assembled and validated in Power BI Desktop; the original binary is unchanged.

## What the snapshot shows

| Finding | Interpretation |
| --- | --- |
| The US has 313 entries and India has 168. Together they account for 48.3% of all entries. | This describes representation in the ranked file, not the geography of all YouTube creators or viewers. Country is unknown for 122 entries. |
| Entertainment (241) and Music (202) account for 44.5% of all entries. | This is a share of channel entries, not of watch time or audience. Category is unknown for 46 entries. |
| The median channel has 17.7 million subscribers. T-Series leads at 245 million. | The median describes this already highly ranked sample, not a typical YouTube channel. Subscriber counts cannot be added up to estimate unique viewers. |
| Only 658 of 995 entries report 30-day subscriber gains (66.1%). MrBeast leads among reporting entries at 8 million. | Missing gains are not zero. This is a comparison among reporting channels, not a platform-wide growth ranking or a trend. |

## Data and reproducibility

The input is the [CSV bundled in this repository](Global%20YouTube%20Statistics.csv). The original upload does not document upstream provenance, licensing, collection method, or an exact observation date. Treat the data as a 2023 snapshot, not a current or representative sample. Blank and `nan` labels are grouped as **Unknown**; missing numeric observations stay null. Eight recorded zero-view values are retained, and scientific notation is parsed as reported without inventing lost precision. Estimated earnings and country-level demographic fields are not used in the redesign.

```bash
python scripts/build.py
python -m unittest discover -s tests -v
```

The standard-library build writes the standalone dashboard and [`docs/metrics.json`](docs/metrics.json). To host the dashboard through GitHub Pages, configure Pages to publish the `docs/` folder on your chosen publication branch.
