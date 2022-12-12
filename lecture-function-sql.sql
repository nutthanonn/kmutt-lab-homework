use university;

select concat('css225', 'is', 'easy') as res;
select concat(name, ' come from ', dept_name, ' department.') from instructor;

select upper('css225') as upperResult;
select ucase(name) from instructor;

select lower('css225') as lowerResult;
select lcase(name) from instructor;

select substr('css225 is easy', 1, 2) as res; -- ติดลบได้ เป็นทศนิยมได้มันจะปัดขึ้น(.5+)ปัดลง(<0.5) length must be positive
select substr(name, 1, 3) from instructor;

select replace('css225 is easy', '225', '222') as res;
select replace(dept_name, '.', '') from instructor;

select trim('     css225 is easy      ') as res;
select ltrim('    css225 is easy      ') as res;
select rtrim('    css225 is easy      ') as res;

select length('css225 is easy') as res;
select length('    css225 is easy   ') as res;

select lpad('css225 is easy', 25, '.') as res;
select rpad('css225 is easy', 25, '') as res; -- ทำให้เป็นว่างๆ 25 ตัวแรก ทำให้ผลลัพธ์ไม่ออก และบังคับ length ตามที่เรากำหนด

select ascii('c') as result;
select ascii('css225 is easy') as res; -- return first char of string

select sign(10); -- positive return 1
select sign(-10); -- negative return -1
select sign(0); -- zero return 0

select pow(4, 2); -- 4^2
select sqrt(-1); -- return null
select exp(2); -- e^2

select round(10.5); -- >= .5 up / < .5 down


use sakila;

select * from address;
select coalesce(address2, 'none') as new_addr from address; -- change null value to 'none'
select address, coalesce(address2, 'none') as new_addr from address;

select * from rental;
select distinct(date_format(rental_date, '%a %D %b %Y')) as date_format from rental;

select current_date(), curdate(), current_time(), current_timestamp();
select dayofmonth(rental_date) as day, month(rental_date) as month, year(rental_date) as year from rental;

select datediff('2018-12-25', '2022-01-01'); -- datediff return number of day betweeen 2 values must be yyyy-mm-dd

select date_add('2020-01-01', interval 11 month);
select date_sub('2020-10-30', interval 10 day);

select * from rental where rental_date >= last_day(rental_date)-20; -- find last 20 day of month


select dayofmonth(current_timestamp());
select datediff('2018-12-25', curdate());

select 10 + '100'; -- result = 110
select cast(10 as char) + '110'; -- result = 120



-- sql create table
create table TICKET(
	TICKET_NO numeric(10) not null primary key,
    TICKET_PRICE numeric(4,2),
    TICKET_TYPE varchar(10) not null,
	PARK_CODE varchar(10),
    foreign key(PARK_CODE) references THEMEPARK(PARK_CODE)
);


create table ATTRACTION(
	ATTRACT_NO numeric(10) not null primary key,
    PARK_CODE varchar(10),
    ATTRACT_NAME varchar(35) not null,
    ATTRACT_AGE numeric(3) not null default 0,
    ATTRACT_CAPACITY numeric(3) not null,
    foreign key(PARK_CODE) references THEMEPARK(PARK_CODE)
);




