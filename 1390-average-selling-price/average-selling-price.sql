select 
    u.product_id , 
    COALESCE(
        ROUND(SUM(u.price * v.units)::numeric / SUM(v.units),2),
        0
        ) AS average_price
from prices u
left join Unitssold v
    on u.product_id = v.product_id
    and purchase_date between start_date and end_date

group by u.product_id;

