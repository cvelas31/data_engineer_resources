from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'+
    insert_into_sql = """TRUNCATE {table};
                         INSERT INTO {table} 
                         {sql_query}
                      """

    @apply_defaults
    def __init__(self,
                 redshift_conn_id,
                 table,
                 sql_query,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_query = sql_query

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        sql_w_format = LoadDimensionOperator.insert_into_sql.format(table=self.table, 
                                                               sql_query=self.sql_query)
        redshift.run(sql_w_format)
        self.log.info(f'LoadDimensionOperator on {self.table} done')
