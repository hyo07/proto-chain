import sqlite3
from contextlib import closing


dbname = "block_to_db.db"


def block_to_db(block_chain: list):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        create_table = "CREATE TABLE db_cahin (key INTEGER PRIMARY KEY AUTOINCREMENT, value CHAR UNIQUE)"

        try:
            c.execute(create_table)
        except sqlite3.OperationalError:
            pass

        count_comm = "SELECT * FROM db_cahin"
        c.execute(count_comm)
        db_len = len(c.fetchall())
        print("db_len>>>>>>>>>>>>", db_len, type(db_len))

        sql_comm ="INSERT INTO db_cahin (value) VALUES (?)"

        for block in block_chain[db_len:]:
            try:
                c.execute(sql_comm, (str(block),))
            except sqlite3.IntegrityError:
                print("もうあるよ！！！")
                pass

        conn.commit()
        print("DBに保存しました！！！！！！")
