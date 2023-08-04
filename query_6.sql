-- Найти список студентов в определенной группе.

SELECT f.name, s.last_name, s.first_name
FROM faculties AS f
         LEFT JOIN main.students s on f.id = s.faculty_id
WHERE f.name = '?';