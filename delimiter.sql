use sakila;

DELIMITER //
CREATE PROCEDURE GetCustomers()
BEGIN
SELECT * FROM customer ORDER BY customer_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetAddress()
BEGIN
SELECT * FROM address ORDER BY address_id;
END //
DELIMITER ;

call GetCustomers();
call GetAddress();

drop procedure if exists GetCustomers; -- <- delete custom procedure
drop procedure if exists GetAddress;

-- in ส่งเข้าแล้วได้อย่างเดียว
-- out ส่งออกได้อย่างเดียว
-- inout รับเข้ามาคำนวนแล้วส่งออกไป


delimiter //
create procedure  GetActorByID(
	in actorID smallint
)
begin
	select first_name from actor where actor_id = actorID;
end //
delimiter ;

call GetActorbyID(1);

delimiter //
create procedure GetOrderCountByStatus(
	in orderStatus varchar(25),
    out total int
)
begin
	select count(orderNumber)
    into total
    from orders
    where status = orderStatus;
end //
delimiter ;


delimiter //
create procedure SetCounter(
	inout counter int,
    in inc int
)
begin
	set counter = counter + inc;
end //
delimiter ;


set @counter = 0;
call SetCounter(@counter, 3);
select @counter;



CALL GetOrderCountByStatus('Shipped', @total);


select * from film;

delimiter //
create procedure GetCountLanguageID(
	in languageID int,
    out total int
)
begin
	select count(film_id)
    into total
    from film
    where language_id = languageID;
end //
delimiter ;

set @total = 0;
call GetCountLanguageID(1, @total);
select @total;
