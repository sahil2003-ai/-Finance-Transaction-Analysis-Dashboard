# Finance Transaction Analysis Dashboard

An end-to-end transaction analytics project using **Python, SQL and Power BI** to profile transaction amounts, compare credit and debit activity, rank merchants, explore monthly trends, and build a foundation for financial reporting.

<p align="left">
  <img src="https://img.shields.io/badge/Python-pandas%20%7C%20EDA-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/SQL-Transaction%20Analytics-336791?logo=mysql&logoColor=white" alt="SQL" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white" alt="Jupyter Notebook" />
</p>

## Project overview

This project analyzes a synthetic-style transaction table at row level and aggregates financial activity by transaction type, merchant, customer and month. It demonstrates data profiling, exploratory data analysis, SQL aggregation and a Power BI reporting artifact.

The analysis is descriptive: it identifies patterns in the supplied data but does not classify fraud, establish customer behavior in the real world, or establish financial performance for a real organization.

## Project files

| File | Purpose |
|---|---|
| [`finance.csv`](finance.csv) | Source transaction dataset |
| [`finance.ipynb`](finance.ipynb) | Data quality checks, descriptive analysis and charts |
| [`finance.sql`](finance.sql) | SQL queries for transaction and merchant summaries |
| [`Finance Dashboard.pbix`](Finance%20Dashboard.pbix) | Power BI dashboard artifact |

## Dataset

The source CSV contains **50,000 rows and 7 columns**. The saved notebook profile reports no missing values in the seven fields.

| Dataset metric | Value |
|---|---:|
| Transaction records | 50,000 |
| Columns | 7 |
| Missing cells in notebook profile | 0 |
| Distinct transaction timestamps | 50,000 |
| Transaction types | 2 |
| Merchants | 8 |
| Unique customers | 5,000 |
| Average transaction amount | 4,990.46 |
| Median transaction amount | 4,984.16 |
| Minimum transaction amount | 5.02 |
| Maximum transaction amount | 9,999.36 |
| Average recorded balance | 29,958.72 |
| Minimum recorded balance | 8.31 |
| Maximum recorded balance | 136,235.43 |

**Data interpretation:** the dataset does not establish a currency symbol, the business meaning of the `Balance` field, or whether each row is a real-world bank transaction. Therefore, values are shown without a currency symbol and the analysis should be treated as a sample/project dataset unless its provenance confirms otherwise.

### Column guide

| Column | Description |
|---|---|
| `TransactionID` | Transaction row identifier |
| `CustomerID` | Customer identifier |
| `TransactionDate` | Recorded timestamp |
| `Amount` | Transaction amount |
| `TransactionType` | Credit or Debit |
| `Merchant` | Merchant / transaction destination label |
| `Balance` | Recorded balance field; interpretation requires source documentation |

The notebook converts `TransactionDate` into a datetime field and creates a `YearMonth` field for monthly aggregation.

## Key results

The metrics below are taken from the notebook's saved outputs and descriptive summaries.

### Credit vs. debit amount totals

| Transaction type | Total amount |
|---|---:|
| Credit | 125,669,700 (approx.) |
| Debit | 123,853,300 (approx.) |
| **Combined total** | **249,523,000 (approx.)** |

The totals are rounded here from the saved notebook output. Recalculate from the CSV if exact cents are required for a report or audit.

### Top merchants by total transaction amount

| Rank | Merchant | Total amount |
|---:|---|---:|
| 1 | Apple Store | 31,565,526.87 |
| 2 | BestBuy | 31,501,575.91 |
| 3 | Netflix | 31,468,690.96 |
| 4 | Target | 31,318,329.67 |
| 5 | Starbucks | 31,210,662.65 |
| 6 | Walmart | 31,021,830.39 |
| 7 | Amazon | 30,771,627.18 |
| 8 | Uber | 30,664,762.88 |

The merchant totals are close to one another relative to their scale. These values are total transaction amounts, not merchant profit, revenue, or net cash flow.

### Monthly transaction trend

The notebook groups amount totals by month. The saved output reports **72 monthly periods** from January 2018 through December 2023. Example totals include:

| Month | Total transaction amount |
|---|---:|
| January 2018 | 1,428,860.37 |
| February 2018 | 1,492,623.77 |
| March 2018 | 1,446,928.03 |
| November 2023 | 1,037,781.42 |
| December 2023 | 991,704.62 |

These are the totals shown in the existing notebook output. Confirm the date parser and full period range when re-running the analysis.

## Exploratory analysis and visualizations

