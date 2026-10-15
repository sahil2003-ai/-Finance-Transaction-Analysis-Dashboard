# Finance Transaction Analysis Dashboard

> A transaction analytics project combining Python, SQL, and Power BI to profile transaction amounts, transaction types, merchants, timestamps, and recorded balances.

![Python](https://img.shields.io/badge/Python-Analysis-blue)
![SQL](https://img.shields.io/badge/SQL-Analytics-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Features](#-features)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Workflow](#-project-workflow)
- [Repository Structure](#-repository-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Results and Insights](#-results-and-insights)
- [Screenshots](#-screenshots)
- [Challenges and Solutions](#-challenges-and-solutions)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [What I Learned](#-what-i-learned)
- [Author](#-author)
- [License](#-license)

## 📖 Overview

This project explores transaction-level data with Python, SQL, and a Power BI dashboard. It is designed to demonstrate data profiling, descriptive statistics, grouped transaction analysis, and dashboard KPI validation.

## 🎯 Problem Statement

Transaction datasets can contain large numbers of records and multiple transaction types or merchants. Reliable reporting requires checking data quality, understanding amount distributions, and making sure summary metrics agree across analytical tools.

## 🎯 Objectives

- Profile the transaction dataset and date/time fields.
- Summarize transaction amounts and categories.
- Use SQL to group and aggregate transactions.
- Compare notebook calculations with dashboard metrics.

## ✨ Features

- Data shape, data type, and missing-value inspection.
- Descriptive statistics for transaction amounts.
- Merchant and transaction-type comparisons.
- SQL query definitions and a Power BI dashboard.

## 📂 Dataset

Source file: `finance.csv`.

| Metric | Value from saved notebook output |
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

The notebook output begins at `01-01-2018 00:00`; the full date range and date parsing should be reconfirmed by rerunning the notebook. Currency is not established by repository evidence, so amounts are shown without a currency symbol. Clarify the meaning of `Balance` before interpreting it.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python / pandas | Data inspection and EDA |
| Jupyter Notebook | Reproducible exploration |
| SQL | Transaction aggregations |
| Power BI | Dashboard and KPI reporting |

## 🔄 Project Workflow

1. Load `finance.csv` and inspect schema and data types.
2. Check missing values and descriptive statistics.
3. Inspect timestamp uniqueness and transaction distributions.
4. Run SQL groupings and aggregations.
5. Refresh the Power BI report.
6. Reconcile shared metrics across tools.

## 🗂️ Repository Structure

```text
-Finance-Transaction-Analysis-Dashboard/
├── finance.csv
├── finance.ipynb
├── finance.sql
├── Finance Dashboard.pbix
└── README.md
```

## ⚙️ Installation

### Prerequisites

- Python and Jupyter Notebook
- A SQL engine compatible with the query script
- Power BI Desktop

### Setup

```bash
git clone https://github.com/sahil2003-ai/-Finance-Transaction-Analysis-Dashboard.git
cd -Finance-Transaction-Analysis-Dashboard
python -m venv .venv
```

Activate the environment, install pandas and the libraries imported by the notebook, then open the notebook. A root-level `requirements.txt` was not identified in the reviewed inventory.

## ▶️ Usage

- Run `finance.ipynb` from top to bottom with `finance.csv` at the expected path.
- Load the CSV into a SQL engine and run `finance.sql` after confirming its dialect and schema.
- Open `Finance Dashboard.pbix` in Power BI Desktop and verify its data source.

## 📊 Results and Insights

### Key Findings

The saved notebook output records 50,000 transaction rows, two transaction types, eight merchants, no missing values across the seven columns, and transaction amounts ranging from 5.02 to 9,999.36 with a mean of 4,990.46.

### Evaluation

These metrics are transcribed from saved notebook output and should be reconfirmed by rerunning the notebook. SQL result tables and the refreshed PBIX were not independently executed in this review. No fraud rate or financial impact is claimed. An unusual transaction should be treated as an investigation candidate, not proof of fraud.

## 🖼️ Screenshots

The repository includes the PBIX dashboard, but no independently verified screenshot was available in the audit. Add actual dashboard screenshots after refresh.

## 🧩 Challenges and Solutions

| Challenge | Approach |
|---|---|
| Currency is not documented | Avoid adding a currency symbol until source metadata confirms it |
| Timestamp fields can be parsed inconsistently | Validate date format and timezone during notebook rerun |
| Dashboard and SQL results may differ | Reconcile filters and KPI formulas across tools |

## ⚠️ Limitations

- Full date range, currency, and dataset provenance need confirmation.
- The interpretation of `Balance` is not established.
- Saved notebook metrics require a fresh run for independent confirmation.
- Anomaly analysis alone cannot establish fraud.

## 🚀 Future Improvements

- [ ] Document source URL, currency, and data dictionary.
- [ ] Add verified SQL result tables and dashboard screenshots.
- [ ] Define and validate transaction KPIs.
- [ ] Add anomaly detection only with a clear evaluation method.

## 📚 What I Learned

- Profiling a medium-sized transaction dataset.
- Using descriptive statistics and SQL aggregations.
- Reconciling financial-style metrics across Python and BI tools.
- Avoiding unsupported assumptions about currency and fraud.

## 👤 Author

**Sahil Gaikwad**

- GitHub: [sahil2003-ai](https://github.com/sahil2003-ai)
- LinkedIn: [Sahil Gaikwad](https://www.linkedin.com/in/sahil-gaikwad-a76b7224a/)

## 📄 License

The project license and dataset source/reuse terms should be checked in the repository before redistribution.
