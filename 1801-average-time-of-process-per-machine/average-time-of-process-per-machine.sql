select e.machine_id , round(avg(w.timestamp - e.timestamp), 3) as processing_time
from activity e
left join activity w
    on e.machine_id = w.machine_id
    and e.process_id = w.process_id
where  e.activity_type = 'start'
    and w.activity_type = 'end'
group by e.machine_id;

