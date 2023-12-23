from pathlib import Path

import chdb
from chdb.session import Session

db = Session()
db.query("create database db")
db.query("use db")

create_table_sql = "create table crime Engine=Log as select * FROM file('crime.parquet')"
res = db.query(create_table_sql, "Pretty")
query_sql = "select * FROM crime limit 2"
res = db.query(query_sql, "Pretty")


print(res)
print(
    f"{res.rows_read()} rows | "
    f"{res.bytes_read()} bytes | "
    f"{res.elapsed()} seconds"
)