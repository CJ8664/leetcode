# Problem URL : https://leetcode.com/problems/combine-two-tables/description/

# Write your MySQL query statement below

SELECT 
    FirstName, 
    LastName, 
    City, 
    State
FROM
    Person pers
    LEFT JOIN Address addr on pers.PersonId = addr.PersonId
