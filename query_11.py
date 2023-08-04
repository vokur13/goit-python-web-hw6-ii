# Средний балл, который определенный преподаватель ставит определенному студенту.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s2.last_name, s2.first_name, p.last_name, p.first_name, round(AVG(m.mark), 2) FROM marks m INNER JOIN main.subjects s on s.id = m.subject_id INNER JOIN main.professors p on p.id = s.professor_id INNER JOIN main.students s2 on s2.id = m.student_id WHERE s2.last_name='?' AND p.last_name='?';
"""

if __name__ == "__main__":
    print(execute_query(sql))
