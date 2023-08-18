DELIMITER $$
DROP PROCEDURE IF EXISTS `insert_performance_user_t`$$

CREATE PROCEDURE `insert_performance_user_t`(in num int(10))
BEGIN
    DECLARE name VARCHAR(60);
    DECLARE sex INT;

    DECLARE id INT;
    DECLARE create_time DATETIME;
    DECLARE update_time DATETIME;
    DECLARE create_by INT;
    DECLARE update_by INT;

    DECLARE now DATETIME;
    DECLARE i INT DEFAULT 1;

    set now = NOW();
    while i <= num
        do
            set id = i;
            SET name = CONCAT('name', i);
            SET sex = FLOOR(1 + RAND() * 2);

            SET create_time = date_sub(now, interval FLOOR(i / 10000) day);
            SET update_time = create_time;
            SET create_by = id;
            SET update_by = id;
            INSERT INTO `performance_user_t`(id, name, sex, create_time, update_time, create_by, update_by)
            VALUE (id, name, sex, create_time, update_time, create_by, update_by);
            SET i = i + 1;
        END WHILE;
END$$