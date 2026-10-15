# Finance Transaction Analysis Dashboard

An analytics portfolio project combining SQL, Python, and Power BI to explore transaction flows, cash movement, balance trends, and potential anomalies in financial transaction data.

## Project Overview
The project is designed to help users inspect transaction activity and summarize financial patterns through query-based analysis and dashboard reporting.

## Analytical Areas
- Credits, debits, and net cash movement
- Transaction trends over time, including rolling averages where implemented
- Customer and merchant-level summaries
- Balance movement and transaction-status analysis
- Potentially suspicious transactions, subject to a clearly documented rule or model

**Important:** A flagged transaction is not proof of fraud. Any anomaly or fraud-related claim should include the detection rule, evaluation method, and limitations.

## Tools
- SQL (document the exact database dialect)
- Python and Jupyter Notebook
- Power BI

## Repository Contents
The current README documents these main files:
- `finance.csv` — transaction dataset
- `finance.ipynb` — Python analysis and EDA
- `finance.sql` — SQL queries and KPIs
- `Finance Dashboard.pbix` — Power BI report

## How to Review
1. Inspect the CSV columns and data types.
2. Review the notebook for cleaning, calculations, and validation.
3. Run the SQL queries in the documented database environment.
4. Open the Power BI file and verify its data source and measures.

## Skills Demonstrated
Transaction analytics, SQL, data cleaning, financial KPI design, rolling-window analysis, dashboarding, and communicating data limitations.

## Recommended Improvements
- Add a data dictionary and dataset provenance.
- Define the transaction balance and net-position calculations.
- Document any anomaly detection logic and its false-positive limitations.
- Add dashboard screenshots and verified findings.
- Never publish real account identifiers or sensitive financial information.

> This is an analytics project, not a financial auditing or fraud-certification system.