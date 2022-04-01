# Write your MySQL query statement below

select activity.player_id, device_id
from 
    
    (select player_id, min(event_date) as first_login
    from activity 
    group by player_id) as buf, activity

where buf.player_id = activity.player_id and buf.first_login = activity.event_date
