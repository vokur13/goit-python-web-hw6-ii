-- Найти средний балл в группах по определенному предмету.

SELECT f.name, title, round(AVG(m.mark), 2)
FROM faculties AS f
         INNER JOIN main.students AS s on f.id = s.faculty_id
         INNER JOIN main.marks m on s.id = m.student_id
         INNER JOIN main.faculties f2 on f2.id = s.faculty_id
         INNER JOIN main.subjects s2 on s2.id = m.subject_id
        WHERE title = 'Theatre manager'
GROUP BY f.name, title;