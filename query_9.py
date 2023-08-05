# Найти список курсов, которые посещает определенный студент.

import sqlite3

q_param = (25,)


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql, q_param)
        return cur.fetchall()


sql = """
SELECT s.last_name, s.first_name, title FROM students s INNER JOIN main.marks m on s.id = m.student_id INNER JOIN main.subjects s2 on s2.id = m.subject_id WHERE s.id=? GROUP BY s.last_name, s.first_name, title;
"""

if __name__ == "__main__":
    print(execute_query(sql))
