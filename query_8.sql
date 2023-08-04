-- Найти средний балл, который ставит определенный преподаватель по своим предметам.

SELECT p.last_name, p.first_name, round(AVG(m.mark), 2)
FROM professors p
         INNER JOIN main.subjects s on p.id = s.professor_id
         INNER JOIN main.marks m on s.id = m.subject_id
GROUP BY p.last_name, p.first_name;