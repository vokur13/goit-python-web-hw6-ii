# Найти какие курсы читает определенный преподаватель.

import sqlite3

q_param=(2,)


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql, q_param)
        return cur.fetchall()


sql = """
SELECT p.last_name, p.first_name, s.title FROM professors AS p LEFT JOIN main.subjects s on p.id = s.professor_id WHERE p.id=?;
"""

if __name__ == "__main__":
    print(execute_query(sql))
