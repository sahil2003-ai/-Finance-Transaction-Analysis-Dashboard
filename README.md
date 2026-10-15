# Finance Transaction Analysis Dashboard

A transaction analytics project combining Python, SQL, and Power BI to profile transaction amounts, transaction types, merchants, timestamps, and recorded balances.

![Python](https://img.shields.io/badge/Python-Analysis-blue) ![SQL](https://img.shields.io/badge/SQL-Analytics-blue) ![Power%20BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)

## Contents
- [Overview](#overview)
- [Business Questions](#business-questions)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Results and Metrics](#results-and-metrics)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Run the Project](#run-the-project)
- [Limitations and Next Steps](#limitations-and-next-steps)

## Overview
This project explores transaction-level data with Python, SQL, and a Power BI dashboard. It demonstrates data profiling, descriptive statistics, grouped transaction analysis, and KPI validation across tools.

## Business Questions
- How are transaction amounts distributed?
- How do transaction types and merchants compare?
- What patterns appear across timestamps?
- Are SQL and dashboard summaries consistent with the source data?

## Dataset
Source file: `finance.csv`.

| Metric | Saved notebook output |
|---|---:|
| Rows | 50,000 |
| Columns | 7 |
| Missing values | 0 reported in each column |
| Distinct timestamps in summary | 50,000 |
| Transaction types | 2 |
| Merchants | 8 |
| Mean transaction amount | 4,990.46 |
| Minimum transaction amount | 5.02 |
| Maximum transaction amount | 9,999.36 |

The notebook output begins at `01-01-2018 00:00`; reconfirm the full date range by rerunning it. Currency is not established by repository evidence, so values are shown without a currency symbol. Clarify the meaning of the `Balance` field before interpreting it.

## Workflow
1. Load `finance.csv` and inspect schema and types.
2. Check missing values and descriptive statistics.
3. Inspect timestamp uniqueness and transaction distributions.
4. Run SQL aggregations and compare grouped results.
5. Refresh the Power BI report and reconcile its measures with the source data.

## Results and Metrics
Saved notebook output reports 50,000 rows, two transaction types, eight merchants, and transaction amounts from 5.02 to 9,999.36, with a mean of 4,990.46. These figures should be reconfirmed with a fresh notebook run. SQL outputs and the refreshed PBIX were not independently executed in this review. No fraud rate or financial impact is claimed.

## Technology Stack
- Python and pandas for profiling and EDA
- Jupyter Notebook for exploration
- SQL for transaction aggregations
- Power BI for dashboard reporting

## Repository Structure
```text
-Finance-Transaction-Analysis-Dashboard/
├── finance.csv
├── finance.ipynb
├── finance.sql
├── Finance Dashboard.pbix
└── README.md
```

## Run the Project
```bash
git clone https://github.com/sahil2003-ai/-Finance-Transaction-Analysis-Dashboard.git
cd -Finance-Transaction-Analysis-Dashboard
python -m venv .venv
```
Activate the environment and install pandas and the packages imported by the notebook. Then run `finance.ipynb`, load the CSV into a compatible SQL engine and run `finance.sql`, and open `Finance Dashboard.pbix` in Power BI Desktop.

## Limitations and Next Steps
- Confirm currency, full date range, dataset provenance, and license.
- Define the `Balance` field and transaction KPI formulas.
- Reconcile SQL and Power BI totals with the notebook.
- Add genuine dashboard screenshots and verified query outputs.
- Treat unusual transactions as candidates for investigation, not proof of fraud.

## Skills Demonstrated
Data profiling, descriptive statistics, SQL aggregation, transaction analysis, Power BI reporting, and cross-tool validation.

## Author
**Sahil Gaikwad** · [GitHub](https://github.com/sahil2003-ai) · [LinkedIn](https://www.linkedin.com/in/sahil-gaikwad-a76b7224a/)
