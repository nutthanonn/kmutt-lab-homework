use sakila;

select distinct rental_duration from film;

select max(length), min(length), avg(length) from film where length between 61 and 99;

select city from city where city like 'G%' or city like '%Z%';

select customer_id, sum(amount) from payment group by customer_id;

select * from film order by rental_rate desc;
