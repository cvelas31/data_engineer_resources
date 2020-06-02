# Data Lake Project

## Introduction
A music streaming startup, Sparkify, has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow their analytics team to continue finding insights in what songs their users are listening to.

You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Datasets
You'll be working with two datasets that reside in S3. Here are the S3 links for each:

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data

## Schema
- Fact Table
    1. songplays - records in log data associated with song plays i.e. records with page NextSong
        - songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
- Dimension Tables
    1. users - users in the app
        - user_id, first_name, last_name, gender, level
    2. songs - songs in music database
        - song_id, title, artist_id, year, duration
    3. artists - artists in music database
        - artist_id, name, location, lattitude, longitude
    4. time - timestamps of records in songplays broken down into specific units
        - start_time, hour, day, week, month, year, weekday

# Execute
To execute the project just run:
```python
python etl.py
```
It has a parameters were you can select to use local input data, or s3 input data.
It will read the input data (s3 or local), and it will save the files inside the output data directory. All the files are saved as parquet.