--SQL Lemur problem: https://datalemur.com/questions/sql-well-paid-employees--

SELECT
  e.employee_id,
  e.name
FROM 
  employee AS e 
INNER JOIN
  employee AS m 
ON e.manager_id = m.employee_id
WHERE e.salary>m.salary;