SELECT DISTINCT l1.value
FROM logs l1
JOIN logs l2
ON l1.id = l2.id - 1
WHERE l1.value = l2.value;
