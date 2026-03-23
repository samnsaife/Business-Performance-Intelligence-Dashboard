-- BUSINESS PERFORMANCE INTELLIGENCE QUERIES

-- 1. Total Revenue & Profit
SELECT 
    SUM(sales) AS total_revenue,
    SUM(profit) AS total_profit
FROM superstore;


-- 2. Monthly Sales Trend
SELECT 
    month,
    SUM(sales) AS monthly_sales
FROM superstore
GROUP BY month
ORDER BY month;


-- 3. Top 10 Products by Revenue
SELECT 
    product_name,
    SUM(sales) AS revenue
FROM superstore
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;


-- 4. Profit Leakage by Region
SELECT 
    region,
    SUM(profit) AS total_profit
FROM superstore
GROUP BY region
ORDER BY total_profit ASC;


-- 5. Loss-Making Categories
SELECT 
    category,
    SUM(profit) AS category_profit
FROM superstore
GROUP BY category
ORDER BY category_profit ASC;


-- 6. Customer Segmentation (High Value Customers)
SELECT 
    customer_name,
    SUM(sales) AS total_spent
FROM superstore
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;
