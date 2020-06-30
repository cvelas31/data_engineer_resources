from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator, SqlDataQualityOperator,
                                LoadDimensionOperator, LengthDataQualityOperator, PostgresOperator)
from helpers import SqlQueries
import sql_statements

# INPUTS
AWS_KEY = "AKIAWA7DVV6T7XTCRP3O" #os.environ.get('AWS_KEY')
AWS_SECRET = "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" #os.environ.get('AWS_SECRET')
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
    table="users",
    sql_query=SqlQueries.user_table_insert,
    truncate=True
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="songs",
    sql_query=SqlQueries.song_table_insert,
    truncate=True
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="artists",
    sql_query=SqlQueries.artist_table_insert,
    truncate=True
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    table="time",
    sql_query=SqlQueries.time_table_insert,
    truncate=True
)

run_quality_checks = LengthDataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    redshift_conn_id=redshift_conn_id,
    tables=["songplays", "users", "songs", "artists", "time"],
)

list_tests = [{"query": "SELECT COUNT(*) FROM users WHERE userid IS NULL;", 
               "expected_result": 0}, 
              {"query": "SELECT COUNT(*) FROM songs WHERE song_id IS NULL;", 
               "expected_result": 0},
              {"query": "SELECT COUNT(*) FROM artists WHERE artist_id IS NULL;",
               "expected_result": 0}]

run_query_quality_checks = SqlDataQualityOperator(
    task_id='Run_query_data_quality_checks',
    dag=dag,
    redshift_conn_id=redshift_conn_id, 
    list_tests=list_tests)

end_operator = DummyOperator(task_id='Stop_execution', dag=dag)


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

run_quality_checks >> run_query_quality_checks >> end_operator