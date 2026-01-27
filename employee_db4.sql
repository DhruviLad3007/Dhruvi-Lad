SELECT department
FROM Employee
GROUP BY department
ORDER BY SUM(salary) DESC
LIMIT 1;