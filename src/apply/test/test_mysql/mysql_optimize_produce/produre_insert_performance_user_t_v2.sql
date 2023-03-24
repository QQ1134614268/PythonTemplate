DELIMITER $$
DROP PROCEDURE IF EXISTS `insert_performance_user_t`$$

CREATE PROCEDURE `insert_performance_user_t`(in num int(10))
BEGIN
    DECLARE count INT DEFAULT 1;
    set @insert_sql =
            "INSERT INTO `performance_user_t`(id, name, sex, create_time, update_time, create_by, update_by) value ";
    set @exec_sql = "";
    set @exec_data = "";

    while count < num
        do
            set @id = "";
            set @row_data =
                    concat(@id, ",", @name, ",", @sex, ",", @create_time, ",", @update_time, ",", @create_by, ",",
                           @update_by);
            set @row_data_2 = concat("(", @row_data, ")");
            set count = count + 1;
            set i = i + 1;
            if i % 1000 = 0
            then
                set @exec_data = SUBSTRING(@exec_data, 2);
                set @exec_sql = concat("insert into csvimp(name,age,sex) values ", @exec_data);
                prepare stmt from @exec_sql;
                execute stmt;
                DEALLOCATE prepare stmt;
                set @exec_data = "";
            end if;
        end while;

    if length(@exec_data) > 0
    then
        set @exec_data = SUBSTRING(@exec_data, 2);
        set @exec_sql = concat("insert into csvimp(name,age,sex) values ", @exec_data);

        /*
        set @exec_sql = concat("select \"", @exesql, "\" from dual");
        */
        prepare stmt from @exec_sql;
        execute stmt;
        DEALLOCATE prepare stmt;
    end if;
END$$