use university;

show full tables;

create view faculty as select id, name, dept_name from instructor;

select * from faculty;

select * from instructor;

insert into faculty values('30765', 'green', 'music');


create view instructor_info as select id, name, building from instructor, department where instructor.dept_name = department.dept_name;

insert into instructor_info values('69987', 'white', 'taylor');

rename table faculty to department;

drop view if exists faculty;
