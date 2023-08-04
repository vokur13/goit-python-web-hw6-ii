-- Список курсов, которые определенному студенту читает определенный преподаватель.

SELECT s1.last_name, s1.first_name, p.last_name, p.first_name, title
FROM students s1
         INNER JOIN main.marks m on s1.id = m.student_id
         INNER JOIN main.subjects s on s.id = m.subject_id
         INNER JOIN main.professors p on p.id = s.professor_id
WHERE s1.id = '?'
  AND p.id = '?';