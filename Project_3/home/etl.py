import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Loading the s3 data to redshift into staging tables,
    execute the queries in copy_table_queries
    
    Parameters
    ----------
    cur : cursos object
    conn: connection to the database in redshift
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()
    print("Loaded")


def insert_tables(cur, conn):
    """
    Insert the data from the staging tables into the star schema for anylitics
    execute the queries in insert_table_queries
    
    Parameters
    ----------
    cur : cursos object
    conn: connection to the database in redshift
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()
    print("Inserted")


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()