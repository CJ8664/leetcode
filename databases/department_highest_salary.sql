# Promblem URL https://leetcode.com/problems/department-highest-salary/description/

# Write your MySQL query statement below

SELECT 
    dep.name as Department,
    emp.name as Employee,
    max_dep.Salary
FROM
    ( 
        SELECT 
            DepartmentId,
            MAX(Salary) as Salary
        FROM Employee emp
        GROUP BY DepartmentId
    ) max_dep
INNER JOIN Department dep on max_dep.DepartmentId = dep.Id
INNER JOIN Employee emp on emp.Salary = max_dep.Salary and emp.DepartmentId = dep.Id
ORDER BY max_dep.Salary
