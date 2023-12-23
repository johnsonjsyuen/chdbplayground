from pathlib import Path

import chdb
from chdb.session import Session

db = Session()
db.query("create database db")
db.query("use db")

query_sql = "select * FROM 'crime.csv' INTO OUTFILE 'crime.parquet' FORMAT Parquet SETTINGS input_format_allow_errors_num = 5, input_format_allow_errors_ratio = 0.1"
res = chdb.query(query_sql, "Parquet")
#path = Path("crime.parquet")
#path.write_bytes(res.bytes())

print(res)
print(
    f"{res.rows_read()} rows | "
    f"{res.bytes_read()} bytes | "
    f"{res.elapsed()} seconds"
)