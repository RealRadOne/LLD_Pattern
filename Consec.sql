--Use of LEAD and LAG:https://leetcode.com/problems/consecutive-numbers/description/ --

WITH 
    num_data 
AS
(
SELECT
    LAG(num) OVER() as prev,
    num,
    LEAD(num) OVER() as nxt
FROM 
    logs
)

SELECT 
DISTINCT
    num 
AS 
    ConsecutiveNums
FROM 
    num_data 
WHERE 
    (num=prev) 
AND 
    (num=nxt);