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
SELECT JSON_CONTAINS('[1,2,3]', '1');
SELECT JSON_CONTAINS('["张三","张三2"]', '"张三"');


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
-- '$.*'	返回全部key的value
-- '$.name'	返回key="name"的数据
-- '$**.name'	返回所有最底层key="name"的数据
-- '$.auth[*].book[*]'	返回key=auth的list的key=book的list的所有内容

-- 二、创建JSON文本的函数
-- 2.1.JSON_ARRAY（转换json数组）
-- 2.2.JSON_OBJECT（转换json对象）
-- 2.3.JSON_QUOTE（转义字符串）
-- 三、搜索JSON文本的函数
-- 3.1.JSON_CONTAINS（json当中是否包含指定value）
-- 3.2.JSON_CONTAINS_PATH（是否包含某个PATH）
-- 3.3.JSON_EXTRACT 和 -> （根据key取值）
-- 3.4.JSON_UNQUOTE(JSON_EXTRACT()) 和 ->> （无引号提取）
-- 3.5.JSON_KEYS（获取json当中key数组）
-- 3.6.JSON_OVERLAPS（判断两个json是否存在同样的的key value）
-- 3.7.JSON_SEARCH（通过内容找path，支持模糊查）
-- 3.8.JSON_VALUE（根据key取值，如果没找到可以给默认值，如果找到了可以转换想要的数据类型）
-- 3.9.MEMBER OF（查看数组是否有某个元素）
-- 四、修改JSON文本的函数
-- 4.1.JSON_ARRAY_APPEND（在指定的数组位置末尾追加元素，假如指定的位置不是数组追加完过后就变成了数组）
-- 4.2.JSON_ARRAY_INSERT（在指定的数组位置后追加元素）
-- 4.3.JSON_INSERT（向指定path添加元素，path有值不覆盖，没值就添加）
-- 4.5.JSON_MERGE（多个json合并）
-- 4.6.JSON_MERGE_PATCH
-- 4.7.JSON_MERGE_PRESERVE
-- 4.8.JSON_REMOVE（根据path移除）
-- 4.9.JSON_REPLACE（替换指定path的值）
-- 5.0.JSON_SET（有则覆盖，没有则新增）
-- 五、返回JSON文本属性的函数
-- 5.1.JSON_DEPTH（返回 JSON 文档的最大深度）
-- 5.2.JSON_LENGTH（返回长度）
-- 5.3.JSON_TYPE（获取json的类型）
-- 5.4.JSON_VALID（判断是否是有效json）
-- 六、JSON工具函数
-- 6.1.JSON_PRETTY（json格式化输出）
-- 6.2.JSON_STORAGE_SIZE（计算占用的存储空间，单位字节）
-- 七、JSON聚合函数
-- 7.1.JSON_ARRAYAGG（配合GROUP BY进行分组，得到的是数组）
-- 7.2.JSON_OBJECTAGG（配合GROUP BY进行分组，得到的是对象）
