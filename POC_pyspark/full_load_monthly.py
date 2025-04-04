import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
from datetime import datetime
import logging

# Configure logging
log_file = "POC_pyspark/store_data.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger()

spark = SparkSession.builder\
    .appName("fullLoad")\
    .config("spark.ui.port", "4041")\
    .getOrCreate()

logger.info("Spark session Initialized.")

def load_new_data(file_path):
    
    try:
        logger.info(f"Loading new store data from {file_path}")

        # Read CSV file
        new_store_df = spark.read.csv(file_path, header=True, inferSchema=True)

        new_store_df.write.mode("overwrite").csv('POC_pyspark/store_data')

        logger.info("Store data successfully loaded and overwritten.")

    except Exception as e:
        logger.error(f"Error while loading store data: {e}")

curr_month = datetime.now().strftime('%Y%m')
txn_path = os.path.join(os.getcwd(), 'POC_pyspark', f'stores_{curr_month}.csv')

logger.info(f"Looking for file: {txn_path}")

# check if file exists or not
if os.path.isfile(txn_path):
    load_new_data(txn_path)
else:
   logger.warning(f"File not found: {e}")

logger.info("Shutting down Spark session.")
spark.stop()