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

-- 慢日志
SHOW VARIABLES LIKE '%slow_query_log%'; # 是否开启记录 慢查询
SHOW VARIABLES LIKE '%slow_query_log_file%'; # 慢查询日志的 文件路径
SHOW VARIABLES LIKE '%long_queries_not_using_indexes%'; # 是否开启记录 没用索引的查询
SHOW VARIABLES LIKE '%long_query_time%';
SHOW VARIABLES LIKE '%log_output%';

set global slow_query_log = ON;
set global long_query_time = 10;
set global log_output = 'FILE,TABLE';

# 1. 查看文件
# 2. 查询表
select * from mysql.slow_log;

# mysqladmin -uroot -p flush-logs # 删除日志
--
select @@global.long_query_time, @@global.log_output,@@session.long_query_time, @@session.log_output;
set @@global.time_zone = '+10:00';
