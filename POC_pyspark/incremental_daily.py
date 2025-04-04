import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
from datetime import datetime
import logging

# Configure logging
log_file = "POC_pyspark/transactions.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()
 
spark = SparkSession.builder\
    .appName("transactions")\
    .config("spark.ui.port", "4041")\
    .getOrCreate()

logger.info("Spark session Initialized.")

# for daily aggregation
def aggregate_daily(df):

    try:
        df = df.withColumn("transaction_date", to_date(col("transaction_date")))
        txn_date = datetime.now().strftime("%Y-%m-%d")

        logger.info(f"Starting daily aggregation for {txn_date}")
    
        # For each day, perform the aggregation to calculate total sales per store and number of transactions per store.
        daily_agg_df = df.groupBy(col("store_id")
                            ).agg(
                                sum('amount').alias('total_sales'),
                                count('transaction_id').alias('no_of_trans')
                            ).orderBy("store_id")
    
        # daily_agg_df.write.mode("overwrite").csv(f'daily_agg/{datetime.now().strftime("%Y%m%d")}')
        daily_agg_df.write.mode("append").csv('POC_pyspark/daily_agg')
        logger.info(f"Daily aggregation completed for {txn_date}")
    
    except Exception as e:
        logger.error(f"Error in daily aggregation: {e}")

def aggregate_monthly(df):

    try:
        df = df.withColumn("transaction_date", to_date(col("transaction_date")))
        txn_month = datetime.now().strftime("%Y-%m")

        logger.info(f"Starting monthly aggregation for {txn_month}")

        # At the end of the month, compute the total sales per store for the month and the total transactions per store for the month.
        monthly_agg_df = df.groupBy(col("store_id"), date_trunc("month", col("transaction_date")).alias("month")
                ).agg(sum("amount").alias("total_sales_store"),
                      count("transaction_id").alias("num_txn_store")
                ).orderBy("store_id")
    
        # monthly_agg_df.write.mode("overwrite").csv(f'monthly_agg/{datetime.now().strftime("%Y%m")}')
        monthly_agg_df.write.mode("append").csv('POC_pyspark/monthly_agg')
        logger.info(f"Monthly aggregation completed for {txn_month}")

    except Exception as e:
        logger.error(f"Error in monthly aggregation: {e}")

def load(txn_path):

    try:
        logger.info(f"Loading transactions from {txn_path}")

        txn_df = spark.read.csv(txn_path, header=True, inferSchema=True)
    
        aggregate_daily(txn_df)
        aggregate_monthly(txn_df)
    
        txn_df.write.mode("append").csv('POC_pyspark/transactions')

        logger.info(f"Data successfully loaded and processed for {txn_path}")
    
    except Exception as e:
        logger.error(f"Error in loading aggregated data: {e}")
 
txn_date = datetime.now().strftime('%Y%m%d')
txn_path = os.path.join(os.getcwd(), 'POC_pyspark', f'transactions_{txn_date}.csv')

logger.info(f"Looking for file: {txn_path}")

try: 
    if os.path.isfile(txn_path):
        load(txn_path)
    else:
        logger.warning(f"File not found: {txn_path}")

except Exception as e:
    logger.error(f"Unexpected Error: {e}")
 
logger.info("Shutting down Spark session.")
spark.stop()