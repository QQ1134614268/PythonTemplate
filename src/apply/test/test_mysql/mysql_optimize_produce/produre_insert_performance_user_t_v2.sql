DELIMITER $$
DROP PROCEDURE IF EXISTS `insert_performance_user_t`$$

CREATE PROCEDURE `insert_performance_user_t`(in num int(10))
BEGIN
    set @count = 1;
    set @insert_sql = 'INSERT INTO `performance_user_t`(id, name, sex, create_time, update_time, create_by, update_by) values ';
    set @exec_data = '';
    set @exec_sql = '';

    while @count <= num
        do
            set @id = @count;
            set @name = CONCAT('name', @id);
            set @sex = FLOOR(1 + RAND() * 2);
            set @create_time = now();
            set @update_time = @create_time;
            set @create_by = @count;
            set @update_by = @count;

            set @row_data = concat(',', '(', @id, ',"', @name, '",', @sex, ',"', @create_time, '","', @update_time, '",', @create_by, ',', @update_by, ')');
            set @exec_data = concat(@exec_data, @row_data);
			set @count = @count + 1;
            if @count % 1000 = 0
            then
                set @exec_data = SUBSTRING(@exec_data, 2);
                set @exec_sql = concat(@insert_sql, @exec_data);
                prepare stmt from @exec_sql;
                execute stmt;
                DEALLOCATE prepare stmt;
                set @exec_data = '';
            end if;
        end while;

    if length(@exec_data) > 0
    then
        set @exec_data = SUBSTRING(@exec_data, 2);
        set @exec_sql = concat(@insert_sql, @exec_data);
        prepare stmt from @exec_sql;
        execute stmt;
        DEALLOCATE prepare stmt;
    end if;
END$$