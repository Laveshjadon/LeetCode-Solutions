-- Write your PostgreSQL query statement below
select u.project_id,
    round(avg(v.experience_years), 2) as average_years
from project u
join employee v
    on u.employee_id = v.employee_id
group by u.project_id;



