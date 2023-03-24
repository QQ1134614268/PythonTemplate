SELECT t1.fund_id,
       t1.cust_id,
       t1.cust_name,
       t1.biz_date,
       t2.debtsbal,
       t3.sum_fund_id_rz_balance
FROM (
         -- 客户信息
         SELECT sc.fund_id, sc.biz_date, sc.cust_id, sc.cust_name
         FROM sec_custinfo sc
         WHERE sc.biz_date = '2022-03-23'
           AND belong_org_id != 999
           and data_label = 0
     ) t1
         LEFT JOIN
     (
         -- 拿取授信额度
         SELECT scadr.fund_id,
                (IF(scadr.funddebtsbal > 0, scadr.funddebtsbal, scadr.stkdebtsbal)) AS debtsbal
         FROM sec_creditassetdebts_real scadr
         where updated_at > '2020-12-31'
     ) t2 ON t1.fund_id = t2.fund_id
         LEFT JOIN
     (
         -- 拿取融资余额
         SELECT scr.fund_id, SUM(scr.clear_amt - scr.creditrepay - scr.creditrepayunfrz) AS sum_fund_id_rz_balance
         FROM sec_contract_real scr
         where updated_at > '2020-12-31'
           and credit_direct = 0
           and data_label = 0
         GROUP BY scr.fund_id
     ) t3 ON t1.fund_id = t3.fund_id
ORDER BY sum_fund_id_rz_balance DESC
LIMIT 10

