# Список курсов, которые определенному студенту читает определенный преподаватель.

import sqlite3

q_param = (3, 2)


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql, q_param)
        return cur.fetchall()


sql = """
SELECT s1.last_name, s1.first_name, p.last_name, p.first_name, title FROM students s1 INNER JOIN main.marks m on s1.id = m.student_id INNER JOIN main.subjects s on s.id = m.subject_id INNER JOIN main.professors p on p.id = s.professor_id WHERE s1.id=? AND p.id=?;
"""

if __name__ == "__main__":
    print(execute_query(sql))
