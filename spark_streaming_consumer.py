import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp, window, expr
from pyspark.sql.types import StructType, StringType, IntegerType

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SparkConsumer")

# Define schema
schema = StructType() \
    .add("user_id", IntegerType()) \
    .add("product", StringType()) \
    .add("timestamp", StringType())

try:
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("ProductClickAnalytics") \
        .master("local[*]") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.0") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")
    logger.info("Spark session started")

    # Read from Kafka
    raw_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "product_clicks") \
        .option("startingOffsets", "earliest") \
        .load()

    # Parse and clean data
    parsed_df = raw_df.select(from_json(col("value").cast("string"), schema).alias("data")) \
        .select("data.*") \
        .na.drop(subset=["user_id", "product", "timestamp"]) \
        .withColumn("event_time", expr("try_to_timestamp(timestamp)")) \
        .drop("timestamp") \
        .filter(col("event_time").isNotNull())

    # Aggregate click counts in 10-second windows
    aggregated_df = parsed_df \
        .withWatermark("event_time", "1 minute") \
        .groupBy(window(col("event_time"), "10 seconds"), col("product")) \
        .count() \
        .selectExpr("window.start as start_time", "window.end as end_time", "product", "count")

    # Write batch to Parquet and CSV
    def write_batch(batch_df, batch_id):
        parquet_path = f"/home/ajaychary06/product_pipeline_output_parquet/batch_{batch_id}"
        csv_path = f"/home/ajaychary06/product_pipeline_output_csv/batch_{batch_id}"
        batch_df.write.mode("overwrite").parquet(parquet_path)
        batch_df.write.mode("overwrite").csv(csv_path, header=True)

    # Start the query
    query = aggregated_df.writeStream \
        .outputMode("update") \
        .foreachBatch(write_batch) \
        .option("checkpointLocation", "/home/ajaychary06/product_pipeline_output_parquet/checkpoint") \
        .trigger(processingTime="10 seconds") \
        .start()

    query.awaitTermination()

except Exception as e:
    logger.error(f"Spark Streaming Failed: {e}")

finally:
    if 'spark' in locals():
        spark.stop()