The notebook generates the following charts:

- Transaction amount distribution histogram
- Total transaction amount by type (credit vs. debit)
- Top merchants by total transaction amount
- Monthly transaction amount trend

These visuals help inspect amount distribution, compare group totals and review changes over time.

### Images available in the repository

The repository currently contains the CSV, notebook, SQL file and Power BI `.pbix` file, but it does **not** contain a separate `images/` folder or exported screenshots. The visuals are notebook outputs, not standalone image files, so I have not embedded fabricated images.

To show the actual Power BI report in this README, export genuine screenshots from Power BI Desktop into an `images/` directory and then reference those images here.

## SQL analytics

SQL file: [`finance.sql`](finance.sql)

The script includes queries for:

- Total number of records
- Overall transaction amount
- Amount totals by credit/debit type
- Average transaction amount by type
- Top merchants by total amount
- Customers ranked by transaction count and total amount
- Monthly total transaction amount

**SQL setup note:** the script uses `CREATE DATABASE` and `USE finance` statements, which are MySQL-style, and expects a transaction table named `finance`. Import the CSV to a compatible database/table before executing the queries. The monthly query extracts year/month parts from the string date, so verify that all source dates use the expected `DD-MM-YYYY HH:MM` format.

The numeric results in this README are based on saved notebook outputs. The SQL script was not independently executed against a live database during this review, and the Power BI report was not refreshed or reconciled against the CSV.

## Power BI dashboard

Dashboard file: [`Finance Dashboard.pbix`](Finance%20Dashboard.pbix)

The `.pbix` file is included for interactive review in Power BI Desktop. After opening it, confirm its data source and refresh the report. Reconcile card totals and chart values with the CSV and notebook using the same filters and calculation definitions.

## Workflow

```text
finance.csv
   │
   ├── Python / pandas
   │      ├── Shape, data types and missing-value checks
   │      ├── Descriptive statistics
   │      ├── Credit/debit totals
   │      ├── Merchant rankings
   │      └── Monthly trend chart
   │
   ├── SQL queries
   │      ├── Global totals
   │      ├── Type and merchant aggregations
   │      ├── Customer rankings
   │      └── Monthly aggregation
   │
   └── Power BI
          └── Interactive financial transaction report
```

## Repository structure

```text
-Finance-Transaction-Analysis-Dashboard/
├── finance.csv
├── finance.ipynb
├── finance.sql
├── Finance Dashboard.pbix
└── README.md
```

## Run the project

### 1. Clone the repository

```bash
git clone https://github.com/sahil2003-ai/-Finance-Transaction-Analysis-Dashboard.git
cd -Finance-Transaction-Analysis-Dashboard
```

### 2. Create an environment and install Python dependencies

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\\Scripts\\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install the libraries imported by the notebook:

```bash
pip install pandas matplotlib seaborn jupyter
```

### 3. Run the notebook

```bash
jupyter notebook finance.ipynb
```

Keep `finance.csv` in the repository root and run the notebook cells in order.

### 4. Run SQL

Create or select a compatible database, import the CSV into a table named `finance`, review the SQL dialect and date format, then execute `finance.sql`.

### 5. Open Power BI

Open `Finance Dashboard.pbix` in Power BI Desktop, confirm the source path, refresh the data and reconcile the key metrics against the CSV.

## Limitations and next steps

- **Currency and source:** document data provenance, licensing and amount units.
- **Balance definition:** clarify whether `Balance` is a running balance, account snapshot or independently generated value; do not assume it represents transaction amount plus/minus a running account balance.
- **Timestamp semantics:** confirm why every timestamp is distinct and whether records are hourly, generated or actual transactions.
- **Cross-tool validation:** reconcile Python, SQL and Power BI measures under the same filters.
- **Visual evidence:** add real Power BI screenshots and exported notebook charts to an `images/` folder.
- **Data integrity:** test duplicate transaction IDs, date parsing and amount ranges.
- **Interpretation:** unusual amounts or merchant patterns are descriptive flags for investigation, not proof of fraud.
- **Reproducibility:** include package versions and document the import/setup sequence for SQL.

## Skills demonstrated

Python · pandas · data profiling · exploratory data analysis · descriptive statistics · SQL aggregation · customer and merchant analysis · time-series grouping · Power BI dashboarding · cross-tool validation · business reporting

## Author

**Sahil Gaikwad**  
[GitHub](https://github.com/sahil2003-ai) · [LinkedIn](https://www.linkedin.com/in/sahil-gaikwad-a76b7224a/)
