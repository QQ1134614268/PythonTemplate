ALTER TABLE `sec_creditassetdebts_real` ADD INDEX index_updated_at ( `updated_at` );
ALTER TABLE `sec_contract_real` ADD INDEX index_updated_at ( `updated_at` );
ALTER TABLE `sec_custinfo` ADD INDEX index_updated_at ( `fund_id` );