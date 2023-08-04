-- Найти список курсов, которые посещает определенный студент.

SELECT s.last_name, s.first_name, title
FROM students s
         INNER JOIN main.marks m on s.id = m.student_id
         INNER JOIN main.subjects s2 on s2.id = m.subject_id
WHERE s.last_name = '?'
  AND s.first_name = '?'
GROUP BY s.last_name, s.first_name, title;