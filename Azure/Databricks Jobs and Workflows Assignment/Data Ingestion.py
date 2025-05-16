# Databricks notebook source
spark.conf.set(
    "fs.azure.account.key.strgazurerj.dfs.core.windows.net", 
    "<Access Key>"
)


dbutils.fs.ls("abfss://data@strgazurerj.dfs.core.windows.net/")


transaction_df = spark.read.format("csv") \
                .option("header", "true") \
                .option("inferSchema", "true") \
                .load("abfss://data@strgazurerj.dfs.core.windows.net/transactions.csv")


transaction_df = transaction_df.withColumnRenamed("Invoice ID", "invoice_id") \
                              .withColumnRenamed("Customer ID", "customer_id") \
                              .withColumnRenamed("Product ID", "product_id") \
                              .withColumnRenamed("Unit Price", "unit_price") \
                              .withColumnRenamed("Line Total", "line_total") \
                              .withColumnRenamed("Store ID", "store_id") \
                              .withColumnRenamed("Employee ID", "employee_id") \
                              .withColumnRenamed("Currency Symbol", "currency_symbol") \
                              .withColumnRenamed("Transaction Type", "transaction_type") \
                              .withColumnRenamed("Invoice Total", "invoice_total") \
                              .withColumnRenamed("Payment Method", "payment_method")


transaction_df.write.format("delta").mode("overwrite").save("/mnt/datalake/raw/transactions")


customer_df = spark.read.format("csv") \
                .option("header", "true") \
                .option("inferSchema", "true") \
                .load("abfss://data@strgazurerj.dfs.core.windows.net/customers.csv")


customer_df = customer_df.withColumnRenamed("Customer ID", "customer_id") \
                         .withColumnRenamed("Date Of Birth", "date_of_birth") \
                         .withColumnRenamed("Job Title", "job_title")


customer_df.write.format("delta").mode("overwrite").save("/mnt/datalake/raw/customers")