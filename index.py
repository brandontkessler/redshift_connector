from sqlalchemy import create_engine
import pandas as pd

class DB:
    """
    Connect to redshift database

    Example:
    >>> import json
    >>> from db_connect import DB

    >>> with open('./creds.json') as f:
            creds = json.load(f)

    >>> db = DB(creds["username"], creds["password"], creds["host"], creds["port"], creds["dbname"])
    >>> df = db.query("select * from my_sql_table limit 10")
    """

    def __init__(self, username, password, host, port, dbname, dtype='postgresql'):
        self.conn = self.connect(username, password, host, port, dbname, dtype)

    def connect(self, user, pw, host, port, dbname, dtype):
        connector = f'{dtype}://{user}:{pw}@{host}:{port}/{dbname}'
        conn = create_engine(connector)
        return conn

    def query(self, query_string):
        df = pd.read_sql_query(query_string, self.conn)
        return df
