# 💰 Finance Transaction Analysis & Dashboard

This project provides end-to-end financial transaction analysis, combining SQL, Python, and Power BI for insights into inflows, outflows, credit, debit, and customer balances. It also includes fraud detection insights and visual dashboards.

📂 Project Structure

├── finance.csv          # Raw dataset of transactions (Amount, Date, Merchant, CustomerID, etc.)

├── finance.ipynb        # Jupyter Notebook for data analysis & visualization in Python

├── finance.sql          # SQL scripts for data exploration & aggregations

├── finance.pbix         # Power BI dashboard 

└── README.md            # Project documentation

🗂 Dataset

The dataset (finance.csv) contains transaction-level data with columns such as:

TransactionDate – Date of transaction

TransactionID – Unique ID of the transaction

CustomerID – Customer identifier

Merchant – Merchant where transaction occurred

Amount – Transaction amount

TransactionType – Credit / Debit indicator

Balance – Running balance

📊 SQL Analysis

File: finance.sql

Queries implemented:

Total number of rows & transactions

Total transaction amount

Credit vs Debit totals

Average transaction amount per type

Top 10 merchants by transaction amount

Top 10 customers by number & value of transactions

Monthly transaction trends (by year-month)

finance

🐍 Python Analysis

File: finance.ipynb

Key analysis steps:

Data loading & cleaning from finance.csv

Exploratory Data Analysis (EDA)

Time-series analysis of inflow, outflow, and net cash flow

Rolling 7-day averages for customer balances

Fraud detection indicators (e.g., suspicious transactions)

Visualizations using Matplotlib / Seaborn / Plotly

📈 Power BI Dashboard

The Power BI dashboard integrates the processed data to provide:

Customer Balance (7-Day Rolling Average)

Monthly Credit vs Debit

Monthly Cash Flow (Inflow vs Outflow)

Net Cash Flow per Customer

Suspicious Transaction Table

Overall KPIs: total transactions, total credit, total debit, net cash flow, and suspicious transaction count

🚀 How to Run
1️⃣ SQL

Run queries from finance.sql in MySQL / PostgreSQL / SQLite after creating the finance database.

2️⃣ Python
jupyter notebook finance.ipynb


Make sure you install the required dependencies first:

pip install pandas matplotlib seaborn plotly

3️⃣ Power BI

Open Power BI Desktop

Load finance.csv

Reproduce visuals or view existing dashboard (Screenshot (90).png)

⚡ Author: Sahil gaikwad
📅 Date: September 2025
