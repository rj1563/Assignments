
# Full Load for Store Data (Monthly) & Incremental Load for Transactions (Daily) with Aggregation 


## Scripts 

```markdown
incremental_daily.py
full_load_monthly.py
```





## Description

This script handles the full load of store data on a monthly basis and the incremental load of transaction data on a daily basis. It performs daily and monthly aggregations to summarize key metrics from the transaction data

## Author

- Rupali Jain


## Date

- 2025-04-03
## Version

- 1.0
## Dependencies

 - findspark
 - pyspark
 - os
 - datetime
 - logging
## Usage/Examples

## Execution command: 

```markdown
spark-submit incremental_daily.py
spark-submit full_load_monthly.py
```

## Inputs

- Store Data (Full Load - Monthly): ``` stores_YYYYMM.csv ```
- Transaction Data (Incremental Load – Daily):  ``` transactions_YYYYMMDD.csv ```

## Expected formats:

 - Store Data: Includes store details like store_id, store_name, location etc.
 - Transaction Data: Includes transaction_id, transaction_date, store references etc.

## Outputs:

- Daily aggregation and monthly aggregation
- Processed data stored in a structured format ie. CSV in a hive table.
- Logs files (transactions.log, store_data.log)




## Imports

- findspark: used for initializing Spark in enviornments.
- SparkSession: Creates and manages Spark session.
- functions: used for data aggregation and transformations.
- os: used for interacting with the operating system such as to check if file exists or not.
- datetime: used for handling date and time operations.
- logging: used for providing logs.
## Spark Session Initialization

``` markdown
spark = SparkSession.builder\
    .appName("transactions")\
    .config("spark.ui.port", "4041")\
    .getOrCreate()
```

- Initializes a Spark session with the application name "transactions".
- Configured to use the default settings.

``` markdown
spark = SparkSession.builder\
    .appName("fullLoad")\
    .config("spark.ui.port", "4041")\
    .getOrCreate()
```

- Initializes a Spark session with the application name "fullLoad".
- Configured to use the default settings.

## Data Ingestion

 Store Data (Full Load – Monthly)
- Source: ``` stores_YYYYMM.csv ```
- Format: CSV
- Schema:
    ```markdown
    store_id (string)
    store_name (string)
    location: (string)
    manager (string)
    total_sales (integer)
    last_updated: (date)
    ```
- Process: Replace the existing store dataset with the new dataset at the start of every month.

Transaction Data (Incremental Load - Daily)
- Source: ```transactions_YYYYMMDD.csv```
- Format: CSV
- Schema:
    ```markdown
    transaction_id (integer)
    store_id (string)
    customer_id (string)
    amount (dobule)
    transaction_date (date)
    status (string)
    payment_method (string)
    ```
- Process
    - Load only new daily transaction data.
    - Compute daily and Monthly aggregations.
## Data Transformations

 - #### Daily Aggregation:
    For each day, performed the aggregation to calculate total sales per store and number of transactions per store, using groupBy, sum and count.

 - #### Monthly Aggregation:
    At the end of the month, computed the total sales per store for the month and the total transactions per store for the month using the date_trunc function for extracting the month from the date and performing the aggregate.
## Output Data

- stores CSV files locally.
- Format: CSV
- #### Write Mode: 
    - Append (for transactions, daily and monthly aggregations)
    - Overwrite (for store data)

## Performance Considerations

- Schema inference to optimize read performance
## Error Handling & Logging
- Exception handling strategy used try – except block for printing error and to raise error.
- Logging details
## Resource Cleanup

``` spark.stop() ```

- Closes the Spark session after execution to free resources.
