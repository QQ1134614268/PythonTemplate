select t1.fund_id,
       t1.cust_id,
       t1.cust_name,
       t1.biz_date,
       (IF(t2.funddebtsbal > 0, t2.funddebtsbal, t2.stkdebtsbal)) AS debtsbal,
       t3.sum_fund_id_rz_balance
from (
         SELECT fund_id, SUM(scr.clear_amt - scr.creditrepay - scr.creditrepayunfrz) AS sum_fund_id_rz_balance
         from sec_contract_real scr
         WHERE scr.updated_at > '2020-12-31'
           and scr.credit_direct = 0
           and scr.data_label = 0
         GROUP BY scr.fund_id
         ORDER BY sum_fund_id_rz_balance DESC
         LIMIT 10
     ) t3
         left join sec_custinfo t1 on t1.biz_date = '2022-03-23' and t1.fund_id = t3.fund_id  AND t1.belong_org_id != 999  and t1.data_label = 0
         left join sec_creditassetdebts_real t2 on t2.fund_id = t1.fund_id
