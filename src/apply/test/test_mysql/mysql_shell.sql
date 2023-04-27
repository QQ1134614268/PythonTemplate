# mysql
--
select * from INFORMATION_SCHEMA.TABLES;
select * from INFORMATION_SCHEMA.COLUMNS;
--
show columns from CBondDescription;
show full fields from CBondDescription;
desc CBondDescription;
show create table CBondDescription;

SHOW VARIABLES LIKE 'sql_mode';

--
alter table user engine=InnoDB; -- 命令来重建表。
OPTIMIZE table user;

-- mysql 数据问题定位
show full processlist;

SELECT * from information_schema.processlist;

select * from information_schema.innodb_trx;

select * from information_schema.innodb_locks;

select * from information_schema.innodb_lock_waits;

SHOW TABLE STATUS LIKE 'securities_score';

show open tables;

KILL 27;
