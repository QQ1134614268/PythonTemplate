-- now函数 根据时区变化

set time_zone = '+8:00';
select now();
--
set time_zone = '+9:00';
select now();