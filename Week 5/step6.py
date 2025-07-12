# now we aree reeading files and then writing these in csv,avro,parquet format copying from database
# then exporting all files using spark also using datetime because of
# a table we have using these features therefore datetime is used with year-month-date format

rom datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")

os.makedirs("spark_exports/csv", exist_ok=True)
os.makedirs("spark_exports/parquet", exist_ok=True)
os.makedirs("spark_exports/avro", exist_ok=True)

for table in tables:
    print(f"🔄 Exporting {table}...")

    df = spark.read.jdbc(url=jdbc_url, table=table, properties=connection_props)

    # CSV
    df.write.mode("overwrite").option("header", "true").csv(f"spark_exports/csv/{table}_{date_str}")

    # Parquet
    df.write.mode("overwrite").parquet(f"spark_exports/parquet/{table}_{date_str}")

    # Avro
    df.write.format("avro").mode("overwrite").save(f"spark_exports/avro/{table}_{date_str}")

print("✅ All tables exported!")