连表 分组 排序 limit
1. left join
2. from 中 子查询 驱动表
3. 都是子查询 left join 做二次筛选
4. 子查询 group_by ,order by , limit,  join a表


1. left join 原理:
   1. a_table join b_table 从 b_table 中取出 每一个 b_table.id = 2  ... 然后拼接上去?
    
2. 子查询

3. order by

4. group by

sql_no_cache


优化策略:
   1. from 小表驱动 
   2. 索引
   3. 子查询
   4. group by 后 join
   5. 连表分页, 先limit
