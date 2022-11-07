use university;


-- 1
select title
from course as c
where c.title in (
	select title
    from course as t
    where t.dept_name = 'Comp. Sci.'
) and c.credits = 3;


-- 2
select distinct s_id
from advisor as a
where a.i_id in (
	select id
    from instructor as i
    where i.name = 'Einstein'
);


-- 3
select name, salary
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


-- 5
select course_id, count(*) as enrollment
from takes
where (semester, year) in (
	select semester, year
    from takes
    where semester = 'Fall' and year = 2009
) group by course_id;


-- 6
select count(*) as enrollment
from takes
where (semester, year) in (
	select semester, year
    from takes
    where semester = 'Fall' and year = 2009
) group by course_id
order by enrollment desc
limit 1;

-- 7
select course_id, count(*) as enrollment
from takes
where (semester, year) in (
	select semester, year
    from takes
    where semester = 'Fall' and year = 2009
) group by course_id
order by enrollment desc
limit 1;



---------- page 2 ---------


-- 1
-- รันไม่ได้เพราะ constraint กำหนดให้ credits มากกว่า 0 
insert into course values ('CS-001', 'Weekly Seminar', 'Comp. Sci.', '0');


-- 2
insert into section values ('CS-001', '1', 'Fall', '2017', 'Packard', '101', 'H');


-- 3
insert into takes(id, course_id, sec_id, semester, year)
select distinct id, course_id, sec_id, semester, year
from student, section
where student.dept_name = 'Comp. Sci.' and section.course_id = 'CS-001';


-- 4
delete from takes
where id = (
	select id 
    from student
    where name = 'Chavez'
);


-- 5
-- จริงๆมันน่าจะเกิดปัญหาขึ้น เพราะว่า table ที่ถูกเชื่อม foreignkey มันหา key ไม่เจอ วิธีแก้คือใส่ function on delete 
delete from course
where course_id = 'CS-001';


-- 6
delete from takes
where course_id = (
	select course_id
    from course
    where title like '%database_%' or title like '%_database%'
);

