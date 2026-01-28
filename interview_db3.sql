--nth highest salary
SELECT salary
FROM employee
WHERE salary = (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
);

