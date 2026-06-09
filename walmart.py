SELECT*FROM walmart LIMIT 10;
SELECT COUNT(*) FROM walmart;
SELECT DISTINCT payment_method FROM walmart;
-- question 1 group each payment method and 
-- give their corresponding total and total sol

SELECT 
    payment_method,
      COUNT(*) as no_pay,
      SUM(quantity) as no_qt_sold
FROM walmart
GROUP BY payment_method;
-- question 2 identify the highest rated category in each 
-- branch,displaying the branch,category
SELECT*FROM walmart;
SELECT branch,
      category,
      AVG(rating) as avg_rating,
      RANK() OVER (PARTITION BY branch ORDER BY AVG(rating)DESC) as rankk
 -- we ranked all top rating in each category
 FROM walmart
 GROUP BY 1,2
 ORDER BY 1,3 DESC;
 -- each branch when they have highest number of transaction
 -- grpby by branch then day then count number of invoice
 SELECT*FROM walmart;
 SELECT 
    branch,
    DAYNAME(STR_TO_DATE(date, '%d/%m/%y')) AS formatted_date,
    COUNT(*) AS no_transactions
FROM walmart
GROUP BY branch, formatted_date
ORDER BY branch, no_transactions DESC;
-- can use rank to find highest number of transaction in each branch, could be on any day
 -- question 3 list total numberof quantty sold per payment method
 SELECT 
     payment_method,
     SUM(quantity) as sold_one
FROM walmart
     GROUP BY payment_method;
-- question 4 determine the avg,min,max,rating of the product for each city for category and list avg rating min and max rating
SELECT *FROM walmart;
SELECT 
      city,
      category,
      avg(rating) as avg_rating,
      MIN(rating) as min_rating,
      MAX(rating) as max_rating
FROM walmart
GROUP BY city,category;
-- question 5 calculate the totalprofit for each category by
-- considering total_profit as unit price*quantity*profit margin,
-- list category and total profit, ordered from highest to lowest

SELECT 
    category,
    SUM(total * profit_margin) AS total_profit
FROM walmart
GROUP BY category
ORDER BY total_profit DESC;
-- question 6 determine the most common payment method for each branch
SELECT
    branch,
    payment_method,
    COUNT(*) AS total_trans,
    RANK() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS `rank`

FROM walmart

GROUP BY branch, payment_method;

-- if we want only rank 1 then WITH cte AS(SELECT......GROUPBY)
-- SELECT*cte WHERE rank=1
-- question 7 categorize sales into 3 grp morning,afternoon,evening, and
-- find out each of the shift and number of invoice 

SELECT
    CASE
        WHEN HOUR(time) < 12 THEN 'Morning'
        WHEN HOUR(time) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS shift,
    COUNT(*) AS num_invoices
FROM walmart
GROUP BY shift
ORDER BY num_invoices DESC;
-- identitfy 5 branch with highest decreas
--  rate in revenue compare to last year 2023 and 2022
WITH branch_revenue AS (
    SELECT 
        branch,
        -- Calculate 2022 revenue
        SUM(CASE WHEN STR_TO_DATE(date, '%d/%m/%y') BETWEEN '2022-01-01' AND '2022-12-31' THEN total ELSE 0 END) AS revenue_2022,
        -- Calculate 2023 revenue
        SUM(CASE WHEN STR_TO_DATE(date, '%d/%m/%y') BETWEEN '2023-01-01' AND '2023-12-31' THEN total ELSE 0 END) AS revenue_2023
    FROM walmart
    GROUP BY branch
)
SELECT 
    branch,
    revenue_2022,
    revenue_2023,
    -- Formula for decrease rate: ((Old - New) / Old) * 100
    ROUND(((revenue_2022 - revenue_2023) / revenue_2022) * 100, 2) AS decrease_rate_pct
FROM branch_revenue
-- Filter to only show branches that actually had a drop in revenue
WHERE revenue_2023 < revenue_2022
ORDER BY decrease_rate_pct DESC
LIMIT 5;


     
     
 

      
      


