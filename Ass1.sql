CREATE TABLE  students(
  student_id INT,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT
)

INSERT INTO students VALUES
(1, 'Aahana', 'CSE', 1 , 82),
(2, 'Riya',   'IT', 4 , 74),
(3, 'Ruchi', 'CSE', 3 , 91),
(4, 'Astha', 'ECE', 2 , 68),
(5, 'Stuti', 'CSE', 1 , 88);

SELECT * FROM students;

SELECT name, department
FROM students;

SELECT *
FROM students
WHERE marks > 75;

SELECT *
FROM students
WHERE department = 'CSE';

SELECT *
FROM students
ORDER BY marks DESC;

SELECT * 
FROM students
ORDER BY marks DESC
LIMIT 3;