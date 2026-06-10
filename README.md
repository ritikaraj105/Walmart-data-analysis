# Walmart-data-analysis
                                     #THE ARCHITECTURE
OBTAIN DATASET

STEP1 -- Setup API by obtaining Kaggle API token by navigating through profile settings and downloading the json file to keep dataset in real-time. Keep the downloaded file in new folder.

LIBRARIES

STEP2 -- Install required Pythomn libraries
pip install pandas numpy sqlalchemy mysql-connector-python psycopg2.

DATA UNDERSTANDING

STEP3 -- Conduct data exploration to understand data and get quick overview of the data structure and statistics.
Using functions like -- .info(),.describe(),.head().

DATA CLEANING

STEP4 -- Clean the dataset by dropping the rows having missing values, fill the missing values by mean, median or mode as required, .replace() for removing the unwanted caharacter( '$' in our case) and many more.

FEATURE ENGINEERING

STEP4 -- Feature Engineering, create new column as per requirement here total as product od price and quantity.

MySQL CONNECTION

STEP5 -- Load the data in MySQL using connectors ,Connect to MySQL  using sqlalchemy and load the cleaned data into  database.
Run initial queried in MySQL to ensure proper data connection.

QUERIES

STEP6 -- Business Problem-Solving: Write and execute complex SQL queries to answer critical business questions, such as:
Revenue trends across branches and categories.
Identifying best-selling product categories.
Sales performance by time, city, and payment method.
Analyzing peak sales periods and customer buying patterns.
Profit margin analysis by branch and category.
Documentation: Keep clear notes of each query's objective, approach, and results.

QUERIES

1 -- Analyize payment method ans sales
2 -- Find highest rated category in each branch
3 -- Determine busiest day
4 -- Total quantity sold per payment method
5 -- Analyze category rating by city
6 -- Calculate total profit by category
7 -- Determine most common payment method per branch
8 -- Analyze sales shift throughout day
9 -- Identitfy branch with highest revenue decline by year

RESULTS AND INSIGHTS

Sales Insights: Key categories, branches with highest sales, and preferred payment methods.
Profitability: Insights into the most profitable product categories and locations.
Customer Behavior: Trends in ratings, payment preferences, and peak shopping hours.



