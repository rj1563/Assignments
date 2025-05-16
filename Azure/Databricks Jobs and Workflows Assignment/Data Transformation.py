transaction_df = spark.read.format("delta").option("header", True).load("/mnt/datalake/raw/transactions")


customer_df = spark.read.format("delta").option("header", True).load("/mnt/datalake/raw/customers")


joined_df = transaction_df.join(customer_df, transaction_df["customer_id"] == customer_df["customer_id"], "inner")


from pyspark.sql.functions import col, avg, sum, count

# Changing datatypes of columns
joined_df = joined_df.withColumn("unit_price", col("unit_price").cast("float"))
joined_df = joined_df.withColumn("Discount", col("Discount").cast("float"))
joined_df = joined_df.withColumn("line_total", col("line_total").cast("float"))
joined_df = joined_df.withColumn("invoice_total", col("invoice_total").cast("float"))

# Dropping nulls 
joined_df = joined_df.dropna(subset=['Size', 'Color'])

joined_df = joined_df.filter((joined_df["Discount"] != 0))

# Total revenue per store per day
total_revenue = joined_df.groupBy("store_id", "Date") \
  .agg(
      sum("line_total").alias("total_revenue"),
      count("invoice_id").alias("num_transactions")
  )


total_revenue.write.format("delta").mode("overwrite").save("/mnt/datalake/output/revenue")