
-- 1. View sample records
SELECT *
FROM sales
LIMIT 5;

-- 2. Total sales and profit
SELECT
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales;

-- 3. Sales by category
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- 4. Profit by region
SELECT
    region,
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_profit DESC;

-- 5. Loss-making subcategories
SELECT
    "sub-category",
    ROUND(SUM(profit), 2) AS total_profit
FROM sales
GROUP BY "sub-category"
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;

-- 6. Top 10 customers by sales
SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM sales
GROUP BY customer_id, customer_name
ORDER BY total_sales DESC
LIMIT 10;
