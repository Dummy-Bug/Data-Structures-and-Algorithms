
CrEaTe DaTAbaSE scaler_ClAsS; 
create database scaler_class;

-- MySQL is case insensitive
-- every line of sql should end with semicolon

create database if not exists scaler_class;

drop database scaler_class;

drop database if exists scaler_class;

create database scaler_class;

use scaler_class;

-- {Name Of Column} {Data Type of Column} {Parameters}

create table if not exists batches (
	id int primary key auto_increment,
    name varchar(20) not null,
    strength int
);

create table if not exists students (
 id int primary key auto_increment,
 name varchar(20) not null,
 email varchar(20) not null,
 batch_id int,
 foreign key (batch_id)
 references batches(id)
 on update restrict
 on delete cascade
);


-- Ensure MySQL8 and MySQL workbench is installed
-- https://dev.mysql.com/doc/refman/8.0/en/database-use.html
-- https://dev.mysql.com/doc/refman/8.0/en/creating-database.html
-- https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html
-- https://stackoverflow.com/a/6720458 
-- https://www.youtube.com/watch?v=uikbtpVZS2s&list=PLSE8ODhjZXjaKScG3l0nuOiDTTqpfnWFf&index=1
