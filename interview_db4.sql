DELETE FROM employee
WHERE emp_id NOT IN (
    SELECT MIN(emp_id)
    FROM employee
    GROUP BY emp_name, salary
);
