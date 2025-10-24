import duckdb, os, pathlib

class Warehouse:
    def __init__(self, path: str):
        self.path = path
        pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.con = duckdb.connect(path)

    def write_df(self, df, table: str, mode: str = "append"):
        self.con.execute(f'CREATE TABLE IF NOT EXISTS {table} AS SELECT * FROM df LIMIT 0')
        if mode == "replace":
            self.con.execute(f'DELETE FROM {table}')
        self.con.register("df", df)
        self.con.execute(f'INSERT INTO {table} SELECT * FROM df')
        self.con.unregister("df")

    def query(self, sql: str):
        return self.con.execute(sql).df()
