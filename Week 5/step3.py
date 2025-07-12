# now set enviroment variables and start Spark (with MySQL & Avro support)
import os
import findspark

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.4.1-bin-hadoop3"
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Export MySQL Tables") \
    .config("spark.jars.packages",
            "mysql:mysql-connector-java:8.0.33,"
            "org.apache.spark:spark-avro_2.12:3.4.1") \
    .getOrCreate()

print("✅ Spark is ready.")


