import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays cascade;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
  artist          varchar,
  auth            varchar,
  firstName       varchar,
  gender          varchar,
  itemInSession   integer,
  lastName        varchar,
  length          double precision,
  level           varchar,
  location        varchar,
  method          varchar,
  page            varchar,
  registration    timestamp,
  sessionId       integer,
  song            varchar,
  status          integer,
  ts              timestamp,
  userAgent       varchar,
  userId          bigint         
);
""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
  num_songs         integer,
  artist_id         varchar,
  artist_latitude   numeric, 
  artist_longitude  numeric, 
  artist_location   varchar, 
  artist_name       varchar,
  song_id           varchar,
  title             varchar,
  duration          double precision,
  year              integer
);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
  songplay_id    bigint       IDENTITY(0,1) not null,
  start_time     timestamp    not null sortkey,
  user_id        bigint       not null,
  level          varchar(4)   not null,
  song_id        varchar(30)  not null distkey,
  artist_id      varchar(30)  not null,
  session_id     integer      not null,
  location       varchar,
  user_agent     varchar,
  PRIMARY KEY(songplay_id),
  FOREIGN KEY(start_time) REFERENCES time(start_time),
  FOREIGN KEY(user_id) REFERENCES users(user_id));
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
  user_id     bigint       not null sortkey,
  first_name  varchar(30)  not null,
  last_name   varchar(30)  not null,
  gender      varchar(1)   not null,
  level       varchar(4)   not null,
  PRIMARY KEY(user_id))
  diststyle all;
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
  song_id     varchar            not null distkey sortkey,
  title       varchar            not null,
  artist_id   varchar            not null,
  year        integer            not null,
  duration    double precision   not null,
  PRIMARY KEY(song_id));
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
  artist_id    varchar   not null sortkey,
  name         varchar   not null,
  location     varchar,
  latitude     numeric,
  longitude    numeric,
  PRIMARY KEY(artist_id))
  diststyle all;
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
  start_time    timestamp   not null sortkey,
  hour          integer     not null,
  day           integer     not null,
  week          integer     not null,
  month         integer     not null,
  year          integer     not null,
  weekday       integer     not null,
  PRIMARY KEY(start_time));
""")

# STAGING TABLES
staging_events_copy = ("""
copy staging_events 
from {}
credentials 'aws_iam_role={}'
json {}
region 'us-west-2'
timeformat 'epochmillisecs';
""").format(config.get("S3","LOG_DATA"),
            config.get("IAM_ROLE","ARN"),
            config.get("S3","LOG_JSONPATH"))

staging_songs_copy = ("""
copy staging_songs 
from {}
credentials 'aws_iam_role={}'
json 'auto'
region 'us-west-2';
""").format(config.get("S3","SONG_DATA"),
            config.get("IAM_ROLE","ARN"))

############################### FINAL TABLES #############################
songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, 
    user_id, 
    level, 
    song_id,
    artist_id,
    session_id,
    location,
    user_agent)
SELECT 
    se.ts,
    se.userId,
    se.level,
    ss.song_id,
    ss.artist_id,
    se.sessionId,
    se.location,
    se.userAgent
FROM
    staging_events as se,
    staging_songs as ss
WHERE
    se.artist = ss.artist_name AND
    se.song = ss.title
""")

user_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level)
SELECT DISTINCT 
    se.userId,
    se.firstName,
    se.lastName,
    se.gender,
    se.level
FROM 
    staging_events as se
WHERE
    se.userId is not null;
""")

song_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title, 
    artist_id, 
    year, 
    duration)
SELECT DISTINCT 
    ss.song_id,
    ss.title,
    ss.artist_id,
    ss.year,
    ss.duration
FROM 
    staging_songs as ss
WHERE
    ss.song_id is not null;
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_id, 
    name, 
    location, 
    latitude, 
    longitude)
SELECT DISTINCT 
    ss.artist_id,
    ss.artist_name,
    ss.artist_location,
    ss.artist_latitude,
    ss.artist_longitude
FROM 
    staging_songs as ss
WHERE
    ss.artist_id is not null;
""")

time_table_insert = ("""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month,
    year,
    weekday)
SELECT DISTINCT
    se.ts,
    EXTRACT(h from se.ts),
    EXTRACT(d from se.ts),
    EXTRACT(w from se.ts),
    EXTRACT(mon from se.ts),
    EXTRACT(y from se.ts),
    EXTRACT(weekday from se.ts)
FROM 
    staging_events as se
""")

# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [user_table_insert, song_table_insert, artist_table_insert, time_table_insert, songplay_table_insert]