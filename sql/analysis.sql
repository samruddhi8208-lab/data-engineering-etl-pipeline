-- Employee and Order Join

SELECT
    e.employee_id,
    e.name,
    e.department,
    e.city,
    e.salary,
    o.order_id,
    o.product,
    o.quantity,
    o.price,
    o.total_amount
FROM employees e
JOIN orders o
ON e.employee_id = o.employee_id;


-- Department-wise order summary

SELECT
    e.department,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_sales,
    AVG(o.total_amount) AS average_order_value
FROM employees e
JOIN orders o
ON e.employee_id = o.employee_id
GROUP BY e.department;
