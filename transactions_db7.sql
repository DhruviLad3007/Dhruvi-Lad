START TRANSACTION;

UPDATE accounts
SET balance = balance - 1000
WHERE acc_no = 101;

UPDATE accounts 
SET balance = balance - 1000
WHERE acc_no = 102;

COMMIT;