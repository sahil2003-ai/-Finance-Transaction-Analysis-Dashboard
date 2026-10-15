# Finance Transaction Analysis Dashboard

A project combining SQL, Python, and Power BI to explore transaction activity, cash movement, customer/merchant patterns, and potential anomalies.

## Step-by-step workflow

1. **Inspect the files** — review `finance.csv`, `finance.ipynb`, `finance.sql`, and `Finance Dashboard.pbix`.
2. **Understand the schema** — check transaction ID, date, customer, merchant, amount, transaction type, and balance/status fields.
3. **Validate data quality** — inspect data types, missing values, duplicate transaction IDs, negative amounts, and date coverage.
4. **Run SQL analysis** — calculate transaction counts, credits/debits, net movement, and customer/merchant summaries supported by the SQL file.
5. **Explore in Python** — follow the notebook's cleaning and EDA steps and reconcile key totals with SQL.
6. **Review Power BI** — open the PBIX, confirm its data source, and inspect filters, KPIs, and rolling calculations.
7. **Investigate anomalies carefully** — document the exact rule used to flag unusual activity and check false positives.
8. **Report findings** — add verified insights, definitions, and practical follow-up questions.

## Tools
SQL, Python, pandas, Jupyter Notebook, Power BI.

## Screenshots
No separate image files were found in the repository root. Add dashboard screenshots in `images/` and embed them here.

## Safety and interpretation
A suspicious-transaction flag is not proof of fraud. Do not publish sensitive financial identifiers.

## Next improvements
Add dataset provenance, setup instructions, KPI definitions, screenshots, and reproducible findings.