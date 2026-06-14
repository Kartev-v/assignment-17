# assignment-17
Perform sales data analysis using PySpark and Docker.

## Operations Performed
1. Read CSV into PySpark DataFrame.
2. Sort products by sales in descending order.
3. Display top 3 products with highest sales.
4. Filter products with sales greater than 80,000.
5. Save filtered records as CSV.

## Build Docker Image
docker build -t sales-spark .

## Run Container
docker run sales-spark