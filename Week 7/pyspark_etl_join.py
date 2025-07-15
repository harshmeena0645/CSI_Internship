from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name, regexp_extract, to_date

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Customer-Order Delta Join") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Read Customer Master Files
cust_df = spark.read.option("header", True).csv("/content/CUST_MSTR_201911*.csv") \
    .withColumn("filename", input_file_name()) \
    .withColumn("date_str", regexp_extract("filename", r"CUST_MSTR_(\d{8})", 1)) \
    .withColumn("cust_file_date", to_date("date_str", "yyyyMMdd")) \
    .drop("filename", "date_str")

# Read master_child_export Files
order_df = spark.read.option("header", True).csv("/content/master_child_export-201911*.csv") \
    .withColumn("filename", input_file_name()) \
    .withColumn("date_str", regexp_extract("filename", r"master_child_export-(\d{8})", 1)) \
    .withColumn("order_file_date", to_date("date_str", "yyyyMMdd")) \
    .drop("filename", "date_str")

# Perform Join on Customer ID
joined_df = cust_df.join(order_df, cust_df.id == order_df.cust_id, "inner") \
    .select(
        cust_df["id"],
        cust_df["name"],
        cust_df["city"],
        order_df["order_id"],
        order_df["amount"],
        cust_df["cust_file_date"],
        order_df["order_file_date"]
    )

# Show the result
joined_df.show(truncate=False)

# Save to Delta Table
joined_df.write.format("delta").mode("overwrite").save("/content/output/delta_output/joined_output")

# Stop Spark session
spark.stop()
