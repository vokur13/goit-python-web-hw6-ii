-- Найти средний балл на потоке (по всей таблице оценок).

SELECT round(AVG(m.mark), 2)
FROM marks AS m;