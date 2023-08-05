# Найти список студентов в определенной группе.

import sqlite3

q_param=('Illustrator',)

def execute_query(sql: str) -> list:
    with sqlite3.connect("university.db") as con:
        cur = con.cursor()
        cur.execute(sql, q_param)
        return cur.fetchall()


sql = """
SELECT f.name, s.last_name, s.first_name FROM faculties AS f LEFT JOIN main.students s on f.id = s.faculty_id WHERE f.name=?;
"""

if __name__ == "__main__":
    print(execute_query(sql))
