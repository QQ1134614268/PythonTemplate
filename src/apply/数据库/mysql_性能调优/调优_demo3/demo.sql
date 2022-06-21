desc CBondDescription;

select *  FROM  CCBondIssuance where CB_INFO_LISTDATE = 3 ;

show columns from CBondDescription;

show full fields from CBondDescription;

show create table CBondDescription;

show full fields from AShareCapitalization ;


alter table A engine=InnoDB; -- 命令来重建表。

OPTIMIZE

show full processlist;  

KILL	27;
