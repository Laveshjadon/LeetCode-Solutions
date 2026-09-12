-- Write your PostgreSQL query statement below
select a.name
from employee a
where a.id in (
    select managerid
    from employee
    group by managerid
    having count(*) >= 5);
