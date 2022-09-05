use university;


-- SELECT * FROM student NATURAL LEFT OUTER JOIN takes;
-- rewrite 1
select *
from student
left join takes 
using(id);

-- SELECT * FROM student NATURAL RIGHT OUTER JOIN takes;
-- rewrite 2
select *
from student
right join takes
using(id);


-- homework 1
select i.id, i.name, count(s.sec_id)
from instructor as i
natural join teaches as t 
natural join section as s
group by i.id;


-- homework 2
select s.course_id, i.name
from section as s
natural join teaches as t 
natural join instructor as i
where s.semester = 'Spring' and s.year = '2010';

-- homework 3
select d.dept_name, count(i.name)
from department as d
natural join instructor as i
group by d.dept_name;



-- example table query
select * from instructor;

select * from teaches;

select * from section;

select * from department;

