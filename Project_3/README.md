# Data Warehouse Project

## Project Datasets
You'll be working with two datasets that reside in S3. Here are the S3 links for each:

Song data: `s3://udacity-dend/song_data` <br>
Log data: `s3://udacity-dend/log_data`<br>
Log data json path: `s3://udacity-dend/log_json_path.json`<br>

## Steps:
- First the drop tables was done to make sure the process can be done from zero
- The table creation is done using 2 staging tables for each S3 dataset
    - staging_events: Having all the simulated events of the users
    - staging_songs: All the information about the song (artist, title, duration, etc)
- The table. creation of ther 5 tables with this schema:
    - **Fact table**

        1. songplays - records in event data associated with song plays i.e. records with page NextSong
            - songplay_id, start_time (sort_key), user_id, level, song_id (distkey), artist_id, session_id, location, user_agent
    - **Dimension Tables**

        2. users - users in the app (dist all)
            - user_id (sort_key), first_name, last_name, gender, level
        3. songs - songs in music database
            - song_id (sortkey adn distkey), title, artist_id, year, duration
        4. artists - artists in music database (dist all)
            - artist_id (sortkey), name, location, lattitude, longitude
        5. time - timestamps of records in songplays broken down into specific units
            - start_time (sortkey), hour, day, week, month, year, weekday
- The copy from the S3 to the redshift was done using the appropiate JSON formating and the buckets.

## Execution
To execute the project run:
- To drop and create the tables
```python
python create_tables.py
```
- To copy the data from s3 to Redshift and insert into the analytics 
```python
python etl.py
```

## Notes:
- On staging area is better to have all the data and do some data cleaning in 
the other tables
- Looking error inside the redshift cluster with the appropiate stl
- Check timestamp loading on redshift

## Additional Resources and Feedback
### Regarding deststyle

It's okay to use the diststyle all for small tables like users/artists especially if they are used in multiple joins with big partitioned tables. The use of song_id as a dist key for songplays table will cause issues, as some songs are played much more than the others leading to a skewed distribution. So using song_id as a distkey needs prior analysis of the distribution of records/song. A better way for distribution is to use the songplay_id, as it contains a unique value per record, which will mostly ensure good distribution of data without skew. You can also use the EVEN diststyle for songplays table to ensure equal distribution of data among the nodes

### Others
- [2X Your Redshift Speed With Sortkeys and Distkeys]
- [Choosing Best Sort Key/ Dist Key - Official AWS Doc
]

[//]: <> (Links and some external resources.)
[2X Your Redshift Speed With Sortkeys and Distkeys]: https://www.sisense.com/blog/double-your-redshift-performance-with-the-right-sortkeys-and-distkeys/
[Choosing Best Sort Key/ Dist Key - Official AWS Doc]: https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html