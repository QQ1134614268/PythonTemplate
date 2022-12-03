-- jsonTest
-- 创建测试表
-- drop table if exists tab_json;
CREATE TABLE `tab_json` (
 `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键id',
 `data` json DEFAULT NULL COMMENT 'json字符串',
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 新增数据
-- INSERT INTO `test`.`tab_json`(`id`, `data`) VALUES (1, '{"id": "1", "name": "david", "jsonArr": [{"name": "jerry"}, {"name": "tom"}], "jsonObj": {"name": "jerry"}}');
-- INSERT INTO `test`.`tab_json`(`id`, `data`) VALUES (2, '[{"city": [{"name": "深圳"}, {"name": "珠海"}], "name": "广东"}, {"city": [{"name": "常州"}, {"name": "徐州"}], "name": "江苏"}]');

-- 查询 JSON_EXTRACT 对tab_json表使用json_extract函数 如果查询没有的key,返回的是NULL
select * from tab_json;

SELECT JSON_EXTRACT('{"a": 1, "b": 2, "c": [3, 4, 5]}', '$.c[*]') =JSON_ARRAY(3, 4, 5);

select JSON_EXTRACT(data,'$.name') from tab_json;

SELECT JSON_EXTRACT(data, '$[*].city[*].name') from tab_json;

select json_extract(json_extract(data,'$.data'),'$.name') from tab_json where json_extract(data,'$.name') = 'Mike';

SELECT JSON_CONTAINS(JSON_ARRAY('0','1'), '"0"')  ; -- 正确

-- JSON_EXTRACT
SELECT * from tab_json WHERE JSON_EXTRACT(data, '$.id') ='1' ; -- 正确

SELECT * from tab_json WHERE JSON_EXTRACT(data, '$.jsonObj.name') ='jerry';  -- 正确

SELECT * from tab_json WHERE JSON_EXTRACT(data, '$.jsonArr[*].name') =JSON_ARRAY('jerry', 'tom');

SELECT * from tab_json WHERE JSON_EXTRACT(data, '$[*].name')= JSON_ARRAY('广东', '江苏');

SELECT * from tab_json WHERE JSON_EXTRACT(data, '$.jsonArr') = JSON_ARRAY(JSON_OBJECT('name', 'jerry'), JSON_OBJECT('name', 'tom'));  -- 正确

SELECT JSON_EXTRACT(data, '$.jsonArr[*].name') from tab_json ; -- 正确

SELECT data->'$.jsonArr[*].name' from tab_json;  -- 正确

SELECT data->'$.jsonObj.name' from tab_json;  -- 正确

SELECT data->>'$.jsonObj.name' from tab_json;  -- 正确

SELECT * from tab_json WHERE data->>'$.jsonObj.name' = 'jerry';  -- 正确

SELECT * from tab_json WHERE data->>'$.jsonArr[*].name' ='tom';  -- 错误

-- 构造json
SELECT JSON_OBJECT('name', 'tom', 'age', 12);

SELECT JSON_ARRAY('tom', 'cat');

SELECT JSON_ARRAY(JSON_OBJECT('name', 'jerry'),  JSON_OBJECT('name', 'tom'));

SELECT JSON_ARRAY(1, 2), JSON_ARRAY(2, 1), JSON_ARRAY(1, 2)=JSON_ARRAY(1, 2),  JSON_ARRAY(1, 2)=JSON_ARRAY(2, 1); -- array 顺序参与比较


-- 条件查询 嵌套json查询

SELECT * from tab_json WHERE JSON_CONTAINS(data, '{"name":"江苏"}'); -- 正确

SELECT * from tab_json WHERE JSON_CONTAINS(data-> '$[*].city[*].name', '"徐州"');  -- 正确

SELECT * from tab_json WHERE JSON_CONTAINS(data-> '$.jsonArr[*].name', '"tom"'); -- 正确

SELECT * from tab_json WHERE JSON_CONTAINS(data-> '$.jsonArr[1].name', '"tom"'); -- 正确

SELECT * from tab_json WHERE JSON_CONTAINS(data -> '$.jsonArr','[{"name": "jerry"}, {"name": "tom"}]'); -- 正确

SELECT * from tab_json WHERE JSON_CONTAINS(data, '"jerry"', '$.jsonObj.name');

-- JSON_EXTRACT(json_doc, path[, path] ...)
-- JSON_CONTAINS(target, candidate[, path])
SELECT * from tab_json WHERE JSON_CONTAINS(data, '"徐州"', '$[*].city[*].name');  -- 错误

SELECT * from tab_json WHERE JSON_CONTAINS(data, '"徐州"', '$.*.city.*.name');  -- 错误

SELECT * from tab_json WHERE JSON_CONTAINS(data->'$.*.city.*.name', '"徐州"'); -- 错误

SELECT * from tab_json WHERE JSON_CONTAINS(data->'$.*.city[*].name', '"徐州"'); -- 错误

-- ‘$.*’	返回全部json
-- ‘$.title’	返回key=”title”的数据
-- ‘$**.text’	返回所有最底层key=”text”的数据
-- ‘$.content[*].item1[*]’	返回key=content的list的key=item1的list的所有内容