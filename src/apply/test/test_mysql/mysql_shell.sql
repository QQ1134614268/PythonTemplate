--
select * from INFORMATION_SCHEMA.TABLES;
select * from INFORMATION_SCHEMA.COLUMNS;
--
show columns from CBondDescription;
show full fields from CBondDescription;
desc CBondDescription;
show create table CBondDescription;

--
alter table user engine=InnoDB; -- 命令来重建表。
OPTIMIZE table user;

--
select * from information_schema.innodb_trx;

select * from information_schema.innodb_locks;

select * from information_schema.innodb_lock_waits;

SHOW VARIABLES LIKE 'sql_mode';

SHOW TABLE STATUS LIKE 'securities_score';

show open tables;

show full processlist;

KILL 27;
