create database finance;

use finance;

-- Total rows
SELECT COUNT(*) AS total_rows FROM finance;

-- Total transaction amount
SELECT SUM(Amount) AS total_amount FROM finance;

-- Total Credit vs Debit
SELECT TransactionType, SUM(Amount) as total_amount
FROM finance
GROUP BY TransactionType;

-- Average transaction amount per type
SELECT TransactionType, AVG(Amount) as avg_amount
FROM finance
GROUP BY TransactionType;

-- Top 10 Merchants by transaction amount
SELECT Merchant, SUM(Amount) as total_amount
FROM finance
GROUP BY Merchant
ORDER BY total_amount DESC
LIMIT 10;

-- Transactions per Customer (Top 10)
SELECT CustomerID, COUNT(*) as num_transactions, SUM(Amount) as total_amount
FROM finance
GROUP BY CustomerID
ORDER BY total_amount DESC
LIMIT 10;

-- Monthly total transaction amount
-- (Assumes TransactionDate can be parsed as date)
SELECT SUBSTR(TransactionDate, 7, 4) || '-' || SUBSTR(TransactionDate, 4, 2) as year_months,
       SUM(Amount) as total_amount
FROM finance
GROUP BY year_months
ORDER BY year_months;
