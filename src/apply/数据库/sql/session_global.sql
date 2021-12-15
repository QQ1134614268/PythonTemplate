select @@session.time_zone,@@global.time_zone;
set @@session.time_zone='+9:00';
set @@global.time_zone='+10:00';
select @@session.time_zone,@@global.time_zone;