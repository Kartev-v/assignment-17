from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

df.show()

print("\nProducts Sorted by Sales")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

print("\nTop 3 Products")
top3 = sorted_df.limit(3)
top3.show()

print("\nSales Greater Than 80000")
high_sales = df.filter(col("sales") > 80000)
high_sales.show()

high_sales.write.mode("overwrite").option("header", True).csv("/data/output")
print("Output saved successfully!")

spark.stop()