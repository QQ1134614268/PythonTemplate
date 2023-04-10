# RECURSIVE cte

# demo1
WITH RECURSIVE cte AS (SELECT d.code, d.parent_code, d.name, d.code as id_code
                       FROM sys_area d
                       WHERE code in ('130132', '130225')
                       UNION ALL
                       SELECT c.code, c.parent_code, c.name, cte.id_code as id_code
                       FROM sys_area c
                                inner join cte on c.code = cte.parent_code)
SELECT code, GROUP_CONCAT(name ORDER BY id_code DESC SEPARATOR '/') as full_name
FROM cte
GROUP BY id_code;

# demo2
WITH RECURSIVE cte AS (SELECT d.id, d.parent_id
                       FROM organization d
                       WHERE id = 100
                       UNION ALL
                       SELECT c.id, c.parent_id
                       FROM organization c,
                            cte
                       WHERE c.parent_id = cte.id)
SELECT user.id
FROM cte
         LEFT JOIN user on cte.id = oa.user.org_id