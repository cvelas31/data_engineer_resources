from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator, PostgresOperator)
from helpers import SqlQueries
import sql_statements

# INPUTS
AWS_KEY = os.environ.get('AWS_KEY')
AWS_SECRET = os.environ.get('AWS_SECRET')
aws_credentials_id = "aws_credentials" # Name in connections
redshift_conn_id = "redshift" # Name in connections
s3_bucket = "udacity-dend"

# Log data
log_s3_key = "log_data"
log_stage_table = "staging_events"
log_json_format = "s3://udacity-dend/log_json_path.json"

# Song data
song_s3_key = "song_data"
song_stage_table = "staging_songs"
song_json_format = "auto"


default_args = {
    'owner': 'udacity',
    'start_date': datetime(2019, 1, 12),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='0 * * * *', 
          catchup = False # Perform scheduler catchup (or only run latest)? Defaults to True
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

create_tables = PostgresOperator(task_id="create_tables",
                                 dag=dag,
                                 postgres_conn_id=redshift_conn_id,
                                 sql=sql_statements.CREATE_TABLES)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    redshift_conn_id=redshift_conn_id, 
    aws_credentials_id=aws_credentials_id,
    s3_bucket=s3_bucket, 
    s3_key=log_s3_key,
    table=log_stage_table, 
    json_format=log_json_format,
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag,
    redshift_conn_id=redshift_conn_id, 
    aws_credentials_id=aws_credentials_id,
    s3_bucket=s3_bucket, 
    s3_key=song_s3_key,
    table=song_stage_table, 
    json_format=song_json_format,
)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="songplays",
    sql_query=SqlQueries.songplay_table_insert
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="user",
    sql_query=SqlQueries.user_table_insert
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="song",
    sql_query=SqlQueries.song_table_insert
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="artist",
    sql_query=SqlQueries.artist_table_insert
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="time",
    sql_query=SqlQueries.time_table_insert
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    tables=["songplays", "user", "song", "artist", "time"],
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


# DAG
start_operator >> create_tables

create_tables >> stage_events_to_redshift
create_tables >> stage_songs_to_redshift

stage_events_to_redshift >> load_songplays_table
stage_songs_to_redshift >> load_songplays_table

load_songplays_table >> load_user_dimension_table
load_songplays_table >> load_song_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table

load_user_dimension_table >> run_quality_checks
load_song_dimension_table >> run_quality_checks
load_artist_dimension_table >> run_quality_checks
load_time_dimension_table >> run_quality_checks

run_quality_checks >> end_operator