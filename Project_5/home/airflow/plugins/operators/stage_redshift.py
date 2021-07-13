from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook

class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    
    copy_sql = """COPY {table} 
                  FROM '{s3_path}' 
                  ACCESS_KEY_ID '{access_key}' 
                  SECRET_ACCESS_KEY  '{secret_key}' 
                  JSON '{json_format}' 
                  TIMEFORMAT as 'epochmillisecs';"""
    
    @apply_defaults
    def __init__(self, redshift_conn_id, aws_credentials_id, 
                 table, s3_bucket, s3_key, json_format="auto",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.table = table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.json_format = json_format

    def execute(self, context):
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        self.log.info("Clearing data from destination Redshift table")
        redshift.run("DELETE FROM {}".format(self.table))
        
        self.log.info("Copying data from S3 to Redshift")
        s3_path = "s3://{}/{}".format(self.s3_bucket, self.s3_key)
        sql_w_format = StageToRedshiftOperator.copy_sql.format(table=self.table, s3_path=s3_path, 
                                                access_key=credentials.access_key, 
                                                secret_key=credentials.secret_key,
                                                json_format=self.json_format)
        redshift.run(sql_w_format)
        self.log.info('StageToRedshiftOperator executed')
        





