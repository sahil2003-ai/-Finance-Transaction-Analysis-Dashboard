# Finance Transaction Analysis Dashboard

> SQL, Python, and Power BI project for exploring transaction activity, cash movement, and potential anomalies.

![Status](https://img.shields.io/badge/Status-Portfolio--Project-blue)

## 📌 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Objectives](#objectives)
- [Features](#features)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Workflow](#project-workflow)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Results and Insights](#results-and-insights)
- [Screenshots](#screenshots)
- [Challenges and Solutions](#challenges-and-solutions)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [What I Learned](#what-i-learned)
- [Author](#author)
- [License](#license)

## 📖 Overview

SQL, Python, and Power BI project for exploring transaction activity, cash movement, and potential anomalies. This README documents the intended workflow and the files available in the repository. Verify all outputs against the current code and data before using them as evidence.

## 🎯 Problem Statement

Financial transaction data needs consistent definitions and validation before totals or unusual activity can be interpreted.

## 🎯 Objectives

- Validate transaction data and calculations.
- Summarize activity with SQL and Python.
- Present key measures in Power BI.

## ✨ Features

- CSV source file and SQL analysis.
- Python notebook for EDA.
- Power BI dashboard in PBIX format.

## 📂 Dataset

The saved notebook confirms **50,000 rows × 7 columns** in `finance.csv`. Its saved `df.info()` and missing-value output report 50,000 non-null values per column and zero missing values.

- **Fields:** `TransactionID`, `CustomerID`, `TransactionDate`, `Amount`, `TransactionType`, `Merchant`, and `Balance`.
- **Source/license:** Document the original dataset source and usage terms.
- **Privacy:** Avoid publishing customer identifiers or sensitive transaction-level records.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| SQL | Transaction queries and KPIs |
| Python/pandas | Data cleaning and EDA |
| Power BI | Dashboard |
| Jupyter Notebook | Analysis workflow |

## 🔄 Project Workflow

1. Inspect finance.csv and identify transaction, date, amount, type, and status fields.
2. Check missing values, duplicate IDs, date types, and unusual amounts.
3. Review finance.sql and confirm the database dialect and KPI formulas.
4. Run finance.ipynb and compare key totals with SQL results.
5. Open Finance Dashboard.pbix and validate the source and measures.
6. Document any anomaly rule and check false positives before interpreting flagged transactions.

## 🗂️ Repository Structure

```text
-Finance-Transaction-Analysis-Dashboard/
├── finance.csv
├── finance.ipynb
├── finance.sql
└── Finance Dashboard.pbix
└── README.md
```

The list above highlights known project files and folders; inspect the repository for the complete current structure.

## ⚙️ Installation

### Prerequisites

- Install the tools listed in the Tech Stack that apply to this project.
- For Python projects, use a Python version compatible with the dependencies actually imported by the code.
- For Power BI projects, use Power BI Desktop.

### Setup

Requires a SQL database compatible with finance.sql, Python/Jupyter for finance.ipynb, and Power BI Desktop for the dashboard. Confirm notebook imports before installing packages.

Do not run generic commands that do not match the files in this repository. Confirm the data paths, database dialect, and package versions before execution.

## ▶️ Usage

Run the SQL queries and notebook after configuring data paths/database; open the PBIX in Power BI Desktop.

## 📊 Results and Insights

### Verified dataset checks from saved notebook output

| Check | Recorded result |
|---|---:|
| Rows | 50,000 |
| Columns | 7 |
| Missing values | 0 across all seven columns |

### SQL analysis available

The SQL file defines queries for total rows, total transaction amount, credit/debit totals, average transaction amount by type, top merchants, top customers, and monthly totals.

The SQL file does not contain saved result values, so total amount and merchant rankings are not reported as verified findings. Execute the queries against the current CSV and validate date parsing and amount semantics before adding figures.

## 🖼️ Screenshots

No image files were confirmed for this repository during this update. If you have screenshots, upload them into an `images/` folder, then embed each real path here with a short caption. Do not use placeholder image paths.

## 🧩 Challenges and Solutions

| Challenge | Solution / validation approach |
|---|---|
| Reconciliation across tools | Compare shared KPIs across SQL, Python, and Power BI. |
| Potential anomaly interpretation | Describe the rule and avoid calling an alert confirmed fraud. |

## ⚠️ Limitations

- Row count and missing-value results come from saved notebook output; rerun to confirm the current CSV.
- Financial aggregate values were not saved in the SQL file.
- Confirm whether `Balance` is transaction-level or post-transaction balance before interpreting it.
- An unusual-transaction flag is not proof of fraud.

## 🚀 Future Improvements

- [ ] Document dataset provenance and schema.
- [ ] Add dashboard screenshots and exact KPI formulas.
- [ ] Add reproducible setup and data-quality checks.

## 📚 What I Learned

- Cross-tool KPI validation.
- Careful interpretation of financial anomalies.

## 👤 Author

**Sahil Gaikwad**

- GitHub: [sahil2003-ai](https://github.com/sahil2003-ai)
- LinkedIn: [Sahil Gaikwad](https://www.linkedin.com/in/sahil-gaikwad-a76b7224a/)

## 📄 License

Check data rights and repository license; avoid exposing sensitive data.
