# Write your MySQL query statement below
select name, bonus
from Employee natural left outer join Bonus
where bonus < 1000 or bonus is null