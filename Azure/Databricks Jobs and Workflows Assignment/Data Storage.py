total_revenue = spark.read.format("delta").option("header", True).load("/mnt/datalake/output/revenue")
total_revenue.write.format("delta").mode("overwrite").saveAsTable("total_revenue")