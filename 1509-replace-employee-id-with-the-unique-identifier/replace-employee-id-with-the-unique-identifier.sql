-- Write your PostgreSQL query statement below
select uni.unique_id,e.name
from employees e
left join employeeuni uni
using(id);
