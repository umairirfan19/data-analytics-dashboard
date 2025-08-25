-- Create a table for the cleaned sales data (if using SQLite or another RDBMS)
CREATE TABLE IF NOT EXISTS sales_cleaned (
  date TEXT,
  product TEXT,
  category TEXT,
  region TEXT,
  units_sold INTEGER,
  unit_price REAL,
  discount REAL,
  returned INTEGER,
  customer_id TEXT,
  revenue REAL
);

-- Top products by revenue
SELECT product,
       SUM(revenue) AS total_revenue,
       SUM(units_sold) AS total_units
FROM sales_cleaned
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 10;

-- Revenue by region and category
SELECT region,
       category,
       ROUND(SUM(revenue), 2) AS revenue
FROM sales_cleaned
GROUP BY region, category
ORDER BY region, revenue DESC;

-- Return rate overall
SELECT ROUND(AVG(returned) * 100, 2) AS return_rate_percent
FROM sales_cleaned;

-- Daily revenue trend
SELECT date,
       ROUND(SUM(revenue), 2) AS revenue
FROM sales_cleaned
GROUP BY date
ORDER BY date;
