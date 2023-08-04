# Найти 5 студентов с наибольшим средним баллом по всем предметам.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.last_name, s.first_name, round(AVG(m.mark), 2) FROM students as s LEFT JOIN main.marks m ON s.id = m.student_id GROUP BY s.id ORDER BY round(AVG(m.mark), 2) DESC LIMIT 5;
"""

if __name__ == "__main__":
    print(execute_query(sql))
