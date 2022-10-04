use university;



select * from course;

-- 1
select title
from course as c
where c.title in (
	select title
    from course as t
    where t.dept_name = 'Comp. Sci.'
) and c.credits = 3;


select * from student;

select * from instructor;

select * from advisor;


-- 2
select distinct s_id
from advisor as a
where a.i_id in (
	select id
    from instructor as i
    where i.name = 'Einstein'
);

-- 3
select salary
from instructor as i
having i.salary = (
	select max(salary)
    from instructor
);

-- 3.1 มากสุดของแต่ละ department
select dept_name, max(salary)
from instructor
group by dept_name;


-- 4
select name
from instructor
where salary = (
	select max(salary)
    from instructor
);


select * from section;

select * from student;

select * from takes;

-- 5
select count(*) as enrollment
from takes
where (semester, year) in (
	select semester, year
    from takes
    where semester = 'Fall' and year = 2009
);

-- 6
select count(*) as enrollment, course_id
from takes
where (semester, year) in (
	select semester, year
    from takes
    where semester = 'Fall' and year = 2009
) group by course_id
order by enrollment desc
limit 1;


