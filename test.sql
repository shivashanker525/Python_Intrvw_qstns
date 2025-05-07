SELECT *, COUNT(*) AS duplicate_count
FROM employees
GROUP BY name, department
HAVING COUNT(*) > 1;
 
SELECT product_name, sum(quantity) as total_quantity
FROM sales
GROUP BY product_name
HAVING total_quantity > 30;