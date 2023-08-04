-- Найти 5 студентов с наибольшим средним баллом по всем предметам.

SELECT s.last_name, s.first_name, round(AVG(m.mark), 2)
FROM students AS s
         LEFT JOIN main.marks m ON s.id = m.student_id
GROUP BY s.id
ORDER BY round(AVG(m.mark), 2) DESC
LIMIT 5;