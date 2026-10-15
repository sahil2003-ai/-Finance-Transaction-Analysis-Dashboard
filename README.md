# Finance Transaction Analysis Dashboard

A descriptive analytics project combining Python, SQL, and Power BI to examine transaction amounts, transaction types, merchants, dates, and recorded balances.

## Project components

| File | Purpose |
|---|---|
| `finance.csv` | Transaction-level dataset |
| `finance.ipynb` | Python data inspection and exploratory analysis |
| `finance.sql` | SQL query definitions |
| `Finance Dashboard.pbix` | Power BI dashboard |

## Verified dataset profile

The saved output in `finance.ipynb` reports the following for `finance.csv`:

| Check | Recorded result |
|---|---:|
| Rows | 50,000 |
| Columns | 7 |
| Missing values | 0 reported in every column |
| Distinct timestamps in the summary output | 50,000 |
| Transaction types | 2 |
| Merchants | 8 |
| Transaction amount mean | 4,990.46 |
| Transaction amount minimum | 5.02 |
| Transaction amount maximum | 9,999.36 |

The notebook records a date-time range beginning at `01-01-2018 00:00`; confirm date parsing and the complete date range by rerunning the notebook. Currency is not established by the repository evidence, so amounts are intentionally shown without a currency symbol.

## Analytical workflow

1. Load the CSV using pandas.
2. Inspect data types, missing values, descriptive statistics, and date-time fields.
3. Use SQL to calculate transaction counts and grouped transaction metrics.
4. Explore distributions and time trends in the notebook.
5. Review and refresh the Power BI report, then reconcile shared KPIs with Python/SQL outputs.

## Tech stack

Python, pandas, Jupyter Notebook, SQL, and Power BI.

## Reproduce

1. Install Python and Jupyter Notebook.
2. Install the packages imported by `finance.ipynb`.
3. Place `finance.csv` alongside the notebook or adjust the data path.
4. Run notebook cells from top to bottom.
5. Run `finance.sql` in a compatible SQL engine after loading the data.
6. Open `Finance Dashboard.pbix` in Power BI Desktop and verify its data source.

## Important interpretation notes

- The values above are taken from saved notebook output; rerun the notebook to validate against the current CSV.
- The SQL file defines analysis, but its final aggregate outputs were not independently confirmed in this review.
- Clarify whether `Balance` represents a post-transaction balance or another measure before interpreting it.
- An unusual transaction is not automatically fraud. Treat anomalies as candidates for investigation, not a conclusion.
- Document the dataset source, currency, and reuse terms before presenting the project as production financial analysis.

## Portfolio skills

Data profiling, missing-value checks, descriptive statistics, SQL aggregations, cross-tool KPI validation, and dashboard communication.

## Author

Sahil Gaikwad · [GitHub](https://github.com/sahil2003-ai) · [LinkedIn](https://www.linkedin.com/in/sahil-gaikwad-a76b7224a/)
