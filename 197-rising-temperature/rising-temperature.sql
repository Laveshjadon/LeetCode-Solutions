-- Write your PostgreSQL query statement below
select w1.id 
from Weather w1
join Weather w2
    ON w2.recordDate = w1.recordDate - INTERVAL '1 day'
WHERE w1.temperature > w2.temperature;
