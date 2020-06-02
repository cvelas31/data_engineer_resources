import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
import pyspark.sql.functions as F
from pyspark.sql.types import (FloatType, DateType, StructType, StructField, StringType, LongType, 
                               IntegerType, ArrayType, BooleanType, DoubleType, DecimalType, TimestampType)

config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config["AWS"]['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config["AWS"]['AWS_SECRET_ACCESS_KEY']
mode = "ignore" #"overwrite"

def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data = os.path.join(input_data, "song_data", "*", "*", "*", "*.json")
    song_table_path = os.path.join(output_data, "song-table")
    artist_table_path = os.path.join(output_data, "artist-table")
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select("song_id", "title", "artist_id", "year", "duration")
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.partitionBy("year", "artist_id").mode(mode).parquet(song_table_path)
    print("songs_table saved")

    # extract columns to create artists table
    artists_table = df.select(F.col("artist_id"), 
                              F.col("artist_name").alias("name"),
                              F.col("artist_location").alias("location"),
                              F.col("artist_latitude").alias("latitude"),
                              F.col("artist_longitude").alias("longitude"))
    
    # write artists table to parquet files
    artists_table.write.mode(mode).parquet(artist_table_path)
    print("artists_table saved")

def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = os.path.join(input_data, "log_data/*.json")
    song_data = os.path.join(input_data, "song_data", "*", "*", "*", "*.json")
    
    users_table_path = os.path.join(output_data, "users-table")
    time_table_path = os.path.join(output_data, "time-table")
    songsplay_table_path = os.path.join(output_data, "songsplay-table")
    
    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.filter(F.col('page') == 'NextSong')

    # extract columns for users table    
    users_table = df.select(F.col("userId").alias("user_id"), 
                            F.col("firstName").alias("first_name"),
                            F.col("lastName").alias("last_name"),
                            F.col("gender"),
                            F.col("level"))
    
    # write users table to parquet files
    users_table.write.mode(mode).parquet(users_table_path)
    print("users_table saved")

    # create timestamp column from original timestamp column
    get_timestamp = F.udf(lambda x: datetime.fromtimestamp(x / 1000), TimestampType())
    df = df.withColumn("ts_timestamp", get_timestamp(F.col("ts")))
    
    # extract columns to create time table
    time_table = df.select(F.col("ts_timestamp").alias("start_time")).distinct()
    time_table = time_table.select(F.col("start_time"), 
                                   F.hour(F.col("start_time")).alias("hour"), 
                                   F.dayofmonth(F.col("start_time")).alias("day"), 
                                   F.weekofyear(F.col("start_time")).alias("week"), 
                                   F.month(F.col("start_time")).alias("month"), 
                                   F.year(F.col("start_time")).alias("year"),
                                   F.dayofweek(F.col("start_time")).alias("weekday"))
    
    # write time table to parquet files partitioned by year and month
    time_table.write.partitionBy("year", "month").mode(mode).parquet(time_table_path)
    print("time_table saved")
    # read in song data to use for songplays table
    song_df = spark.read.json(song_data)

    # extract columns from joined song and log datasets to create songplays table
    songplays_table = df.join(song_df, 
                              (df.artist == song_df.artist_name)&\
                              (df.length == song_df.duration)&\
                              (df.song == song_df.title),
                              how="inner")
    songplays_table = songplays_table.select(F.monotonically_increasing_id().alias("songplay_id"), 
                                             F.col("ts_timestamp").alias("start_time"), 
                                             F.col("userId").alias("user_id"), 
                                             F.col("level"), 
                                             F.col("song_id"),
                                             F.col("artist_id"), 
                                             F.col("sessionID").alias("session_id"), 
                                             F.col("location"),
                                             F.col("userAgent").alias("user_agent"),
                                             F.month(F.col("ts_timestamp")).alias("month"),
                                             F.year(F.col("ts_timestamp")).alias("year"))
    # Missing drop duplicates

    # write songplays table to parquet files partitioned by year and month
    songplays_table.write.partitionBy("year", "month").mode(mode).parquet(songsplay_table_path)
    print("songplays_table saved")


def main():
    spark = create_spark_session()
    selected_input_data = "local" #or "s3"
    if selected_input_data=="local":
        input_data = "./data"
    elif selected_input_data=="s3":
        input_data = "s3a://udacity-dend"
    else:
        print("Not valid input data selected")
    output_data = "s3a://udacity-de-nd"
    
    process_song_data(spark, local_data, output_data)    
    process_log_data(spark, local_data, output_data)


if __name__ == "__main__":
    main()
