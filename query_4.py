# Найти средний балл на потоке (по всей таблице оценок).

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT round(AVG(m.mark), 2) FROM marks AS m;
"""

if __name__ == "__main__":
    print(execute_query(sql))
