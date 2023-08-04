-- Найти какие курсы читает определенный преподаватель.

SELECT p.last_name, p.first_name, s.title
FROM professors AS p
         LEFT JOIN main.subjects s on p.id = s.professor_id;