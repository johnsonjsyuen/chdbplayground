from pathlib import Path

import chdb
from chdb.session import Session

db = Session()
db.query("create database db")
db.query("use db")

# Create table
create_table_sql = "create table crime Engine=Log as select * FROM file('crime.parquet')"
res = db.query(create_table_sql, "Pretty")

# Query 1
query_sql = "describe table crime"
res = db.query(query_sql, "Pretty")
print(res)
print(
    f"{res.rows_read()} rows | "
    f"{res.bytes_read()} bytes | "
    f"{res.elapsed()} seconds"
)

# Query 2
query_sql = "select count(LOCATION) as num, LOCATION FROM crime group by LOCATION order by num DESC"
res = db.query(query_sql, "Pretty")
print(res)
print(
    f"{res.rows_read()} rows | "
    f"{res.bytes_read()} bytes | "
    f"{res.elapsed()} seconds"
)