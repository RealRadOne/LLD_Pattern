--Data Lemur problem: https://datalemur.com/questions/odd-even-measurements--

WITH RANK_CTE AS 
(
SELECT 
  measurement_id,
  measurement_value,
  measurement_time::DATE as measurement_day,
  RANK() OVER
    (PARTITION BY measurement_time::DATE ORDER BY measurement_time::TIME) 
  AS rank_time
FROM 
  measurements
),
ODD_CTE AS 
(
SELECT 
  measurement_day,
  SUM(measurement_value) AS odd_sum
FROM
  RANK_CTE
WHERE 
  rank_time IN(1,3,5)
GROUP BY 
  measurement_day
),
EVEN_CTE AS 
(
SELECT 
  measurement_day,
  SUM(measurement_value) AS even_sum
FROM
  RANK_CTE
WHERE 
  rank_time IN(2,4,6)
GROUP BY 
  measurement_day
)
SELECT 
  ODD_CTE.measurement_day as measurement_day,
  ODD_CTE.odd_sum,
  EVEN_CTE.even_sum
FROM
  ODD_CTE
JOIN
  EVEN_CTE 
ON
  ODD_CTE.measurement_day = EVEN_CTE.measurement_day
ORDER BY measurement_day ASC;