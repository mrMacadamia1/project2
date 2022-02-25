-- CREATE TABLE students (

-- 	first_name TEXT,
-- 	last_name TEXT,
-- 	age INTEGER

-- );

-- CREATE TABLE employees (

-- 	first_name TEXT,
-- 	last_name TEXT,
-- 	age INTEGER

-- );




-- CRUD - Create, Read, Update, Delete

-- Create

INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 18);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 19);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 17);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 19);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jack", "White", 18);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jane", "Black", 19);
INSERT INTO employees (first_name, last_name, age) VALUES ("Jim", "Brown", 17);
INSERT INTO employees (first_name, last_name, age) VALUES ("Janet", "Rose", 19);

-- -- Read

-- SELECT * FROM employees;
-- SELECT first_name FROM employees;
-- SELECT first_name, age FROM employees;
-- SELECT first_name, age FROM employees WHERE first_name = "Jack";
-- SELECT first_name, age FROM employees WHERE first_name IS "Jack";
-- SELECT first_name, age FROM employees WHERE age IS 19;
-- SELECT last_name, age FROM employees WHERE last_name IS NOT "Black";
-- SELECT last_name, age FROM employees WHERE last_name IS NOT "Black" AND age IS NOT 17;
-- SELECT last_name, age FROM employees WHERE age < 18;
-- SELECT first_name, age FROM employees WHERE first_name LIKE "Ja%";
-- SELECT * FROM employees WHERE first_name LIKE "%ck" OR last_name LIKE "%ck";
-- SELECT * FROM employees WHERE first_name LIKE "%an%";

-- -- Update

-- UPDATE employees SET first_name="Jimm" WHERE first_name="Jim";
-- UPDATE employees SET age=20;
-- UPDATE employees SET first_name="Jim", age=19 WHERE first_name="Jimm";
-- UPDATE employees SET age=18 WHERE first_name="Jane" OR last_name="White";

-- -- Delete

-- DELETE FROM employees WHERE age=20;
-- DELETE FROM employees WHERE age=18 AND last_name="White";
-- DELETE FROM employees;








