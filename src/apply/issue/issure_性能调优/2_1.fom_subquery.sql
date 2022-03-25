SELECT t1.fund_id,
       t1.cust_id,
       t1.cust_name,
       t1.biz_date,
       (IF(t2.funddebtsbal > 0, t2.funddebtsbal, t2.stkdebtsbal))  AS debtsbal,
       SUM(scr.clear_amt - scr.creditrepay - scr.creditrepayunfrz) AS sum_fund_id_rz_balance
FROM (select t1.fund_id,
             t1.cust_id,
             t1.cust_name,
             t1.biz_date
      from sec_custinfo t1
      WHERE t1.biz_date = '2022-03-23'
        AND t1.belong_org_id != 999
        and t1.data_label = 0) t1
         left join sec_creditassetdebts_real t2 on t2.fund_id = t1.fund_id
         LEFT JOIN sec_contract_real scr
                   on scr.fund_id = t1.fund_id and scr.updated_at > '2020-12-31' and scr.credit_direct = 0 and
                      scr.data_label = 0
GROUP BY scr.fund_id
ORDER BY sum_fund_id_rz_balance DESC
LIMIT 10

