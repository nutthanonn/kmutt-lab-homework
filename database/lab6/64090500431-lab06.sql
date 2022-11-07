use sakila;

-- 1
select '7' as rental_duration from film;

-- 2
select ucase(trim(lpad(title, 3, ' '))) from film;

-- 3
select floor(datediff(curdate(), '2003-04-28')/365) as my_age;

-- 4
select date_format(curdate(), '%y%j') as julian_date;

-- 5
select curdate() as today;
select date_format(curdate(), '%D %M %Y') as today;
select date_format(curdate(), '%d/%m/%Y') as today;
select date_format(current_timestamp(), '%a %d %b %H:%i') as today;
select date_format(current_timestamp(), '%H:%i %a %d %b %Y') as today;