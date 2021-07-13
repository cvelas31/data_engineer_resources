from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LengthDataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id,
                 tables,
                 *args, **kwargs):

        super(LengthDataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        assert len(tables)>0, "Tables must contain at least one table name"
        self.tables = tables

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        errors_list = []
        for table in self.tables:
            records = redshift.get_records(f"SELECT COUNT(*) FROM {table}")
            if len(records) < 1 or len(records[0]) < 1:
                errors_list.append(f"Data quality check failed. {table} returned no results")
            num_records = records[0][0]
            if num_records < 1:
                errors_list.append(f"Data quality check failed. {table} contained 0 rows")
        if len(errors_list)>0:
            paragraph = "This was the list of errors encountered:\n"
            for error in errors_list:
                paragraph+=f"   - {error}\n"
            raise ValueError(paragraph)
        self.log.info('LengthDataQualityOperator passed')
        
class SqlDataQualityOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 redshift_conn_id,
                 list_tests,
                 *args, **kwargs):
        super(SqlDataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.list_tests = list_tests

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        errors_list = []
        for test in self.list_tests:
            records = redshift.get_records(test["query"])
            if records[0][0] != test["expected_result"]:
                errors_list.append(f"Data quality check failed on {test['query']}. {records[0][0]} is different from {test['expected_result']}.")
        if len(errors_list)>0:
            paragraph = "This was the list of errors encountered:\n"
            for error in errors_list:
                paragraph+=f"   - {error}\n"
            raise ValueError(paragraph)
        self.log.info('SqlDataQualityOperator passed')