-- jsonTest
-- 创建测试表
-- drop table if exists json_test;
CREATE TABLE `json_test` (
 `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键id',
 `obj` json DEFAULT NULL COMMENT '国家详情(json对象)',
 `arr` json DEFAULT NULL COMMENT '省列表(json数组)',
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 新增数据
INSERT INTO `json_test`(`obj`, `arr`) VALUES ('{"number":2,"name":"china"}',  '[{"city": [{"name": "深圳市"}, {"name": "珠海市"}], "name": "广东省"}, {"city": [{"name": "常州市"}, {"name": "徐州市"}], "name": "江苏省"}]' );

select * from json_test;

-- JSON_EXTRACT(json_doc, path[, path] ...) 如果查询没有的key,返回的是NULL
select JSON_EXTRACT(obj,'$.name') from json_test;
SELECT obj -> '$.name' from json_test;
SELECT obj ->> '$.name' from json_test;

SELECT JSON_EXTRACT(arr, '$[*].city[*].name') from json_test;
SELECT JSON_EXTRACT(arr, '$[*].name') from json_test;
SELECT arr -> '$[*].name' from json_test; # json数组类型
SELECT arr ->> '$[*].name' from json_test; # 字符串类型


SELECT obj -> '$.*' from json_test ;
SELECT obj -> '$.number' from json_test ;
SELECT JSON_EXTRACT(obj, '$.number','$.name') from json_test ;


-- 条件查询
SELECT * from json_test WHERE JSON_EXTRACT(obj, '$.name') ='china' ;
SELECT * from json_test WHERE JSON_EXTRACT(arr, '$[*].name')= JSON_ARRAY('广东省', '江苏省'); # 数组类型
SELECT * from json_test WHERE arr ->> '$[*].name'= '["广东省", "江苏省"]'; # 字符串类型
SELECT * from json_test WHERE obj -> '$.name' = '"china"';
SELECT * from json_test WHERE obj ->> '$.name' = 'china';

-- 条件查询 嵌套json查询 -- JSON_CONTAINS(target, candidate[, path])
SELECT * from json_test WHERE JSON_CONTAINS(obj -> '$.name', '"china"');
SELECT * from json_test WHERE JSON_CONTAINS(obj, '"china"','$.name');
SELECT * from json_test WHERE JSON_CONTAINS(obj, '{"name":"china"}');


SELECT * from json_test WHERE JSON_CONTAINS(arr ,'{"city": [{"name": "深圳市"}, {"name": "珠海市"}]}');
SELECT * from json_test WHERE JSON_CONTAINS(arr -> '$[0].name', '"广东省"');
SELECT * from json_test WHERE JSON_CONTAINS(arr -> '$[*].city[*].name', '"徐州市"');

-- UPDATE
UPDATE json_test SET obj = JSON_SET(obj,'$.name2','china2') ;
UPDATE json_test SET obj = JSON_REMOVE(obj, '$.name2');

-- 构造json
SELECT JSON_OBJECT('name', 'tom', 'age', 12);

SELECT JSON_ARRAY('1', '2');

SELECT JSON_ARRAY(JSON_OBJECT('name', 'jerry'),  JSON_OBJECT('name', 'tom'));

SELECT JSON_ARRAY(1, 2)=JSON_ARRAY(2, 1), JSON_ARRAY(1, 2)=JSON_ARRAY(1, 2); -- array 顺序参与比较

-- jsonpPath
SELECT JSON_EXTRACT('{"name": "book1", "auth": [{"name":"张三"},{"name":"李四"}], "info": {"money":100}}', '$.*');
SELECT JSON_EXTRACT('{"name": "book1", "auth": [{"name":"张三"},{"name":"李四"}], "info": {"money":100}}', '$.name');
SELECT JSON_EXTRACT('{"name": "book1", "auth": [{"name":"张三"},{"name":"李四"}], "info": {"money":100}}', '$**.name');
SELECT JSON_EXTRACT('{"name": "book1", "auth": [{"name":"张三","book": ["book1","mysql"]},{"name":"李四","book": ["book1","mysql"]}], "info": {"money":100}}', '$.auth[*]');
SELECT JSON_EXTRACT('{"name": "book1", "auth": [{"name":"张三","book": ["book1","mysql"]},{"name":"李四","book": ["book1","mysql"]}], "info": {"money":100}}', '$.auth[*].book'); # 嵌套数组
SELECT JSON_EXTRACT('{"name": "book1", "auth": [{"name":"张三","book": ["book1","mysql"]},{"name":"李四","book": ["book1","mysql"]}], "info": {"money":100}}', '$.auth[*].book[*]'); # 取出值

# book 是对象; '$.auth[*].book[*].size' # 异常
SELECT JSON_EXTRACT('{"auth":[{"book":{"size":[1,2,3]}}]}', '$.auth[*].book.size'), JSON_EXTRACT('{"auth":[{"book":{"size":[1,2,3]}}]}', '$.auth[*].book.size[*]') ;
-- ‘$.*’	返回全部key的value
-- ‘$.name’	返回key=”name”的数据
-- ‘$**.name’	返回所有最底层key=”name”的数据
-- ‘$.auth[*].book[*]’	返回key=auth的list的key=book的list的所有内容
