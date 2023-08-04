-- Найти оценки студентов в отдельной группе по определенному предмету.

SELECT s.last_name, s.first_name, f.name, title, m.mark
FROM students AS s
         INNER JOIN main.marks m on s.id = m.student_id
         INNER JOIN main.faculties f on f.id = s.faculty_id
         INNER JOIN main.subjects s2 on s2.id = m.subject_id
         INNER JOIN main.marks m2 on s.id = m2.student_id
WHERE f.name = '?'
  AND title = '?';