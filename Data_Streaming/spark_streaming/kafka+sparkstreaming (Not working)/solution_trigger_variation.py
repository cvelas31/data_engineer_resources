import logging
from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)

def run_spark_job(spark):

    df = spark.readStream.format("kafka")\
                .option("kafka.bootstrap.servers", "localhost:9092")\
                .option("subscribe", "exampleTopic")\
                .option("startingOffsets", "earliest")\
                .option("maxOffsetsPerTrigger", 10)\
                .option("stopGracefullyOnShutdown", "true")\
                .load()
    logger.info(f"df: {df}")
    # Show schema for the incoming resources for checks
    df.printSchema()
    
    agg_df = df.groupBy().count()
    # agg_df = df.count() # Not working
    
    logger.info("----------  WriteStream -----------")
    
    # play around with processingTime to see how the progress report changes
    query = agg_df.writeStream.trigger(processingTime="120 seconds")\
                .outputMode('Complete')\
                .format('console')\
                .option("truncate", "false")\
                .start()
    
        
if __name__ == "__main__":
    

    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("StructuredStreamingSetup") \
        .getOrCreate()

    logger.info("Spark started")

    run_spark_job(spark)

    spark.stop()
