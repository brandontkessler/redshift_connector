# easy connect and query for postgres/redshift

## Example

#### setup

From terminal:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv)$ pip install sqlalchemy
(venv)$ pip install psycopg2-binary
(venv)$ pip install pandas
```

#### Usage

From py file:

```
>>> import json
>>> from db_connect import DB

>>> with open('./creds.json') as f:
        creds = json.load(f)

>>> db = DB(creds["username"], creds["password"], creds["host"], creds["port"], creds["dbname"])
>>> data = db.query("select * from my_sql_table limit 10")
>>> data.head()
```
