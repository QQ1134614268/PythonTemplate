SELECT * FROM `performance_user_t` limit 100;

SELECT * FROM `performance_order_t` limit 100;

SELECT * FROM `performance_order_info_t` limit 100;

EXPLAIN SELECT order_id, SUM(num*price) FROM performance_order_info_t GROUP BY order_id ;
-- 1	SIMPLE	performance_order_info_t		ALL					1991187	100.00	Using temporary


EXPLAIN SELECT * from performance_user_t
LEFT JOIN performance_order_t on performance_order_t.user_id=performance_user_t.id
LEFT JOIN performance_order_info_t on performance_order_info_t.order_id=performance_order_t.id
LIMIT 100;

EXPLAIN SELECT * from performance_user_t
LEFT JOIN (SELECT id+1 as id , user_id  FROM (SELECT * FROM performance_order_t) t1) t1 on t1.user_id=performance_user_t.id
LEFT JOIN performance_order_info_t on performance_order_info_t.order_id=t1.id
LIMIT 100;

EXPLAIN SELECT * from performance_user_t
LEFT JOIN performance_order_t t1 on t1.user_id=performance_user_t.id
LEFT JOIN performance_order_info_t on performance_order_info_t.order_id=t1.id
LIMIT 100;

EXPLAIN SELECT * FROM (SELECT * from performance_user_t LIMIT 10)t1
LEFT JOIN performance_order_t on performance_order_t.user_id=t1.id
LEFT JOIN performance_order_info_t on performance_order_info_t.order_id=performance_order_t.id;


EXPLAIN SELECT * from performance_order_t WHERE user_id=1000;
-- 1	SIMPLE	performance_order_t		ALL					997194	10.00	Using where

EXPLAIN SELECT * from performance_order_t WHERE user_id=1000 or user_id=1001;
-- 1	SIMPLE	performance_order_t		ALL					997194	19.00	Using where

EXPLAIN SELECT * from performance_order_t WHERE id=1000; # or id=1001
-- 1	SIMPLE	performance_order_t		const	PRIMARY	PRIMARY	4	const	1	100.00

EXPLAIN SELECT COUNT(1) FROM performance_order_t;
-- 1	SIMPLE	performance_order_t		index		PRIMARY	4		997194	100.00	Using index


EXPLAIN SELECT id FROM (SELECT id from (SELECT id from performance_user_t LIMIT 10)t1 LIMIT 10)t1
-- 1	PRIMARY	<derived2>		ALL					10	100.00	
-- 2	DERIVED	<derived3>		ALL					10	100.00	
-- 3	DERIVED	performance_user_t		index		PRIMARY	4		9748178	100.00	Using index