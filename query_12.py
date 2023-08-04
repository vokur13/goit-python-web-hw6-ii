# Оценки студентов в определенной группе по определенному предмету на последнем занятии.

import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s1.last_name, s1.first_name, f.name, s.title, m.mark, max(m.date_of) FROM marks m INNER JOIN main.subjects s on s.id = m.subject_id INNER JOIN main.students s1 on s1.id = m.student_id INNER JOIN main.faculties f on f.id = s1.faculty_id WHERE f.name='?' AND s.title='?';
"""

if __name__ == "__main__":
    print(execute_query(sql))
