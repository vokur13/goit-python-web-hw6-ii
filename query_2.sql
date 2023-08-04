-- Найти студента с наивысшим средним баллом по определенному предмету.

SELECT s.last_name, s.first_name, f.name, (round(AVG(m.mark), 2))
FROM students AS s
         INNER JOIN main.faculties AS f ON f.id = s.faculty_id
         INNER JOIN main.marks m ON s.id = m.student_id
GROUP BY f.name;