SELECT * 
FROM Employee
WHERE department = (
  SELECT department
  FROM Employee
  WHERE emp_name = 'Amit'
)