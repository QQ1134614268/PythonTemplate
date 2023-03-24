#  DateTime 类型没有时区信息的, Timestamp 和时区有关
#  https://blog.csdn.net/weixin_33677704/article/details/113252849
CREATE TABLE IF NOT EXISTS `time_zone_test`
(
    `id`         int       NOT NULL AUTO_INCREMENT,
    `date_time`  datetime  NOT NULL,
    `time_stamp` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO time_zone_test(date_time, time_stamp)
VALUES (NOW(), NOW());

select date_time, time_stamp
from time_zone_test;

set time_zone = '+9:00'; # 修改时区,time_stamp 时间跟随变化

select date_time, time_stamp from time_zone_test;

select @@session.time_zone, @@global.time_zone;

SELECT date_add(NOW(), interval 1 day);


-- now函数 根据时区变化

set time_zone = '+8:00';
select now();
--
set time_zone = '+9:00';
select now();

-- 修改时区
select @@session.time_zone, @@global.time_zone;

set @@session.time_zone = '+9:00';
set @@global.time_zone = '+10:00';
select @@session.time_zone, @@global.time_zone;
