SELECT COUNT(*) AS total_students
FROM students;

SELECT AVG(marks) AS average_marks
FROM students;

SELECT
    MAX(marks) AS highest_marks,
	MIN(marks) AS lowest_marks
FROM students;

SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department;

SELECT department, AVG(marks) AS avg_marks
FROM students
GROUP BY department
HAVING AVg(marks) > 70;