-- Write your PostgreSQL query statement below
select a.user_id ,round(avg(
    case 
        
        when b.action = 'confirmed' then 1
        else 0
    end
    
    ),2) as confirmation_rate
from signups a
left join Confirmations b
    On a.user_id = b.user_id
group by a.user_id




