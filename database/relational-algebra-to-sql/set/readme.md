<img src="../assets/union.png"/>

```sql
select course_id
from section
when semester='Fall' and year=2017
union
select course_id
from section
when semester='spring' and year=2018
```
