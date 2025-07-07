--Leetcode hard SQL:https://leetcode.com/problems/department-top-three-salaries/--
WITH employee_money AS 
(
SELECT 
    employee.id,
    employee.name,
    employee.salary,
    department.name as department,
    RANK() OVER (PARTITION BY employee.departmentId ORDER by employee.salary DESC) as salary_rank
FROM 
    employee
JOIN 
    department
ON 
    employee.departmentId = Department.id
)
SELECT
    department as Department,
    name as Employee,
    salary as Salary
FROM
    employee_money
WHERE 
    salary_rank IN(1,2,3);
