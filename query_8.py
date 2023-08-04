# Найти средний балл, который ставит определенный преподаватель по своим предметам.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT p.last_name, p.first_name, round(AVG(m.mark), 2) FROM professors p INNER JOIN main.subjects s on p.id = s.professor_id INNER JOIN main.marks m on s.id = m.subject_id GROUP BY p.last_name, p.first_name;
"""

if __name__ == "__main__":
    print(execute_query(sql))
