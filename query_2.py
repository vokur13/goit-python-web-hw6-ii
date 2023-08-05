# Найти студента с наивысшим средним баллом по определенному предмету.

import sqlite3

q_param = ("Ophthalmologist",)


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql, q_param)
        return cur.fetchall()


sql = """
SELECT s.last_name, s.first_name, f.name, (round(AVG(m.mark), 2)) FROM students AS s INNER JOIN main.faculties AS f ON f.id = s.faculty_id INNER JOIN main.marks m ON s.id = m.student_id WHERE f.name=? GROUP BY f.name;
"""

if __name__ == "__main__":
    print(execute_query(sql))
