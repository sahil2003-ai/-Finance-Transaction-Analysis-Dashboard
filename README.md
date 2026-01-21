# 💰 Finance Transaction Analysis & Dashboard

> A comprehensive financial analytics platform providing real-time insights into transaction flows, fraud detection, and customer financial health using SQL, Python, and interactive Power BI dashboards.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-MySQL%2FPostgreSQL-orange.svg)](#)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](#)

## 📋 Overview

This project delivers an **end-to-end financial transaction analysis system** combining multiple analytical tools to provide actionable insights into cash flows, customer financial behavior, fraud patterns, and balance management.

### Key Capabilities
- **Real-time Transaction Analysis** - SQL queries for instant financial metrics
- **Interactive Dashboards** - Power BI visualizations with 7-day rolling averages
- **Fraud Detection** - Automated identification of suspicious transactions
- **Cash Flow Analytics** - Inflow/outflow tracking and net position analysis
- **Customer Financial Health** - Running balance calculations and trend analysis

## 🗂️ Project Structure

```
-Finance-Transaction-Analysis-Dashboard/
├── finance.csv                          # Raw transaction dataset
├── finance.ipynb                        # Jupyter notebook with Python analysis & EDA
├── finance.sql                          # SQL queries for data exploration & KPIs
├── Finance Dashboard.pbix              # Power BI dashboard (main page with 5 visualizations)
└── README.md                           # Project documentation
```

## 📊 Dataset Overview

The dataset contains **transaction-level financial data** with comprehensive attributes:

| Field | Description | Type |
|-------|-------------|------|
| **TransactionID** | Unique transaction identifier | String |
| **TransactionDate** | Date and time of transaction | DateTime |
| **CustomerID** | Customer identifier | String |
| **Merchant** | Merchant/vendor name | String |
| **Amount** | Transaction amount (USD) | Numeric |
| **TransactionType** | Credit (inflow) or Debit (outflow) | Categorical |
| **Category** | Transaction category (e.g., Food, Utilities, Entertainment) | Categorical |
| **Balance** | Running account balance after transaction | Numeric |
| **Status** | Transaction status (Completed, Pending, Failed) | Categorical |
| **Location** | Geographic location of transaction | String |

## 🔍 Key Analytics Features

### 1. **Transaction Flow Analysis**
- Total credits (inflows) vs debits (outflows)
- Net cash flow calculations
- Monthly/daily transaction trends
- Category-wise spending patterns
- Top merchants by volume and value

### 2. **Customer Financial Health**
- 7-day rolling average balance trends
- Account balance volatility analysis
- High-risk account identification
- Customer spending patterns
- Average transaction value by customer

### 3. **Fraud Detection System**
- Suspicious transaction flagging (23 alerts in current dataset)
- Unusual merchant activity alerts
- High-value transaction monitoring
- Velocity checks (frequent transactions in short timeframe)
- Outlier detection using statistical methods

### 4. **Financial KPIs**
- Total transaction volume
- Average transaction size
- Peak transaction hours/days
- Customer retention metrics
- Account churn indicators

## 🧮 SQL Analysis (`finance.sql`)

Comprehensive SQL queries covering:

### Core Metrics
```sql
-- Total transactions and amounts
SELECT 
  COUNT(*) AS total_transactions,
  ROUND(SUM(CASE WHEN TransactionType='Credit' THEN Amount ELSE 0 END), 2) AS total_credits,
  ROUND(SUM(CASE WHEN TransactionType='Debit' THEN Amount ELSE 0 END), 2) AS total_debits,
  ROUND(SUM(CASE WHEN TransactionType='Credit' THEN Amount ELSE -Amount END), 2) AS net_cash_flow
FROM finance;
```

### Analysis Queries
- **Transaction Summary**: Total rows, transaction counts, amount aggregations
- **Credit vs Debit**: Side-by-side comparison of inflows and outflows
- **Average Analysis**: Average transaction amounts by type
- **Top Merchants**: Ranking merchants by transaction volume and value
- **Top Customers**: Identifying high-value customers by transaction frequency and total spent
- **Time Series**: Monthly and daily transaction trends
- **Customer Segmentation**: Grouping customers by spending patterns
- **Balance Analysis**: Rolling balance calculations and trend identification

**Total Queries**: 12+ comprehensive analytical queries

## 🐍 Python Analysis (`finance.ipynb`)

### Analysis Pipeline

1. **Data Loading & Preprocessing**
   - Load finance.csv with proper data types
   - Handle missing values and data quality issues
   - Date/time parsing and normalization
   - Outlier detection and treatment

2. **Exploratory Data Analysis (EDA)**
   - Statistical summary (mean, median, std, min, max)
   - Distribution analysis of transaction amounts
   - Time-based patterns (daily, weekly, monthly)
   - Customer segmentation insights

3. **Transaction Flow Analysis**
   - Total inflows vs outflows
   - Net cash flow calculations
   - Cumulative balance tracking
   - Cash flow forecasting

4. **Customer Financial Health**
   - 7-day rolling average balance
   - Balance volatility metrics
   - Customer spending velocity
   - Account activity trends

5. **Fraud Detection Model**
   - Anomaly detection using statistical methods
   - Suspicious transaction identification
   - Merchant risk scoring
   - Velocity-based alerts

6. **Visualizations**
   - Time series plots (cash flow trends)
   - Histograms (transaction amount distributions)
   - Box plots (category comparisons)
   - Heatmaps (hourly/daily transaction patterns)
   - Scatter plots (transaction amount vs frequency)
   - Line charts (rolling balance trends)

### Required Libraries
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter
```

## 📈 Power BI Dashboard (`Finance Dashboard.pbix`)

### Dashboard Overview - Main Page: Transaction Insights

**Executive KPI Cards**
- **2,084** Total Transactions (all recorded transactions)
- **5.36M** Total Credit (total inflows/deposits)
- **5.20M** Total Debit (total outflows/withdrawals)
- **156.61K** Net Cash Flow (Credits - Debits)
- **23** Suspicious Transactions (Fraud Alerts flagged)

### Main Dashboard Visualizations

**1. Customer Balance (7-Day Rolling Average)**
- Line chart showing customer account balance trends over time
- Displays balance smoothing over 7-day rolling window
- Helps identify account health and volatility patterns
- X-axis: Time period | Y-axis: Balance amount

**2. Customer Net Cash Flow**
- Horizontal bar chart ranking customers by net cash position
- Shows individual customer cash flow status (positive/negative)
- Sorted by cash flow value for easy identification
- Top customers ranked by cash flow contribution

**3. Suspicious Transactions Table**
- Transaction-level fraud detection table
- Columns: TransactionDate, TransactionID, CustomerID, Amount, Merchant, Balance, Suspicious Transaction (Yes/No)
- Red dot indicators (●) for flagged suspicious transactions
- Sortable and filterable by date, merchant, amount, and status
- Sample flagged merchants: Uber, Walmart, Apple Store

**4. Monthly Credit vs Debit**
- Stacked column chart comparing inflows and outflows
- Orange bars = Credits | Blue bars = Debits
- Monthly breakdown across complete date range
- Shows seasonal cash flow patterns
- Values range from ~$95K to $461K per month

**5. Monthly Cash Flow (Inflow vs Outflow)**
- Dual-axis line chart showing inflow/outflow trends
- Green line = Monthly Inflow (Credits)
- Red line = Monthly Outflow (Debits)
- Time period: 2018-2023 (multi-year analysis)
- Helps identify peak and low cash flow periods
- Approximately ±$400K-500K range

### Interactive Filters & Controls
- **Date Filter**: Custom date range selection (01-01-2018 to 15-09-2023)
- **Amount Range Filter**: Filter transactions by amount thresholds ($5.52 - $9,999.36)
- **Merchant Filter**: Filter by specific merchant names (All option with dropdown)
- **CustomerID Filter**: Search and filter by individual customers
- **Real-time Updates**: All visualizations update dynamically based on filter selections

### Key Features
- Responsive layout for all screen sizes
- Tooltip hover details on all charts
- Drilldown capabilities for deeper analysis
- Professional color scheme (blue/orange for credits/debits)
- Performance-optimized for 5M+ transaction datasets

## 🚀 How to Use

### Option 1: SQL Analysis
```sql
-- Create database
CREATE DATABASE finance_db;
USE finance_db;

-- Import data
LOAD DATA INFILE 'finance.csv' INTO TABLE finance
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;

-- Run analysis queries
SOURCE finance.sql;
```

### Option 2: Python Analysis (Jupyter Notebook)
```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter

# Launch Jupyter
jupyter notebook finance.ipynb

# Run all cells to generate analysis and visualizations
```

### Option 3: Power BI Dashboard
```
1. Open Finance Dashboard.pbix in Power BI Desktop
2. Click "Transform Data" to refresh CSV connection
3. View Transaction Insights main page
4. Use filters to analyze by date, customer, merchant
5. Export reports as needed
```

## 💡 Key Insights & Metrics

### Financial Metrics
- **Total Transactions**: 2,084 transactions
- **Total Credits**: $5.36M (inflows)
- **Total Debits**: $5.20M (outflows)
- **Net Cash Flow**: $156.61K (positive)
- **Average Transaction**: ~$2,478
- **Balance Range**: Min to Max account balance across customers

### Behavioral Insights
- Peak transaction hours and days
- Top spending categories and merchants
- High-value customer segments
- Merchant concentration risk
- Transaction frequency patterns

### Risk Indicators
- **Fraud Alerts**: 23 suspicious transactions flagged
- Fraud detection rate: Automated anomaly detection
- High-risk merchant identification
- Unusual transaction patterns
- Balance volatility scores

## 📁 File Descriptions

| File | Size | Description |
|------|------|-------------|
| `finance.csv` | ~500 KB | Raw transaction dataset (2,084 records) |
| `finance.ipynb` | ~2 MB | Jupyter notebook with Python analysis |
| `finance.sql` | ~20 KB | 12+ SQL queries for analytics |
| `Finance Dashboard.pbix` | ~3 MB | Interactive Power BI dashboard |
| `README.md` | This file | Complete project documentation |

## 🛠️ Technologies & Tools

| Category | Technologies |
|----------|---------------|
| **Data Processing** | Python (Pandas, NumPy) |
| **Visualization** | Matplotlib, Seaborn, Plotly, Power BI |
| **Database** | SQL (MySQL, PostgreSQL, SQLite) |
| **Machine Learning** | Scikit-learn (anomaly detection, classification) |
| **Analysis** | Jupyter Notebook |
| **BI/Reporting** | Microsoft Power BI |
| **Data Format** | CSV, XLSX |

## 🎯 Use Cases

1. **Bank Account Monitoring** - Real-time transaction tracking and alerts
2. **Fraud Prevention** - Automated detection of suspicious activities
3. **Customer Financial Health** - Balance monitoring and trend analysis
4. **Merchant Insights** - Top spenders and category analysis
5. **Cash Flow Planning** - Inflow/outflow forecasting
6. **Financial Compliance** - Audit trails and transaction history
7. **Risk Management** - Customer segmentation and risk scoring

## 🎯 Future Enhancements

- [ ] Predictive cash flow modeling with ARIMA/Prophet
- [ ] Advanced machine learning fraud detection
- [ ] Real-time streaming data processing
- [ ] API integration with banking systems
- [ ] Mobile app for transaction alerts
- [ ] Advanced customer segmentation (RFM analysis)
- [ ] Automated report generation and scheduling
- [ ] Machine learning for spending pattern prediction

## 📝 License

MIT License - Feel free to use this project for personal and commercial purposes.

## 👤 Author

**Sahil Gaikwad**
- GitHub: [@sahil2003-ai](https://github.com/sahil2003-ai)
- LinkedIn: [Sahil Gaikwad](https://linkedin.com)
- Portfolio: [Data Science Projects](https://github.com/sahil2003-ai)

## 🙏 Acknowledgments

- Dataset: Financial Transaction Data
- Tools: Python, SQL, Power BI
- Inspiration: FinTech best practices and financial analytics standards

## ⭐ Show Your Support

If this project helped you with financial analytics or fraud detection, please consider giving it a **star**! Your support motivates me to create more comprehensive financial analysis tools.

---

**Last Updated**: January 2026 | **Version**: 3.0 | **Status**: Active Development
