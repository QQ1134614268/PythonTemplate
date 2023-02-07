EXPLAIN
SELECT t1.code,
       t1.cn_short_name,
       t2.stkqty as '客户持仓'
from (select stk_code, sum(stkqty) as stkqty from sec_stkasset_real group by stk_code) t2
         left join securities t1 on t1.code = t2.stk_code
         left join stock_fin_idx t4
                   on t4.biz_date = (SELECT max(biz_date) from stock_fin_idx WHERE stk_code = t1.code) and
                      t1.code = t4.stk_code;


EXPLAIN
SELECT t1.code,
       t1.cn_short_name,
       t2.stkqty as '客户持仓'
from (select stk_code, sum(stkqty) as stkqty from sec_stkasset_real group by stk_code) t2
         left join securities t1 on t1.code = t2.stk_code
         left join (SELECT ashare_gl_cptl,
                           stk_code,
                           ROW_NUMBER() over (PARTITION BY stk_code ORDER BY biz_date DESC) as row_num
                    from stock_fin_idx) t4 on row_num < 2 and t1.code = t4.stk_code;

EXPLAIN
SELECT t1.code,
       t1.cn_short_name,
       t2.stkqty as '客户持仓'
from (select stk_code, sum(stkqty) as stkqty from sec_stkasset_real group by stk_code) t2
         left join securities t1 on t1.code = t2.stk_code
         left join (SELECT stk_code, ashare_gl_cptl
                    FROM (SELECT ashare_gl_cptl,
                                 stk_code,
                                 ROW_NUMBER() over (PARTITION BY stk_code ORDER BY biz_date DESC) as row_num
                          from stock_fin_idx) t6
                    WHERE row_num < 2) t4 on t1.code = t4.stk_code;


EXPLAIN
SELECT ashare_gl_cptl
FROM (SELECT ashare_gl_cptl, ROW_NUMBER() over (PARTITION BY stk_code ORDER BY biz_date DESC) as row_num
      from stock_fin_idx) t6
WHERE row_num < 2;
