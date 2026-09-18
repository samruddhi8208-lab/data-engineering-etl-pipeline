-- Employees with salary greater than 70000

SELECT *
FROM employees
WHERE salary > 70000;


-- Average salary by department

SELECT
    department,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department;


-- Total order amount by department

SELECT
    e.department,
    SUM(o.total_amount) AS total_order_amount
FROM employees e
JOIN orders o
ON e.employee_id = o.employee_id
GROUP BY e.department;


-- Top 3 employees by total order amount

SELECT
    e.employee_id,
    e.name,
    SUM(o.total_amount) AS total_order_amount
FROM employees e
JOIN orders o
ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.name
ORDER BY total_order_amount DESC
LIMIT 3;
