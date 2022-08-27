create schema Park;

use Park;

create table THEMEPARK (
	PARK_CODE varchar(10) not null primary key,
    PARK_NAME varchar(35) not null,
    PARK_CITY varchar(50) not null,
    PARK_COUNTRY char(2) not null
);

create table EMPLOYEE(
	EMP_NUM numeric(4) not null primary key,
    EMP_TITLE varchar(4),
    EMP_LNAME varchar(15) not null,
    EMP_FNAME varchar(15) not null,
    EMP_DOB date not null,
    EMP_HIRE_DATE date not null,
    EMP_AREACODE varchar(4) not null,
    EMP_PHONE varchar(12) not null,
    PARK_CODE varchar(10),
    foreign key(PARK_CODE) references THEMEPARK(PARK_CODE)
);

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

create table HOUR(
	EMP_NUM numeric(4) not null,
    ATTRACT_NO numeric(10) not null,
    HOURS_PER_ATTRACT numeric(2) not null,
    HOUR_RATE numeric(4,2) not null,
    DATE_WORKED date not null,
    primary key(EMP_NUM, ATTRACT_NO),
    foreign key(EMP_NUM) references EMPLOYEE(EMP_NUM),
    foreign key(ATTRACT_NO) references ATTRACTION(ATTRACT_NO)
);


create table SALES(
	TRANSACTION_NO numeric not null primary key,
    PARK_CODE varchar(10),
    SALE_DATE date not null,
    foreign key(PARK_CODE) references THEMEPARK(PARK_CODE)
);

create table SALESLINE(
	TRANSACTION_NO numeric not null primary key,
    LINE_NO numeric(2) not null,
    TICKET_NO numeric(10),
    LINE_QTY numeric(4),
    LINE_PRICE numeric(9,2),
    foreign key(TRANSACTION_NO) references SALES(TRANSACTION_NO),
    foreign key(TICKET_NO) references TICKET(TICKET_NO)
);






