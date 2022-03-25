
select * from information_schema.innodb_trx;

select * from information_schema.innodb_locks;

select * from information_schema.innodb_lock_waits;

SHOW VARIABLES LIKE 'sql_mode'

SHOW TABLE STATUS LIKE 'securities_score';

show open tables;

alter table securities_score engine=InnoDB

DELETE from securities_score  WHERE date<'2021-05-10';


-- DELETE from securities_score  WHERE date<'2021-12-25';

-- DELETE from securities_score  WHERE date<'2021-11-20';






