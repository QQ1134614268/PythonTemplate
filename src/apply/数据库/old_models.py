# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DECIMAL, Date, DateTime, Float, ForeignKey, Index, Integer, JSON, String, TIMESTAMP, Table, text
from sqlalchemy.dialects.mysql import BIGINT, BIT, CHAR, INTEGER, TEXT, TIMESTAMP, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AshareEspecialStk(Base):
    __tablename__ = 'ashare_especial_stk'
    __table_args__ = {'comment': '中国A股特别处理表'}

    stk_code = Column(VARCHAR(10), comment='证券代码')
    sec_unique_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券唯一码')
    trd_mkt_code = Column(VARCHAR(10), comment='交易市场代码')
    wind_code = Column(VARCHAR(10), comment='Wind代码')
    especial_deal_type = Column(VARCHAR(10), primary_key=True, nullable=False, comment='特别处理类型(S:特别处理(ST) Z:暂停上市 P:特 转让服务(PT) L:退市整理 X:创业板暂停上市风险警示 T:退市)')
    in_date = Column(DECIMAL(8, 0), comment='纳入日期')
    out_date = Column(DECIMAL(8, 0), comment='剔除日期')
    announce_date = Column(DECIMAL(8, 0), primary_key=True, nullable=False, comment='公布日期')
    especial_deal_reason = Column(VARCHAR(200), comment='特别处理原因')
    data_time = Column(DateTime, comment='数据时间')
    biz_date = Column(Integer, comment='业务日期')


class AshareOldname(Base):
    __tablename__ = 'ashare_oldname'
    __table_args__ = {'comment': '中国a股证券曾用名表'}

    stk_code = Column(VARCHAR(12), comment='证券代码')
    trd_mkt_code = Column(VARCHAR(12), comment='交易市场代码')
    sec_unique_code = Column(VARCHAR(12), comment='证券唯一码')
    wind_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='wind代码')
    start_date = Column(Integer, primary_key=True, nullable=False, comment='起始日期')
    ddln_date = Column(Integer, comment='截止日期')
    notice_date = Column(Integer, comment='公告日期')
    sec_abbr = Column(VARCHAR(50), comment='证券简称')
    chan_reason_code = Column(VARCHAR(12), comment='变化原因代码')
    chan_reason_name = Column(VARCHAR(200), comment='变化原因名称')
    opr_date = Column(DateTime, comment='操作日期')
    opr_type = Column(VARCHAR(12), comment='操作类型')
    data_time = Column(DateTime, comment='数据时间')
    biz_date = Column(Integer, comment='业务日期')


class AsynExport(Base):
    __tablename__ = 'asyn_export'
    __table_args__ = {'comment': '异步导出信息表'}

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    type = Column(VARCHAR(10), nullable=False, server_default=text("''"), comment='类型')
    filename = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='文件名称')
    status = Column(VARCHAR(10), nullable=False, server_default=text("''"), comment='生成状态')
    create_by = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='创建人ID')
    create_by_name = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='创建人名字')
    gmt_create = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')


class AuthBranchCd(Base):
    __tablename__ = 'auth_branch_cd'
    __table_args__ = {'comment': '营业部代码'}

    server_id = Column(VARCHAR(4), comment='节点')
    branch_cd = Column(VARCHAR(20), primary_key=True, comment='营业部代码')
    branch_name = Column(VARCHAR(40), comment='营业部名称')
    branch_grade = Column(VARCHAR(20), comment='营业部等级')
    commission_no = Column(VARCHAR(20), comment='证监会机构编码')
    center_branch_cd = Column(VARCHAR(20), comment='中心营业部代码')
    center_branch_name = Column(VARCHAR(40), comment='中心营业部名称')
    belong_area = Column(VARCHAR(20), comment='归属地区')
    branch_office = Column(VARCHAR(20), comment='归属分公司代码')
    branch_office_name = Column(VARCHAR(20), comment='归属分公司名称')
    sub_branch_office = Column(VARCHAR(20), comment='下辖分公司代码')
    sub_branch_office_name = Column(VARCHAR(40), comment='下辖分公司名称')
    belong_west_flag = Column(VARCHAR(4), comment='归属西部标志')
    city = Column(VARCHAR(40), comment='所在城市')
    valid_flag = Column(VARCHAR(2), comment='有效标志')
    data_label = Column(VARCHAR(4), comment='数据标签，区分来自宏源(hy)还是申万(sw)的数据')
    branch_office_level = Column(VARCHAR(20), comment='所属分公司级别')
    brch_type_cd = Column(VARCHAR(4), comment='营业部类型代码')
    sys_branch_code = Column(VARCHAR(20), comment='源系统机构代码')
    remark = Column(VARCHAR(128), comment='备注')


class BaseConversionRateConfig(Base):
    __tablename__ = 'base_conversion_rate_config'
    __table_args__ = {'comment': '基准表'}

    id = Column(Integer, primary_key=True, comment='ID')
    stk_category = Column(VARCHAR(10), comment='证券分类')
    market = Column(VARCHAR(10), comment='市场')
    stk_type = Column(VARCHAR(10), comment='证券品种')
    range_in = Column(VARCHAR(30), comment='调入范围')
    change_reason = Column(VARCHAR(20), comment='调整原因')
    period_adj = Column(VARCHAR(10), comment='定调折算率')
    margin_finance_rate = Column(VARCHAR(10), comment='融资保证金比例')
    margin_securities_rate = Column(VARCHAR(10), comment='融券保证金比例')


class Company(Base):
    __tablename__ = 'company'
    __table_args__ = {'comment': '公司信息表'}

    comp_code = Column(VARCHAR(10), primary_key=True, comment='公司代码')
    stk_short_name = Column(VARCHAR(100), comment='公司简称')
    eng_short_name = Column(VARCHAR(100), comment='公司简称(英文)')
    base_info = Column(TEXT, comment='公司基本信息')
    full_name = Column(VARCHAR(200), comment='公司全称')
    eng_full_name = Column(VARCHAR(128), comment='公司全称(英文)')
    indu_name = Column(VARCHAR(100), comment='行业名称(申万二级)')
    datatime = Column(DateTime, comment='数据时间')
    biz_date = Column(Date, comment='业务日期')


t_company_category = Table(
    'company_category', metadata,
    Column('stk_code', CHAR(6)),
    Column('wind_code', VARCHAR(10)),
    Column('sec_abbr', VARCHAR(24)),
    Column('co_chn_name', VARCHAR(100)),
    Column('list_plate', Integer),
    Column('list_plate_desc', VARCHAR(20)),
    Column('sw_fst_code', Integer),
    Column('industry_name', VARCHAR(20)),
    Column('datatime', DateTime),
    Column('biz_date', Integer),
    comment='公司分类表'
)


class ConstituentStocksList(Base):
    __tablename__ = 'constituent_stocks_list'
    __table_args__ = {'comment': '成分股列表'}

    biz_date = Column(Date, primary_key=True, nullable=False)
    stk_code = Column(VARCHAR(20), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    is_sh180 = Column(CHAR(1), comment='上证180')
    is_sz100 = Column(CHAR(1), comment='深证100')
    is_sh50 = Column(CHAR(1), comment='上证50')
    is_hs300 = Column(CHAR(1), comment='沪深300')
    is_zz1000 = Column(CHAR(1), comment='中证1000')


class CpGuaranteeList(Base):
    __tablename__ = 'cp_guarantee_list'
    __table_args__ = {'comment': '券商担保券清单'}

    stk_code = Column(VARCHAR(20), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    rate = Column(DECIMAL(26, 4), comment='折算率')
    market = Column(VARCHAR(10), comment='上交所  深交所')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')


class CustRiskGrade(Base):
    __tablename__ = 'cust_risk_grade'
    __table_args__ = {'comment': '客户风险等级分类设置结果表'}

    fund_id = Column(VARCHAR(200), primary_key=True, nullable=False, comment='资金账户（信用）')
    final_score = Column(DECIMAL(10, 0), comment='风险等级设置最后总得分')
    detail_score = Column(JSON, comment='客户风险等级6个指标的得分')
    grade = Column(Integer, comment='客户风险等级，0:安全,1:关注,2:低风险,3:中风险,4:高风险')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='计算日期')
    ranks = Column(BigInteger, comment='得分排名')
    rank_percent = Column(DECIMAL(10, 4), comment='得分排名比')
    guarantee_rank_percent = Column(DECIMAL(10, 4), comment='担保物质量排名比')
    gmt_create = Column(Date, comment='创建日期')
    gmt_modified = Column(Date, comment='修改日期')


class CustRiskKeeprateReal(Base):
    __tablename__ = 'cust_risk_keeprate_real'
    __table_args__ = {'comment': '客户风险维保信息表'}

    fund_id = Column(VARCHAR(200), primary_key=True, comment='资金账户（信用）')
    risk_keeprate = Column(DECIMAL(10, 4), comment='风险维保比例得分')
    ranks = Column(Integer, comment='得分排名')
    rank_less_percent = Column(DECIMAL(10, 2), comment='得分低于多少客户百分比(排名-1/客户数)')
    update_at = Column(DateTime, comment='更新时间')


class CustRiskgradeAvgScore(Base):
    __tablename__ = 'cust_riskgrade_avg_score'
    __table_args__ = {'comment': '客户风险等级分类设置结果表-6维分'}

    biz_date = Column(Date, primary_key=True, comment='更新日期')
    collateral_quality = Column(DECIMAL(7, 4), comment='担保物质量平均分\\r\\n')
    debt_assets = Column(DECIMAL(7, 4), comment='资产负债平均分')
    risk_rank = Column(DECIMAL(7, 4), comment='资信等级平均分')
    investment_ability = Column(DECIMAL(7, 4), comment='投资能力平均分')
    risk_control = Column(DECIMAL(7, 4), comment='风控能力平均分')
    customer_value = Column(DECIMAL(7, 4), comment='客户价值平均分')
    gmt_create = Column(Date, comment='创建时间')
    gmt_modified = Column(Date, comment='修改时间')


class DataDictionary(Base):
    __tablename__ = 'data_dictionary'
    __table_args__ = (
        Index('data_dictionary_type_IDX', 'type', 'name'),
        Index('idx_col1_col2', 'type', 'en_name', unique=True),
        {'comment': '数据字典'}
    )

    category = Column(VARCHAR(100), comment='类别')
    id = Column(Integer, primary_key=True, comment='ID')
    type = Column(VARCHAR(32), nullable=False, comment='字段类型')
    name = Column(VARCHAR(64), nullable=False, comment='字段中文名称')
    en_name = Column(VARCHAR(32), nullable=False, comment='字段英文名称')
    info = Column(VARCHAR(255), comment='字段说明')
    unit = Column(VARCHAR(32), comment='单位')
    updated_at = Column(DateTime, nullable=False, comment='更新时间')
    created_at = Column(DateTime, nullable=False, comment='创建时间')


class DataMissAny(Base):
    __tablename__ = 'data_miss_any'
    __table_args__ = {'comment': '数据缺失分析'}

    db_table_col = Column(VARCHAR(100), primary_key=True, nullable=False, comment='数据库名.表名.字段名(英文)')
    db_name = Column(VARCHAR(50), comment='数据库名')
    table_name = Column(VARCHAR(50), comment='表名')
    column_name = Column(VARCHAR(50), comment='列名(指标名称)')
    total = Column(Integer, comment='数值计数(总)')
    null_val = Column(Integer, comment='缺失值计数')
    miss_rate = Column(DECIMAL(26, 4), comment='缺失率')
    median = Column(DECIMAL(26, 4), comment='中值')
    max_val = Column(DECIMAL(26, 4), comment='最大值')
    min_val = Column(DECIMAL(26, 4), comment='最小值')
    avg_val = Column(DECIMAL(26, 4), comment='平均值')
    created_at = Column(Date, primary_key=True, nullable=False, comment='分析时间')


class Department(Base):
    __tablename__ = 'department'
    __table_args__ = {'comment': '部门信息'}

    id = Column(Integer, primary_key=True, comment='ID')
    name = Column(VARCHAR(64), nullable=False, comment='部门名称')
    created_at = Column(DateTime, nullable=False, comment='创建时间')


class DictConv(Base):
    __tablename__ = 'dict_conv'
    __table_args__ = {'comment': '字典转换表'}

    source_sys = Column(VARCHAR(10), primary_key=True, nullable=False, comment='源系统，用服务域标识，如WIND,TX,JC,UPCHINA')
    source_item = Column(VARCHAR(50), primary_key=True, nullable=False, comment='源系统字典项')
    dest_item = Column(VARCHAR(50), nullable=False, comment='目标系统字典项')
    dest_sys = Column(VARCHAR(50), primary_key=True, nullable=False, comment='目标系统')
    dest_text = Column(VARCHAR(50), comment='字典项名称')
    flag = Column(CHAR(1), comment='字典项类型，用于一对多字典时区分主用字典，0-非主用字典，1-主用字典')
    remark = Column(VARCHAR(50), comment='备注')


class EsContractMonitorFin(Base):
    __tablename__ = 'es_contract_monitor_fin'
    __table_args__ = {'comment': 'ES 融资合约监控统计表'}

    sno = Column(VARCHAR(50), primary_key=True, nullable=False, comment='合约编号')
    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    open_date = Column(Date, primary_key=True, nullable=False, comment='合约开仓日期')
    close_date = Column(Date, comment='合约到期日期')
    countdown_day = Column(Integer, comment='剩余到期时间')
    creditrepay = Column(DECIMAL(26, 4), comment='t日之前归还金额(融资总负债/融券总负债)')
    unpay_fin_pri = Column(DECIMAL(26, 4))
    unpay_oth_fee_tot = Column(DECIMAL(26, 4))
    unpay_interest = Column(DECIMAL(26, 4))
    stk_code = Column(CHAR(8), comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券简称')
    board = Column(VARCHAR(32), comment='板块')
    match_qty = Column(BigInteger, comment='成交数量')
    match_amt = Column(DECIMAL(26, 4), comment='成交金额')
    ext_num = Column(Integer, comment='已展期次数')
    stk_status = Column(VARCHAR(10), comment='停牌或正常')
    noext_flag = Column(CHAR(1), comment='禁止外围展期标志（数据字典待提供）')
    halfyear_close_pos_num = Column(Integer, comment='180日内平仓次数（资金账户级别）')
    cust_name = Column(VARCHAR(32), comment='客户名称')
    keeprate = Column(DECIMAL(26, 4), comment='维持担保比例')
    pni_fee_tot = Column(DECIMAL(26, 4), comment='当日应还本息合计')
    avl_amt = Column(DECIMAL(26, 4), comment='可用资金')
    is_covered_pni_fee = Column(CHAR(1), comment='流动资金是否覆盖当日负债，1覆盖，0未覆盖')
    can_ext = Column(CHAR(1), comment='是否符合展期条件')
    updated_at = Column(DateTime, comment='合约更新时间')
    update_time = Column(DateTime, comment='更新时间')
    biz_date = Column(Date, comment='数据日期')
    regis_ratio = Column(DECIMAL(26, 4), comment='注册制持仓集中度')
    regis_no_limit_ratio = Column(DECIMAL(26, 4), comment='无涨跌幅限制注册制持仓集中度')
    liquid_assets = Column(DECIMAL(26, 4), comment='流动资产')


class EsContractMonitorSec(Base):
    __tablename__ = 'es_contract_monitor_sec'
    __table_args__ = {'comment': 'ES 融券合约监控统计表'}

    sno = Column(VARCHAR(50), primary_key=True, nullable=False, comment='合约编号')
    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    open_date = Column(Date, primary_key=True, nullable=False, comment='合约开仓日期')
    close_date = Column(Date, comment='合约到期日期')
    countdown_day = Column(Integer, comment='剩余到期时间')
    creditrepay = Column(DECIMAL(26, 4), comment='t日之前归还金额(融资总负债/融券总负债)')
    unpay_fin_pri = Column(DECIMAL(26, 4))
    unpay_oth_fee_tot = Column(DECIMAL(26, 4))
    unpay_interest = Column(DECIMAL(26, 4))
    stk_code = Column(CHAR(8), comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券简称')
    board = Column(VARCHAR(32), comment='板块')
    match_qty = Column(BigInteger, comment='成交数量')
    match_amt = Column(DECIMAL(26, 4), comment='成交金额')
    ext_num = Column(Integer, comment='已展期次数')
    stk_status = Column(VARCHAR(10), comment='停牌或正常')
    noext_flag = Column(CHAR(1), comment='禁止外围展期标志（数据字典待提供）')
    halfyear_close_pos_num = Column(Integer, comment='180日内平仓次数（资金账户级别）')
    cust_name = Column(VARCHAR(32), comment='客户名称')
    keeprate = Column(DECIMAL(26, 4))
    pni_fee_tot = Column(DECIMAL(26, 4))
    avl_amt = Column(DECIMAL(26, 4))
    is_covered_pni_fee = Column(CHAR(1))
    can_ext = Column(CHAR(1))
    updated_at = Column(DateTime)
    update_time = Column(DateTime)
    unpay_sec_val = Column(DECIMAL(26, 4), comment='未还证券金额')
    unpay_sec_num = Column(DECIMAL(26, 4), comment='未还证券数量')
    biz_date = Column(Date, comment='数据日期')
    regis_ratio = Column(DECIMAL(26, 4), comment='注册制持仓集中度')
    regis_no_limit_ratio = Column(DECIMAL(26, 4), comment='无涨跌幅限制注册制持仓集中度')
    stkqty = Column(Integer, comment='该证券合计持仓数量')
    unpay_sec_num_tot = Column(DECIMAL(26, 4), comment='该证券合计未还数量')
    is_limit_ext = Column(String(2, 'utf8mb4_general_ci'), comment='是否限制融券展期，是和否')


class EsCustinfo(Base):
    __tablename__ = 'es_custinfo'
    __table_args__ = {'comment': 'ES 客户画像统计表'}

    belong_org_id = Column(CHAR(4), comment='营业部代码')
    fund_id = Column(VARCHAR(100), primary_key=True, comment='资金账号（信用）')
    cust_id = Column(VARCHAR(19), comment='客户id')
    cust_name = Column(VARCHAR(32), comment='客户名称')
    biz_date = Column(Date, comment='业务日期')
    credit_level = Column(VARCHAR(16), comment='当前资信等级')
    tot_asset = Column(DECIMAL(26, 4), comment='总资产')
    tot_debts = Column(DECIMAL(26, 4), comment='总负债')
    keeprate = Column(DECIMAL(26, 4), comment='维持担保比例')
    asset_desc = Column(VARCHAR(500))
    cash = Column(DECIMAL(26, 4))
    max_share_desc = Column(VARCHAR(100))
    update_time = Column(DateTime)
    resist_stop_times = Column(DECIMAL(26, 4), comment='抗跌停次数，-1表示有问题')


class EsDebtCustomerInfo(Base):
    __tablename__ = 'es_debt_customer_info'
    __table_args__ = {'comment': 'es负债客户信息'}

    fund_id = Column(VARCHAR(100), primary_key=True, comment='资金账号（信用）')
    belong_org_id = Column(CHAR(4), comment='营业部代码')
    cust_name = Column(VARCHAR(32), comment='客户名称')
    noext_flag = Column(VARCHAR(200), comment='禁止外围展期标记')
    biz_date = Column(Date, comment='业务日期')
    keeprate_lastweek = Column(DECIMAL(26, 4), comment='上周维持担保比例')
    keeprate_real = Column(DECIMAL(26, 4), comment='本周维持担保比例')
    stk_code = Column(CHAR(8), comment='持仓证券代码')
    mktval = Column(DECIMAL(26, 4), comment='持仓证券市值')
    total_asset = Column(DECIMAL(26, 4), comment='信用总资产')
    total_debts = Column(DECIMAL(26, 4), comment='信用总负债')
    credit_line = Column(DECIMAL(26, 4), comment='授信额度（万元）')
    stk_name = Column(VARCHAR(200), comment='证券名称')
    pos_concentration = Column(DECIMAL(26, 4), comment='持仓集中度')
    updated_at = Column(TIMESTAMP, comment='实时更新时间')
    update_time = Column(TIMESTAMP, comment='更新时间')
    awkward_secu_risk = Column(VARCHAR(30))
    account_pos = Column(VARCHAR(30))
    pos_control = Column(VARCHAR(30))


class EsHoldCustomer(Base):
    __tablename__ = 'es_hold_customer'
    __table_args__ = {'comment': 'es注册制持仓客户'}

    fund_id = Column(VARCHAR(100), primary_key=True, comment='资金账号（信用）')
    belong_org_id = Column(CHAR(4), comment='营业部代码')
    biz_date = Column(Date, comment='业务日期')
    cust_name = Column(VARCHAR(32), comment='客户名称')
    cust_code_arr_cd = Column(Integer, comment='客户类别标签（个人/机构）')
    tot_asset = Column(DECIMAL(26, 4), comment='总资产')
    fin_debt_tot_amt = Column(DECIMAL(26, 4), comment='融资总负债')
    secu_debt_tot_amt = Column(DECIMAL(26, 4), comment='融券总负债')
    tot_debts = Column(DECIMAL(26, 4), comment='总负债')
    keeprate = Column(DECIMAL(26, 4), comment='维持担保比例')
    net_asset = Column(DECIMAL(26, 4), comment='净资产')
    tot_mrkt_val = Column(DECIMAL(26, 4), comment='折人民币总市值')
    max_stk_desc = Column(VARCHAR(170), comment='证券代码-证券简称-折人民币市值')
    update_time = Column(TIMESTAMP, comment='更新时间')
    tot_mrkt_val_asset_ratio = Column(DECIMAL(26, 4), comment='折人民币市值/总资产')


class EsNetShortCustomer(Base):
    __tablename__ = 'es_net_short_customer'
    __table_args__ = {'comment': 'ES 净空头客户'}

    fund_id = Column(VARCHAR(100), primary_key=True, comment='资金账号')
    belong_org_id = Column(CHAR(4), comment='营业部代码')
    biz_date = Column(Date, comment='业务日期')
    cust_net_short_value = Column(DECIMAL(26, 4))
    max_net_short_value = Column(DECIMAL(26, 4))
    cust_name = Column(VARCHAR(32), comment='客户名称')
    cust_code_arr_cd = Column(Integer, comment='客户类别标签（个人/机构）')
    tot_asset = Column(DECIMAL(26, 4), comment='总资产')
    fin_debt_tot_amt = Column(DECIMAL(26, 4), comment='融资总负债')
    secu_debt_tot_amt = Column(DECIMAL(26, 4), comment='融券总负债')
    tot_debts = Column(DECIMAL(26, 4), comment='总负债')
    keeprate = Column(DECIMAL(26, 4), comment='维持担保比例')
    net_asset = Column(DECIMAL(26, 4), comment='净资产')
    net_short_val_net_asset_prop = Column(DECIMAL(26, 4))
    max_short_val_net_asset_prop = Column(DECIMAL(26, 4))
    stk_code = Column(VARCHAR(19), comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券简称')
    industry_sw_2 = Column(VARCHAR(64))
    max_value = Column(DECIMAL(26, 4))
    max_value_net_ass_prop = Column(DECIMAL(26, 4))
    sum_value = Column(DECIMAL(26, 4))
    sum_value_tot_ass_prop = Column(DECIMAL(26, 4))
    update_time = Column(DateTime)


class EsNetShortIndustry(Base):
    __tablename__ = 'es_net_short_industry'
    __table_args__ = {'comment': 'ES 净空头行业'}

    industry_sw_2 = Column(VARCHAR(64), primary_key=True)
    biz_date = Column(Date, comment='业务日期')
    sum_value = Column(DECIMAL(26, 4))
    update_time = Column(DateTime)
    indu_type = Column(Integer, comment='类别，0：普通行业，1：ETF基金')


class EsNetShortStock(Base):
    __tablename__ = 'es_net_short_stock'
    __table_args__ = {'comment': 'ES 净空头证券'}

    stk_code = Column(VARCHAR(19), primary_key=True, comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券简称')
    board = Column(VARCHAR(32), comment='板块')
    industry_sw_1 = Column(VARCHAR(64), comment='申万一级行业')
    industry_sw_2 = Column(VARCHAR(64))
    biz_date = Column(Date, comment='业务日期')
    stk_net_short_value = Column(DECIMAL(26, 4))
    stk_net_short_qty = Column(DECIMAL(26, 4))
    total_share = Column(DECIMAL(26, 4), comment='证券总股本')
    net_short_qty_tot_shr_prop = Column(DECIMAL(26, 4))
    tra_shares = Column(DECIMAL(26, 4), comment='流通股')
    net_short_qty_tra_shr_prop = Column(DECIMAL(26, 4))
    match_amt_avg = Column(DECIMAL(19, 2), comment='最近30天平均成交额（日终算一次）')
    liduid_days = Column(DECIMAL(19, 2), comment='最近30天平均成交额（日终算一次）')
    update_time = Column(DateTime)


class EsStockList(Base):
    __tablename__ = 'es_stock_list'
    __table_args__ = {'comment': 'es证券列表'}

    biz_date = Column(Date, comment='业务日期')
    stk_code = Column(CHAR(8), primary_key=True, comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券简称')
    indu_code = Column(VARCHAR(32), comment='申万一级行业代码')
    indu_name = Column(VARCHAR(64), comment='申万一级行业')
    board_name = Column(VARCHAR(32), comment='板块名称')
    price = Column(DECIMAL(9, 4), comment='价格')
    total_sec_shares = Column(DECIMAL(26, 4), comment='信用账户持股合计')
    total_shares = Column(DECIMAL(26, 4), comment='总股本')
    sec_shares_ratio = Column(DECIMAL(26, 6), comment='占总股本比例')
    tra_shares = Column(DECIMAL(26, 4), comment='流通股本')
    tra_shares_ratio = Column(DECIMAL(26, 6), comment='占总股本比例')
    match_qty_avg = Column(BigInteger, comment='日均成交量(近一个月)')
    force_trade_out_days = Column(Float, comment='理论平仓天数')
    sec_shares_mkt_val = Column(DECIMAL(26, 4), comment='信用账户持仓市值')
    sec_shares_mkt_val_change = Column(DECIMAL(9, 4), comment='信用账户持仓市值较上日增减')
    total_mkt_val = Column(DECIMAL(26, 4), comment='证券总市值')
    sec_shares_mkt_val_ratio = Column(DECIMAL(9, 4), comment='占信用账户总市值比例')
    is_collateral = Column(CHAR(1), comment='是否为担保物')
    value_rate = Column(DECIMAL(9, 4), comment='折算率')
    risk_score = Column(DECIMAL(9, 4), comment='风险评分')
    board_code = Column(VARCHAR(32), comment='板块代码')
    secu_cate_code = Column(CHAR(1), comment='证券类别（S：股票，F：基金，B：债券）')
    update_time = Column(TIMESTAMP, comment='更新时间')


class ExpertIndice(Base):
    __tablename__ = 'expert_indices'
    __table_args__ = {'comment': '风险分析总表（当天）'}

    id = Column(Integer, primary_key=True, comment='ID')
    comp_code = Column(VARCHAR(12), nullable=False, comment='证券代码')
    data_model = Column(JSON, nullable=False, comment='财务指标')
    risk_analysis = Column(JSON, nullable=False, comment='风险评分')
    notices = Column(JSON, nullable=False, comment='风险提示')
    notices_level = Column(JSON, nullable=False, comment='风险等级')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')


class GuaranteeBond(Base):
    __tablename__ = 'guarantee_bonds'
    __table_args__ = {'comment': '担保券清单'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='交易日期')
    conversion_rate = Column(VARCHAR(10), comment='折算率')
    standard_basis = Column(VARCHAR(20), comment='标准依据')
    trading_market = Column(VARCHAR(20), comment='交易市场')
    stk_type = Column(String(20, 'utf8mb4_general_ci'), comment='证券品种')
    regist = Column(VARCHAR(2), comment='是否注册制上市')
    sec_code = Column(VARCHAR(30), comment='带后缀的code')


class HoldersPledge(Base):
    __tablename__ = 'holders_pledge'
    __table_args__ = {'comment': '中国A股重要股东（5%以上）质押表'}

    stk_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    report_time = Column(Date, primary_key=True, nullable=False, comment='报告日期')
    shareholder_name = Column(VARCHAR(128), primary_key=True, nullable=False, server_default=text("''"), comment='股东名称')
    pledgee_name = Column(VARCHAR(128), primary_key=True, nullable=False, comment='质押方')
    first_holder_name = Column(VARCHAR(128), comment='控股股东')
    shareholding_ratio = Column(DECIMAL(26, 8), comment='（当前股东）股东持股比例')
    pledge_number_holder = Column(BIGINT, comment='（当前股东）累计质押股数')
    pledge_ratio_holder = Column(DECIMAL(26, 8), comment='（当前股东）累计质押占总股本比例')
    pledge_ratio_holder_all = Column(DECIMAL(26, 8), comment='重要股东(持股5%以上)累计质押占总股本比例')
    data_time = Column(DateTime, comment='数据时间')


t_inf_ashare_ipo_type = Table(
    'inf_ashare_ipo_type', metadata,
    Column('stk_code', VARCHAR(12)),
    Column('trd_mkt_code', VARCHAR(12)),
    Column('sec_unique_code', VARCHAR(12)),
    Column('wind_code', VARCHAR(12), comment='wind'),
    Column('co_id', VARCHAR(10), comment='id'),
    Column('co_name', VARCHAR(100)),
    Column('ipo_type_code', VARCHAR(10), comment='ipo'),
    Column('ipo_type_name', VARCHAR(100), comment='ipo'),
    Column('in_date', Integer),
    Column('out_date', Integer),
    Column('latest_flag', VARCHAR(5)),
    Column('opr_date', DateTime),
    Column('opr_type', VARCHAR(5)),
    Column('data_time', DateTime),
    Column('biz_date', Integer),
    comment='A股ipo类型'
)


class LrDiscountRate(Base):
    __tablename__ = 'lr_discount_rate'
    __table_args__ = {'comment': '同业折算率'}

    id = Column(Integer, nullable=False, comment='ID')
    code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    cn_short_name = Column(VARCHAR(12), nullable=False, comment='中文简称')
    created_at = Column(Date, primary_key=True, nullable=False, comment='创建时间')
    status = Column(Integer, comment='证券代码')
    zhongxin = Column(Float, comment='中信证券')
    guotai = Column(Float, comment='国泰君安')
    huatai = Column(Float, comment='华泰证券')
    shenwan = Column(Float, comment='申万宏源')
    zhaoshang = Column(Float, comment='招商证券')
    guangfa = Column(Float, comment='广发证券')
    haitong = Column(Float, comment='海通证券')
    yinhe = Column(Float, comment='银河证券')
    zhongxinjt = Column(Float, comment='中信建投')
    zhongjin = Column(Float, comment='中金证券')
    dongfang = Column(Float, comment='东方证券')
    zhongtai = Column(Float, comment='中泰证券')
    updated_at = Column(DateTime, comment='更新时间')
    fangzheng = Column(Float, comment='方正证券')
    guoxin = Column(Float, comment='国信证券')
    jinyuan = Column(Float, comment='金元')
    wanhe = Column(Float, comment='万和')
    zhongshan = Column(Float, comment='中山')
    caixin = Column(Float, comment='财信')
    guohai = Column(Float, comment='国海')
    diyicy = Column(Float, comment='第一创业')
    zhongyuan = Column(Float, comment='中原')


t_lr_guar_daily_sta = Table(
    'lr_guar_daily_sta', metadata,
    Column('id', Integer, nullable=False, comment='自增ID'),
    Column('create_time', DateTime, comment='创建时间'),
    Column('created_at', Date, nullable=False, comment='统计日期'),
    Column('serial_num', Integer, comment='序号'),
    Column('code', VARCHAR(255), nullable=False, comment='证券代码'),
    Column('sim_cn_name', VARCHAR(255), comment='证券简称'),
    Column('yester_gua_num', VARCHAR(255), comment='上一交易日末担保证券数量（万股）'),
    Column('gua_change_num', VARCHAR(255), comment='当日担保证券数量变动（万股）'),
    Column('fin_gua_num', VARCHAR(255), comment='当日末担保证券数量（万股）'),
    Column('fin_value', VARCHAR(255), comment='当日末担保证券市值（亿元）'),
    Column('fin_total_value', VARCHAR(255), comment='当日末证券总市值（亿元）'),
    Column('accounted', VARCHAR(255), comment='当日末担保证券市值占该证券总市值比重（%）'),
    comment='担保券市值每日数据统计'
)


class LrMarketDailySta(Base):
    __tablename__ = 'lr_market_daily_sta'
    __table_args__ = {'comment': '融资融券市场每日数据统计'}

    id = Column(Integer, primary_key=True, comment='ID')
    created_at = Column(Date, nullable=False, comment='统计日期')
    rz_balance = Column(Float, comment='融资余额（亿）')
    rq_balance = Column(Float, comment='融券余额（亿）')
    a_balance_percent = Column(VARCHAR(255), comment='两融余额占A股流通市值比重')
    rz_buy = Column(Float, comment='融资买入额（亿）')
    rq_sale = Column(Float, comment='融券卖出额（亿）')
    lr_turnover = Column(Float, comment='融资融券交易额（亿）')
    lr_turnover_percent = Column(VARCHAR(255), comment='两融交易额占A股交易额比重')
    comp_num = Column(Float, comment='证券公司数量（家）')
    yyb_num = Column(Float, comment='营业部数量（家）')
    individual_investor_num = Column(Float, comment='个人投资者数量')
    institutional_investor_num = Column(Float, comment='机构投资者数量')
    part_trader_num = Column(Float, comment='参与交易的投资者数量（名）')
    in_debt_num = Column(Float, comment='有融资融券负债的投资者数量（名）')
    mvms = Column(VARCHAR(255), comment='可充抵保证金证券市值（亿元）')
    guarantee_fund = Column(Float, comment='担保资金（亿元）')
    total_value_col = Column(Float, comment='担保物总价值（亿元）')
    ave_gua_ratio = Column(VARCHAR(255), comment='平均维持担保比例')


class MacroDatum(Base):
    __tablename__ = 'macro_data'
    __table_args__ = {'comment': '宏观观测指标表'}

    end_date = Column(Date, primary_key=True, comment='日期')
    M2 = Column(Float, comment='M2货币供应量（亿元）')
    GDP = Column(Float, comment='国内生产总值（亿元）')
    total_val = Column(Float, comment='两市证券总市值（亿元）')
    sh_index = Column(Float, comment='上证指数')
    social_fin = Column(Float, comment='社会融资规模存量（万亿元）')


class MacroStkM2(Base):
    __tablename__ = 'macro_stk_m2'
    __table_args__ = {'comment': '宏观观测-A股融资融券信息表'}

    date = Column(Date, primary_key=True, nullable=False, comment='日期')
    stk_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    cn_short_name = Column(VARCHAR(128), nullable=False, comment='证券简称')
    close_price = Column(Float, comment='收盘价（元）')
    price_limit = Column(Float, comment='涨跌幅(%)')
    financing_balance = Column(BigInteger, comment='融资余额（元）')
    ratio_of_balance = Column(Float, comment='融资余额占流通市值比(%)')
    financing_buy = Column(BigInteger, comment='融资买入（元）')
    financing_repay = Column(BigInteger, comment='融资偿还（元）')
    financing_net_buy = Column(BigInteger, comment='融资净买入（元）')
    securities_balance = Column(BigInteger, comment='融券余额（元）')
    securities_allowance = Column(BigInteger, comment='融券余量（股）')
    securities_sales = Column(BigInteger, comment='融券买入（股）')
    securities_repay = Column(BigInteger, comment='融券偿还（股）')
    securities_net_sales = Column(BigInteger, comment='融券净卖出（股）')
    total_balance = Column(BigInteger, comment='融资融券余额（元）')
    difference_balance = Column(BigInteger, comment='融资融券余额差值（元）')


class MacroTotalM2(Base):
    __tablename__ = 'macro_total_m2'
    __table_args__ = {'comment': '宏观观测-两市总融资融券余额'}

    date = Column(Date, primary_key=True, comment='日期')
    securities_balance = Column(BigInteger, comment='融券余额（元）')
    financing_balance = Column(BigInteger, comment='融资余额（元）')


class MainCirHolder(Base):
    __tablename__ = 'main_cir_holder'
    __table_args__ = {'comment': '中国A股十大流通股东表'}

    stk_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    report_time = Column(Integer, comment='报告日期')
    end_date = Column(Integer, primary_key=True, nullable=False, comment='截止日期')
    shareholder_name = Column(VARCHAR(128), primary_key=True, nullable=False, comment='股东名称')
    shareholder_class = Column(Integer, comment='股东类型')
    share_number = Column(DECIMAL(26, 8), comment='持股数量')
    share_ratio = Column(DECIMAL(26, 8), comment='持股比例')
    shareholder_rank = Column(Integer, comment='股东排名')
    data_time = Column(DateTime, comment='数据时间')
    biz_date = Column(Date, comment='业务日期')


class MainHolder(Base):
    __tablename__ = 'main_holder'
    __table_args__ = {'comment': '中国A股十大股东表'}

    stk_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    report_time = Column(Date, comment='报告日期')
    end_date = Column(Date, primary_key=True, nullable=False, comment='截止日期')
    shareholder_name = Column(VARCHAR(128), primary_key=True, nullable=False, comment='股东名称')
    shareholder_class = Column(Integer, comment='股东类型')
    share_number = Column(DECIMAL(26, 8), comment='持股数量')
    share_ratio = Column(DECIMAL(26, 8), comment='持股比例')
    shareholder_rank = Column(Integer, comment='股东排名')
    data_time = Column(DateTime, comment='更新时间')
    biz_date = Column(Date, comment='创建时间')


class NameChange(Base):
    __tablename__ = 'name_change'
    __table_args__ = {'comment': '中国A股名称变更表'}

    stk_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    change_date = Column(Date, primary_key=True, nullable=False, comment='修改日期')
    change_type = Column(Integer, primary_key=True, nullable=False, comment='修改类型')
    change_reason = Column(TEXT, comment='修改内容')
    data_time = Column(DateTime, comment='数据时间')
    biz_date = Column(Date, comment='业务日期')


class NetShortReal(Base):
    __tablename__ = 'net_short_real'
    __table_args__ = {'comment': '净值'}

    biz_date = Column(Date, primary_key=True, nullable=False, comment='资金账号')
    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='业务日期')
    updated_at = Column(DateTime, comment='更新时间')
    net_short = Column(DECIMAL(10, 4), comment='账户净值')
    type = Column(CHAR(1), comment='类型，0用户净值 ，1沪深300，2无风险收益率')
    year_return_rate = Column(DECIMAL(10, 4), comment='收益率，近一年')
    share = Column(DECIMAL(20, 4), comment='份额')
    is_effective_trade_day = Column(BIT(1), comment='是否有效交易日')


class PdFinancierAttPool(Base):
    __tablename__ = 'pd_financier_att_pool'
    __table_args__ = {'comment': '质押关注池'}

    target_company = Column(VARCHAR(255), comment='标的公司名称')
    holding_company = Column(VARCHAR(255), comment='持股公司名称')
    project_name = Column(VARCHAR(255), comment='对应项目')
    attention_tag = Column(Integer, primary_key=True, nullable=False, comment='关注类型(项目关注，自选关注)')
    add_tag = Column(Integer, primary_key=True, nullable=False, comment='区分个人和机构添加(融资人类别)')
    user_id = Column(Integer, primary_key=True, nullable=False, comment='用户ID')
    id_card = Column(VARCHAR(255), primary_key=True, nullable=False, comment='身份证号/组织机构代码')
    name = Column(VARCHAR(100), comment='融资人姓名')
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    fund_id = Column(String(32, 'utf8mb4_general_ci'), comment='融资人信用账户')


class PdRiskLevel(Base):
    __tablename__ = 'pd_risk_level'
    __table_args__ = {'comment': '舆情列表 证券风险等级和风险事件'}

    stk_code = Column(VARCHAR(10), primary_key=True, comment='证券代码')
    risk_level = Column(VARCHAR(4), comment='风险等级，0:无风险,1:一般风险,2:高风险, 默认0')
    biz_date = Column(Date, comment='更新时间')
    risk_items = Column(VARCHAR(100), comment='风险事件')


class PdTag(Base):
    __tablename__ = 'pd_tag'
    __table_args__ = {'comment': '质押券风险标签'}

    tag_id = Column(Integer, primary_key=True, comment='自增id')
    tag_name = Column(VARCHAR(100), comment='标签名')
    type = Column(VARCHAR(100), comment='一级分类（新闻，公告，金融监管事件）')
    cls = Column(VARCHAR(100), comment='二级分类')


class PdUnderlyingSecuritiesPool(Base):
    __tablename__ = 'pd_underlying_securities_pool'
    __table_args__ = {'comment': '质押标的池'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    user_id = Column(Integer, primary_key=True, nullable=False, comment='用户ID')
    att_id = Column(Integer, primary_key=True, nullable=False, comment='添加类型（项目关注，自选关注）')
    create_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')


class PdUserAttentionTag(Base):
    __tablename__ = 'pd_user_attention_tag'
    __table_args__ = {'comment': '质押分组标签信息'}

    group_id = Column(Integer, primary_key=True, comment='自增ID')
    user_id = Column(Integer, comment='用户ID')
    group_name = Column(VARCHAR(20), comment='分组名称')
    tags = Column(JSON, comment='关注标签')
    update_date = Column(Date, comment='更新时间')


class PlanTrialCalculation(Base):
    __tablename__ = 'plan_trial_calculation'
    __table_args__ = {'comment': '计划试算'}

    id = Column(Integer, primary_key=True, comment='ID')
    name = Column(VARCHAR(64), nullable=False, comment='任务名称')
    code_list = Column(JSON, nullable=False, comment='公司列表')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by = Column(Integer, nullable=False, comment='创建人')
    created_by_name = Column(VARCHAR(120), comment='创建人姓名')
    status = Column(Integer, nullable=False, server_default=text("'0'"), comment='状态（0：计算中；1：计算完成）')
    end_at = Column(DateTime, comment='结束时间')
    department_id = Column(Integer, nullable=False, index=True, comment='部门ID')
    period = Column(VARCHAR(32), comment='计算周期')


class PlanTrialCalculationItem(Base):
    __tablename__ = 'plan_trial_calculation_item'
    __table_args__ = {'comment': '计划试算项'}

    plan_trial_calculation_id = Column(Integer, nullable=False, comment='试算任务ID')
    id = Column(Integer, primary_key=True, comment='ID')
    plan_id = Column(Integer, index=True, comment='方案ID')
    plan_name = Column(VARCHAR(64), nullable=False, comment='方案名称')
    rating_item_list = Column(JSON, nullable=False, comment='评分项配置')
    total_score_list = Column(JSON, nullable=False, comment='汇总分配置')
    total_score_process_list = Column(JSON, nullable=False, comment='后处理配置')
    securities_metrics_list = Column(JSON, nullable=False, comment='指标列表')
    created_by = Column(Integer, nullable=False, comment='创建人')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by_name = Column(VARCHAR(120), comment='创建人名称')


class PlanTrialCalculationResult(Base):
    __tablename__ = 'plan_trial_calculation_result'
    __table_args__ = (
        Index('only_id_id', 'plan_trial_calculation_item_id', 'securities_code', 'date', unique=True),
        {'comment': '计划试算结果'}
    )

    plan_trial_calculation_item_id = Column(Integer, nullable=False, index=True, comment='试算任务方案ID')
    id = Column(Integer, primary_key=True, comment='ID')
    securities_code = Column(VARCHAR(12), nullable=False, comment='证券代码')
    final_score = Column(Float, comment='最终得分')
    date = Column(Date, nullable=False, comment='得分日期')
    created_at = Column(TIMESTAMP, nullable=False)


class PledgerateBefore(Base):
    __tablename__ = 'pledgerate_before'
    __table_args__ = {'comment': '券商折算率（手动导入）'}

    stk_code = Column(VARCHAR(10), primary_key=True, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    rate = Column(DECIMAL(26, 4), comment='折算率')
    created_at = Column(Date, comment='创建时间')
    update_at = Column(Date, comment='更新日期')


class PledgeratePeriodAdj(Base):
    __tablename__ = 'pledgerate_period_adj'
    __table_args__ = {'comment': '折算率管理'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    stk_type = Column(VARCHAR(20), comment='证券类型(S: 股票;F：基金;B：债券)')
    is_collateral = Column(Integer, comment='交易所担保品(上、深官网爬取，债券/基金默认是1)')
    status = Column(VARCHAR(16), comment='状态')
    pledge_rate_limit = Column(DECIMAL(26, 4), comment='折算率上限')
    period_adj = Column(DECIMAL(26, 4), comment='定调折算率')
    model_pledge_rate = Column(DECIMAL(26, 4), comment='模型折算率')
    advice_pledge_rate = Column(DECIMAL(26, 4), comment='建议折算率')
    manual_pledge_rate = Column(DECIMAL(26, 4), comment='手动调整')
    pledge_rate_before = Column(DECIMAL(26, 4), comment='调整前折算率')
    pledge_rate_after = Column(DECIMAL(26, 4), comment='调整后折算率')
    adj_way = Column(VARCHAR(10), comment='调整方式')
    adj_reason = Column(VARCHAR(20), comment='调整原因')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')


class PledgeratePeriodAdjReport(Base):
    __tablename__ = 'pledgerate_period_adj_report'
    __table_args__ = {'comment': '折算率担保券公告'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    stk_type = Column(VARCHAR(10), comment='证券类型')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    margin_pledge_rate_in = Column(VARCHAR(10), comment='可冲抵保证金及折算率-调入')
    margin_pledge_rate_out = Column(VARCHAR(10), comment='可冲抵保证金及折算率-调出')
    margin_pledge_rate_before = Column(VARCHAR(10), comment='可冲抵保证金及折算率-调整前')
    margin_pledge_rate_after = Column(VARCHAR(10), comment='可冲抵保证金及折算率-调整后')
    margin_finance_rate_in = Column(VARCHAR(10), comment='融资标的及其保证金比例-调入')
    margin_finance_rate_out = Column(VARCHAR(10), comment='融资标的及其保证金比例-调出')
    margin_finance_rate_before = Column(VARCHAR(10), comment='融资标的及其保证金比例-调整前')
    margin_finance_rate_after = Column(VARCHAR(10), comment='融资标的及其保证金比例-调整后')
    margin_securities_rate_in = Column(VARCHAR(20), comment='融资券的及其保证金比例-调入')
    margin_securities_rate_out = Column(VARCHAR(20), comment='融资券的及其保证金比例-调出')
    margin_securities_rate_before = Column(VARCHAR(10), comment='融券标的及其保证金比例-调整前')
    margin_securities_rate_after = Column(VARCHAR(20), comment='融券标的及其保证金比例-调整后')


class PledgeratePeriodAdjStatu(Base):
    __tablename__ = 'pledgerate_period_adj_status'
    __table_args__ = {'comment': '折算率保证金比例定调-中间表'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    stk_type = Column(VARCHAR(20), comment='证券类型')
    stk_cname = Column(VARCHAR(20), comment='证券中文全称')
    is_collateral = Column(Integer, comment='是否交易所担保品')
    change_date = Column(Date, primary_key=True, nullable=False, comment='公告日期')
    change_thing = Column(VARCHAR(25), comment='变动事项')
    stk_category = Column(VARCHAR(20), comment='证券分类(详细)')
    trading_market = Column(VARCHAR(20), comment='交易市场')
    pe = Column(DECIMAL(26, 4), comment='静态市盈率')
    sh180 = Column(VARCHAR(2), comment='上证180')
    sz100 = Column(VARCHAR(2), comment='深圳100')
    listed_day = Column(VARCHAR(25), comment='上市天数')


class PubDate(Base):
    __tablename__ = 'pub_date'
    __table_args__ = {'comment': '交易日历'}

    date_code = Column(DECIMAL(8, 0), primary_key=True, comment='日期代码')
    date_desc = Column(VARCHAR(30), comment='日期描述')
    wk_of_year_code = Column(DECIMAL(8, 0), comment='周代码')
    wk_of_year_lbl = Column(VARCHAR(10), comment='周标签')
    wk_of_year_desc = Column(VARCHAR(30), comment='周描述')
    mth_code = Column(DECIMAL(8, 0), comment='月份代码')
    mth_lbl = Column(VARCHAR(10), comment='月份标签')
    mth_desc = Column(VARCHAR(30), comment='月份描述')
    quar_code = Column(DECIMAL(8, 0), comment='季度代码')
    quar_lbl = Column(VARCHAR(10), comment='季度标签')
    quar_desc = Column(VARCHAR(30), comment='季度描述')
    six_months_code = Column(DECIMAL(8, 0), comment='上下半年代码')
    six_months_desc = Column(VARCHAR(30), comment='上下半年描述')
    year_code = Column(DECIMAL(8, 0), comment='年份代码')
    year_desc = Column(VARCHAR(30), comment='年份描述')
    wk_start_flag = Column(VARCHAR(30), comment='周开始标志')
    wk_end_flag = Column(VARCHAR(30), comment='周结束标志')
    mth_start_flag = Column(VARCHAR(30), comment='月开始标志')
    mth_end_flag = Column(VARCHAR(30), comment='月结束标志')
    quar_start_flag = Column(VARCHAR(30), comment='季开始标志')
    quar_end_flag = Column(VARCHAR(30), comment='季结束标志')
    year_start_flag = Column(VARCHAR(30), comment='年开始标志')
    year_end_flag = Column(VARCHAR(30), comment='年结束标志')
    trd_daily_flag = Column(CHAR(1), comment='交易日标志')
    etl_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='ETL日期')
    hkex_trd_daily_flag = Column(CHAR(1), comment='港交所交易日标志')
    hgt_trd_daily_flag = Column(CHAR(1), comment='沪港通交易日标志')
    six_months_lbl = Column(VARCHAR(10), comment='上下半年标签')


class RatingItem(Base):
    __tablename__ = 'rating_item'
    __table_args__ = {'comment': '评分项'}

    id = Column(Integer, primary_key=True, comment='ID')
    department_id = Column(Integer, nullable=False, index=True, comment='部门ID')
    type_id = Column(Integer, index=True, comment='类别ID')
    name = Column(VARCHAR(64), nullable=False, comment='评分项名称')
    status = Column(Integer, nullable=False, server_default=text("'1'"), comment='状态（0：删除；1：正常）')
    created_by = Column(Integer, nullable=False, comment='创建人')
    updated_at = Column(DateTime, nullable=False, comment='更新时间')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by_name = Column(String(120), comment='创建人姓名')


class RatingItemRule(Base):
    __tablename__ = 'rating_item_rule'
    __table_args__ = {'comment': '评分项规则'}

    id = Column(Integer, primary_key=True, comment='ID')
    rating_item_id = Column(Integer, nullable=False, index=True, comment='评分项id')


class RatingItemRuleResult(Base):
    __tablename__ = 'rating_item_rule_results'
    __table_args__ = {'comment': '评分项规则项'}

    id = Column(Integer, primary_key=True, comment='ID')
    rating_item_rule_id = Column(Integer, nullable=False, index=True, comment='评分项规则id')
    name = Column(VARCHAR(64), nullable=False)
    form = Column(VARCHAR(64))
    text = Column(VARCHAR(64))
    type = Column(VARCHAR(64), nullable=False)


class RatingItemRuleTerm(Base):
    __tablename__ = 'rating_item_rule_terms'
    __table_args__ = {'comment': '评分项规则结果'}

    id = Column(Integer, primary_key=True, comment='ID')
    rating_item_rule_id = Column(Integer, nullable=False, index=True, comment='评分项规则id')
    name = Column(VARCHAR(64), nullable=False)
    form = Column(VARCHAR(64))
    text = Column(VARCHAR(64))
    type = Column(VARCHAR(64), nullable=False)


class RePlan(Base):
    __tablename__ = 're_plan'
    __table_args__ = {'comment': '方案表'}

    plan_id = Column(BIGINT, primary_key=True, comment='自增ID')
    plan_name = Column(VARCHAR(64), nullable=False, server_default=text("''"), comment='方案名称')
    plan_type = Column(VARCHAR(32), nullable=False, server_default=text("'0'"), comment='类型，1-担保券评分 2-质押评分 3-折算率定调 4-证券异动')
    descs = Column(VARCHAR(100), comment='方案描述')
    is_enable = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='是否启用，0-否 1-是')
    created_by = Column(Integer, nullable=False, server_default=text("'0'"), comment='创建人ID')
    created_by_name = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='创建人名字')
    gmt_create = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')
    modify_by_name = Column(VARCHAR(100), comment='修改人名字')
    period = Column(VARCHAR(32), comment='计算周期')
    oper_by_name = Column(VARCHAR(100), comment='操作人名字')
    special_config = Column(JSON, comment='方案类配置')
    status = Column(Integer, server_default=text("'0'"), comment='方案状态:0:切换完成;1:切换中;2:切换失败')
    ref_id = Column(BigInteger, comment='方案引用ID (方案如果被模型评分引用, 需要在方案中设置该字段为模型评分的 ID)')
    use_begin_time = Column(DateTime, comment='使用方案的开始时间')


class ReResult(Base):
    __tablename__ = 're_result'
    __table_args__ = (
        Index('uk_biz_date_biz_id_plan_id_var_id', 'biz_date', 'biz_id', 'plan_id', 'var_id', unique=True),
        {'comment': '变量结果表'}
    )

    result_id = Column(BIGINT, primary_key=True, comment='自增ID')
    plan_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='方案ID')
    stage = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='阶段，业务中使用，如评分模型：1-评分项 2-汇总分 3-风险评分')
    var_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='变量ID')
    rule_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='规则ID')
    biz_id = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='业务ID，如证券代码')
    biz_date = Column(Date, nullable=False, comment='业务时间')
    ret_value = Column(TEXT, comment='规则返回值')
    show_text = Column(TEXT, comment='展示内容')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)


class ReRule(Base):
    __tablename__ = 're_rule'
    __table_args__ = {'comment': '分段规则明细表'}

    rule_id = Column(BIGINT, primary_key=True, comment='自增ID')
    var_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='变量ID')
    serial_no = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='规则编号')
    if_expr = Column(TEXT, nullable=False, comment='条件表达式')
    ret_expr = Column(TEXT, nullable=False, comment='返回表达式')
    expr_type = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='表达式类型，1-数字计算 2-文本类型')
    params = Column(TEXT, comment='使用到的参数')
    calc_fields = Column(TEXT, comment='需要计算的字段')
    is_enable = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='是否开启，0-否 1-是')
    web_cfg = Column(JSON, comment='前端配置')
    remark = Column(JSON, comment='额外信息')


class ReRuleShow(Base):
    __tablename__ = 're_rule_show'
    __table_args__ = {'comment': '分段规则文案'}

    id = Column(BIGINT, primary_key=True, comment='自增主键')
    plan_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='方案ID')
    rule_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='规则ID')
    type = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='类型，sec_rate-折算率 fun_rate-保证金比例')
    market = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='市场')
    stk_type = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='证券品种')
    stk_sort = Column(VARCHAR(100), nullable=False, server_default=text("''"), comment='证券分类')
    range_in = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='调入范围')
    adj_rule = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='调整规则')
    pledgerate_period_adj = Column(DECIMAL(26, 4), comment='定调折算率')
    rz_guarantee_rate = Column(VARCHAR(100), comment='融资保证金比例')
    rq_guarantee_rate = Column(VARCHAR(100), comment='融券保证金比例')
    guarantee_adj_reason = Column(VARCHAR(100), server_default=text("''"), comment='担保券调整原因')
    underlying_adj_reason = Column(VARCHAR(100), server_default=text("''"), comment='标的券调整原因')
    create_by = Column(Integer, nullable=False, server_default=text("'0'"), comment='录入人ID')
    create_by_name = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='录入人名字')
    gmt_create = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='修改时间')


class ReVariable(Base):
    __tablename__ = 're_variable'
    __table_args__ = {'comment': '变量表'}

    var_id = Column(BIGINT, primary_key=True, comment='自增ID')
    plan_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='方案ID')
    var_name = Column(VARCHAR(32), nullable=False, server_default=text("''"), comment='变量名称')
    scope = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='作用域，1-共用 2-私有')
    var_type = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='变量类型，1-评分项 2-汇总分 3-风险评分 4-折算率定调 5-证券异动')
    calc_type = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='计算类型，1-匹配第一项 2-匹配最后一项 3-取最小值')
    calc_params = Column(TEXT, comment='计算参数')
    stage = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='阶段，业务中使用，如评分模型：1-评分项 2-汇总分 3-风险评分')
    ret_type = Column(TINYINT, nullable=False, comment='结果类型，1-Double 2-String')
    ret_default = Column(TEXT, comment='结果默认值，匹配不到时使用')
    ref_var_id = Column(BigInteger, nullable=False, server_default=text("'0'"), comment='关联ID')
    is_enable = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='是否生效，0-否 1-是')
    show_text_cfg = Column(TEXT, comment='显示文案配置')


class RiskScoreHist(Base):
    __tablename__ = 'risk_score_hist'
    __table_args__ = {'comment': '财务风险分数表（历史）'}

    id = Column(Integer, primary_key=True, comment='ID')
    comp_code = Column(VARCHAR(12), nullable=False, comment='证券代码')
    end_date = Column(Date, nullable=False, comment='截止日期')
    risk_score = Column(Float, nullable=False, comment='公司风险得分')
    risk_score_indu = Column(Float, comment='风险得分_行业中位数')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')


class RzrqBizRiskIndex(Base):
    __tablename__ = 'rzrq_biz_risk_index'
    __table_args__ = {'comment': '融资融券业务风险指标表'}

    range_ind = Column(VARCHAR(60), primary_key=True, comment='范围_指标(全英文 用作主键  sc证券公司 ws西部证券 )')
    range = Column(VARCHAR(30), comment='范围(中文)')
    biz_sort = Column(VARCHAR(30), comment='业务分类')
    index = Column(VARCHAR(100), comment='指标(中文)')
    curr_val = Column(DECIMAL(26, 4), comment='当前值')
    index_status = Column(Integer, comment='指标状态 安全-0 预警-1 触警-2')
    regulatory_std = Column(VARCHAR(30), comment='监管标准')
    comp_std = Column(VARCHAR(30), comment='公司标准')
    warning_val = Column(VARCHAR(30), comment='预警阀值')


class RzrqComDatum(Base):
    __tablename__ = 'rzrq_com_data'
    __table_args__ = {'comment': '公司合计融资融券余额信息表'}

    biz_date = Column(Date, primary_key=True, index=True, comment='数据日期')
    fin_avl_amt = Column(DECIMAL(26, 4), comment='融资余额')
    secu_avl_amt = Column(DECIMAL(26, 4), comment='融券余额')
    fin_secu_avl_amt = Column(DECIMAL(26, 4), comment='两融余额')


class RzrqCustOrg(Base):
    __tablename__ = 'rzrq_cust_orgs'
    __table_args__ = {'comment': '营业部融资融券客户数信息表'}

    biz_date = Column(Date, primary_key=True, nullable=False, index=True, comment='数据日期')
    fin_avl_amt = Column(DECIMAL(26, 4), comment='融资余额')
    secu_avl_amt = Column(DECIMAL(26, 4), comment='融券余额')
    fin_secu_avl_amt = Column(DECIMAL(26, 4), comment='两融余额')
    cust_count = Column(Integer, comment='客户数')
    keeprate_range = Column(VARCHAR(26), primary_key=True, nullable=False, comment='维保比例范围,左闭右开，目前只有-1.0_1.3和1.3_1.5两种')
    belong_org_id = Column(Integer, primary_key=True, nullable=False, comment='营业部代码（0为所有的）')


class RzrqDatum(Base):
    __tablename__ = 'rzrq_data'
    __table_args__ = {'comment': '融资融券数据表'}

    biz_date = Column(Date, primary_key=True, comment='数据日期')
    fin_avl_amt = Column(DECIMAL(26, 4), comment='融资余额（亿）')
    secu_avl_amt = Column(DECIMAL(26, 4), comment='融券余额（亿）')
    fin_secu_avl_amt = Column(DECIMAL(26, 4), comment='融资融券余额（亿）')
    a_balance_percent = Column(VARCHAR(255), comment='两融余额占A股流通市值比重')
    rz_buy = Column(DECIMAL(26, 4), comment='融资买入额（亿）')
    rq_sale = Column(Float, comment='融券卖出额（亿）')
    lr_turnover = Column(Float, comment='融资融券交易额（亿）')
    lr_turnover_percent = Column(VARCHAR(255), comment='两融交易额占A股交易额比重')


class RzrqMarketDatum(Base):
    __tablename__ = 'rzrq_market_data'
    __table_args__ = {'comment': '融资融券全市场数据'}

    biz_date = Column(Date, primary_key=True, nullable=False)
    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    market = Column(CHAR(1), comment='市场(1深交，2上交)')
    fin_secu_avl_amt = Column(DECIMAL(26, 4), comment='融资融券余额（元）')
    fin_avl_amt = Column(DECIMAL(26, 4), comment='融资余额（元）')
    rz_buy = Column(DECIMAL(26, 4), comment='融资买入额（元）')
    secu_avl_amt = Column(DECIMAL(26, 4), comment='融券余额（元）')
    rq_sale_qty = Column(DECIMAL(26, 4), comment='融券卖出量 (股/份)')
    pred_guar_securities_qty = Column(Float, comment='上一交易日末担保证券数量（万股）')
    curd_guar_securities_qty_change = Column(Float, comment='当日担保证券数量变动（万股）')
    curd_guar_securities_qty = Column(Float, comment='当日末担保证券数量 （万股）')
    curd_guar_securities_mkt = Column(Float, comment='当日末担保证券市值（亿元）')
    curd_securities_mkt = Column(Float, comment='当日日末证券总市值（亿元）')
    guar_sec_prop = Column(Float, comment='当日日末担保证券市值占该证券总市值比重（%）')
    flag = Column(Integer, primary_key=True, nullable=False, comment='标记位 用于区分 证金数据-1 、交易数据-2')


class SecAcctInfo(Base):
    __tablename__ = 'sec_acct_info'
    __table_args__ = {'comment': '股东账户表'}

    biz_date = Column(Date, primary_key=True, nullable=False, comment=' 业务日期')
    data_label = Column(VARCHAR(4), primary_key=True, nullable=False, comment=' 数据标签')
    secu_acct = Column(VARCHAR(100), primary_key=True, nullable=False, comment=' 股东账户')
    fund_id = Column(VARCHAR(19), primary_key=True, nullable=False, comment=' 资金账号')
    open_acct_dt = Column(Date, comment=' 开户日期')
    close_acct_dt = Column(Date, comment=' 销户日期')
    acct_status = Column(CHAR(4), comment=' 账户状态')
    trade_mrkt = Column(VARCHAR(4), comment=' 交易所')
    trade_board = Column(VARCHAR(4), primary_key=True, nullable=False, comment=' 交易板块')
    trade_prvlg = Column(VARCHAR(10), comment=' 股东账户交易权限')
    spec_trade_seat = Column(VARCHAR(100), comment=' 股东指定席位')
    acct_type = Column(VARCHAR(10), comment=' 账户类别')
    credit_flag = Column(VARCHAR(10), comment='信用标志')


class SecAcctPo(Base):
    __tablename__ = 'sec_acct_pos'
    __table_args__ = {'comment': '账户持仓表'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资产账户')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    cust_id = Column(VARCHAR(19), comment='客户代码')
    cust_char = Column(VARCHAR(4), comment='客户性质（0-个人，1-机构）')
    data_label = Column(VARCHAR(4), primary_key=True, nullable=False, comment='数据标签，区分来自宏源(HY)还是申万(SW)的数据')
    belong_org_id = Column(VARCHAR(12), comment='归属机构编号')
    crdt_acct_flag = Column(CHAR(1), comment='信用账户标志')
    secu_acct = Column(VARCHAR(100), comment='证券账户')
    trade_mrkt = Column(VARCHAR(4), comment='交易市场')
    trade_board = Column(VARCHAR(12), comment='交易板块')
    stk_code = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    secu_cate_code = Column(VARCHAR(4), comment='证券类别代码')
    orig_curr_code = Column(CHAR(1), comment='原币种代码')
    share_bal = Column(DECIMAL(26, 4), comment='股份余额')
    price = Column(DECIMAL(26, 4), comment='价格')
    orig_curr_mrkt_val = Column(DECIMAL(26, 4), comment='原币种市值')
    exch_rate = Column(DECIMAL(10, 6), comment='汇率')
    mrkt_val_rmb = Column(DECIMAL(26, 4), comment='折人民币市值')
    ref_cost = Column(DECIMAL(26, 4), comment='参考成本')
    ref_mrkt_val = Column(DECIMAL(26, 4), comment='参考市值')


class SecBkseBizEvt(Base):
    __tablename__ = 'sec_bkse_biz_evt'
    __table_args__ = {'comment': '资金股份变动流水表'}

    data_label = Column(VARCHAR(10), primary_key=True, nullable=False, comment=' 数据标签')
    evt_id = Column(VARCHAR(200), comment=' 事件编号')
    trade_dt = Column(Date, comment=' 交易日期')
    in_org_id = Column(VARCHAR(80), comment=' 内部机构')
    bank_cd = Column(VARCHAR(20), comment=' 银行代码')
    cust_bdmf_acct = Column(VARCHAR(32), comment=' 客户存管账户')
    depo_bank_id = Column(VARCHAR(80), comment=' 管理账号')
    new_depo_bank_id = Column(VARCHAR(80), comment=' 新管理账号')
    sett_acct = Column(VARCHAR(80), comment=' 结算账号')
    trade_tm = Column(TIMESTAMP(fsp=6), comment=' 交易时间')
    secu_serial_no = Column(VARCHAR(40), comment=' 证券流水号')
    bank_serial_no = Column(VARCHAR(40), comment=' 银行流水号')
    spon_flag = Column(VARCHAR(4), comment=' 发起方')
    trade_type_cd = Column(VARCHAR(2), comment=' 交易类型')
    curr_cd = Column(CHAR(1), comment=' 币种')
    amt = Column(DECIMAL(26, 4), comment=' 发生金额')
    ext_msg = Column(VARCHAR(256), comment=' 外部信息')
    ser_num = Column(VARCHAR(50), primary_key=True, nullable=False, comment=' 流水序号')
    current_dt = Column(Date, comment=' 当前日期')
    current_tm = Column(Integer, comment=' 当前时间')
    chan_id = Column(VARCHAR(4), comment=' 渠道编号')
    oper_bran_org = Column(VARCHAR(10), comment=' 操作分支机构')
    station_addr = Column(VARCHAR(256), comment=' 站点地址')
    operr_cd = Column(VARCHAR(40), comment=' 操作员代码')
    cust_id = Column(VARCHAR(18), primary_key=True, nullable=False, comment=' 客户代码')
    cust_no = Column(VARCHAR(18), comment=' 客户编号')
    fin_asset_acct = Column(VARCHAR(18), comment=' 理财资金账户')
    trade_type = Column(VARCHAR(12), comment=' 交易类型')
    comm = Column(DECIMAL(19, 2), comment=' 手续费')
    post_amt = Column(DECIMAL(19, 2), comment=' 后资金额')
    bktrans_status = Column(VARCHAR(2), comment=' 请求状态')
    decl_tm = Column(Integer, comment=' 申报时间')
    id_type = Column(VARCHAR(4), comment='证件类别')
    id_code = Column(VARCHAR(50), comment=' 证件号码')
    biz_date = Column(Date, primary_key=True, nullable=False, comment=' 清算日期')
    strike_cnt = Column(Integer, comment=' 冲正次数')
    secu_num = Column(VARCHAR(16), comment=' 证券商号')
    secu_term_num = Column(VARCHAR(8), comment=' 证券商终端号')
    bank_open = Column(VARCHAR(16), comment=' 银行操作员')
    rela_biz_type = Column(VARCHAR(1), comment=' 关联业务类型（空值）')
    err_cd = Column(VARCHAR(10), comment=' 错误代码')
    secu_acct = Column(VARCHAR(40), comment=' 证券账号')
    co_seq_num = Column(VARCHAR(40), comment=' 协作流水号')
    asset_prop = Column(VARCHAR(1), comment=' 资产属性（空值）')
    org_flag = Column(CHAR(1), comment=' 机构标志')
    biz_type = Column(VARCHAR(1), comment=' 业务类型（空值）')
    trans_bran_cd = Column(VARCHAR(10), comment=' 转发分支代码')
    resend_num = Column(Integer, comment=' 重发次数')
    bank_err_info = Column(VARCHAR(2000), comment=' 银行错误信息')
    cancel_seq_num = Column(VARCHAR(64), comment=' 冲销流水号')
    brh_org_id = Column(VARCHAR(20), comment=' 分支机构编号')
    other_oper_addr = Column(VARCHAR(300), comment=' 其他操作地址')
    cust_name = Column(VARCHAR(200), comment=' 客户名称')
    memo = Column(VARCHAR(500), comment=' 备注')
    strike_flag = Column(VARCHAR(4), comment=' 冲正标志')
    dohist_cd = Column(VARCHAR(4), comment=' 归档代码')


class SecCapStkChangeEvt(Base):
    __tablename__ = 'sec_cap_stk_change_evt'
    __table_args__ = {'comment': '资金股份变动流水表'}

    data_label = Column(VARCHAR(4), primary_key=True, nullable=False, comment=' 数据标签')
    evt_id = Column(VARCHAR(200), comment=' 事件编号')
    biz_date = Column(Date, primary_key=True, nullable=False, comment=' 清算日期')
    occur_dt = Column(Date, comment=' 发生日期')
    occur_tm = Column(Integer, comment=' 发生时间')
    oper_dt = Column(Date, comment=' 操作日期')
    cap_arrv_dt = Column(Date, comment=' 资金到账日期')
    ser_num = Column(VARCHAR(500), primary_key=True, nullable=False, comment=' 流水序号')
    contr_seq_num = Column(VARCHAR(50), comment=' 合同序号')
    cust_cd = Column(VARCHAR(80), comment=' 客户代码')
    cust_name = Column(VARCHAR(200), comment=' 客户名称')
    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment=' 资金账号')
    curr_cd = Column(CHAR(1), comment=' 币种代码')
    belong_org_id = Column(VARCHAR(4), comment=' 归属机构编号')
    brh_org_id = Column(VARCHAR(20), comment=' 分支机构编号')
    init_org_id = Column(VARCHAR(10), comment=' 发起机构编号')
    secu_acct = Column(VARCHAR(100), comment=' 证券账户')
    trade_seat = Column(VARCHAR(6), comment=' 交易席位')
    trade_mrkt = Column(VARCHAR(4), comment=' 交易市场')
    trade_board = Column(VARCHAR(4), comment=' 交易板块')
    prod_id = Column(VARCHAR(60), comment=' 产品编号')
    secu_cd = Column(VARCHAR(20), comment=' 证券代码')
    secu_name = Column(VARCHAR(20), comment=' 证券名称')
    secu_cate_cd = Column(VARCHAR(4), comment=' 证券类别代码')
    src_secu_cate_cd = Column(VARCHAR(4), comment=' 源证券类别代码')
    biz_cd = Column(VARCHAR(50), comment=' 业务代码')
    src_biz_cd = Column(VARCHAR(50), comment=' 源业务代码')
    secu_trade_type_cd = Column(VARCHAR(4), comment=' 证券交易类型代码')
    depo_bank_id = Column(VARCHAR(80), comment=' 存管银行编号')
    depo_bank_acct = Column(VARCHAR(100), comment=' 存管银行账号')
    amt = Column(DECIMAL(26, 4), comment=' 发生金额')
    cap_bal = Column(DECIMAL(26, 4), comment=' 资金余额')
    share_occur_num = Column(DECIMAL(26, 0), comment=' 股份发生数')
    share_bal = Column(DECIMAL(26, 0), comment=' 股份余额')
    order_price = Column(DECIMAL(26, 6), comment=' 委托价格')
    order_qtty = Column(DECIMAL(26, 0), comment=' 委托数量')
    bond_intr = Column(DECIMAL(26, 4), comment=' 债券应计利息')
    match_price = Column(DECIMAL(26, 5), comment=' 成交价格')
    match_qtty = Column(DECIMAL(26, 0), comment=' 成交数量')
    match_amt = Column(DECIMAL(26, 4), comment=' 成交金额')
    match_times = Column(Integer, comment=' 成交笔数')
    commission = Column(DECIMAL(26, 2), comment=' 手续费')
    net_commission = Column(DECIMAL(26, 2), comment=' 净手续费')
    stamp_duty = Column(DECIMAL(26, 2), comment=' 印花税')
    tran_fee = Column(DECIMAL(26, 2), comment=' 过户费')
    clear_fee = Column(DECIMAL(26, 2), comment=' 清算费')
    transt_fee = Column(DECIMAL(26, 2), comment=' 交易规费')
    other_fee = Column(DECIMAL(26, 2), comment=' 其他费用')
    front_fee = Column(DECIMAL(26, 2), comment=' 前台费用')
    actl_change_fee = Column(DECIMAL(26, 4), comment=' 实际收取费用')
    exch_tran_fee = Column(DECIMAL(26, 2), comment=' 交易所过户费')
    clear_corp_sett_fee = Column(DECIMAL(26, 2), comment=' 结算公司结算费')
    exch_transt_fee = Column(DECIMAL(26, 2), comment=' 交易所交易规费')
    hand_fee = Column(DECIMAL(26, 2), comment=' 经手费')
    manage_fee = Column(DECIMAL(26, 2), comment=' 管理费')
    risk_amt = Column(DECIMAL(26, 2), comment=' 风险金')
    match_id = Column(VARCHAR(100), comment=' 成交编号')
    order_dt = Column(Date, comment=' 委托日期')
    order_tm = Column(Integer, comment=' 委托时间')
    match_tm = Column(Integer, comment=' 成交时间')
    operr_cd = Column(VARCHAR(80), comment=' 操作员代码')
    operr_name = Column(VARCHAR(16), comment=' 操作员名称')
    oper_ip_addr = Column(VARCHAR(32), comment=' 操作IP地址')
    chan_id = Column(VARCHAR(4), comment=' 渠道编号')
    exch_rate = Column(DECIMAL(16, 10), comment=' 汇率')
    order_evt_id = Column(VARCHAR(200), comment=' 委托事件编号')
    prft_amt = Column(DECIMAL(26, 4), comment=' 收益金额')
    memo = Column(VARCHAR(2000), comment=' 备注')
    check_status_cd = Column(VARCHAR(4), comment=' 复核状态代码')
    cancel_status_cd = Column(VARCHAR(4), comment=' 撤单状态代码')
    order_ser_num = Column(VARCHAR(50), comment=' 委托流水序号')
    spon_cd = Column(VARCHAR(4), comment='发起方代码（不需要字典）')
    src_sys_trade_behav_cd = Column(VARCHAR(4), comment=' 源系统交易行为代码')
    std_trade_behav_cd = Column(VARCHAR(10), comment=' 标准交易行为代码')
    busi_sort_cd = Column(VARCHAR(10), comment=' 业务分类代码')
    ref_ser_num = Column(VARCHAR(100), comment=' 关联流水序号')
    crdt_prod_flag = Column(VARCHAR(4), comment=' 信用产品标志')
    credit_trade_type_cd = Column(VARCHAR(4), comment=' 信用交易类型代码')
    bb_prod_id = Column(VARCHAR(4), comment=' 回购产品编号')
    rela_dt = Column(Date, comment=' 关联日期')
    rela_tm = Column(Integer, comment=' 关联时间')
    rela_busi_ser_num = Column(VARCHAR(50), comment=' 关联业务流水序号')
    rela_busi_cd = Column(VARCHAR(50), comment=' 关联业务代码')
    rela_busi_name = Column(VARCHAR(100), comment=' 关联业务名称')
    ext_inst = Column(VARCHAR(50), comment=' 外部机构')
    fin_secu_contr_num = Column(VARCHAR(40), comment=' 融资融券合同号')
    crdt_sort_cd = Column(VARCHAR(4), comment=' 信用分类代码')
    sys_src_cd = Column(VARCHAR(4), comment=' 系统来源代码')


class SecCollateral(Base):
    __tablename__ = 'sec_collateral'
    __table_args__ = {'comment': '担保物信息表（日终算一次）'}

    stk_code = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券简称')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    indu_code = Column(VARCHAR(32), comment='申万一级行业代码')
    indu_name = Column(VARCHAR(64), comment='申万一级行业')
    board_name = Column(VARCHAR(32), comment='板块名称')
    price = Column(DECIMAL(9, 4), comment='价格')
    total_sec_shares = Column(DECIMAL(26, 4), comment='信用账户持股合计')
    total_shares = Column(DECIMAL(26, 4), comment='总股本')
    sec_shares_ratio = Column(DECIMAL(26, 6), comment='占总股本比例')
    tra_shares = Column(DECIMAL(26, 4), comment='流通股本')
    tra_shares_ratio = Column(DECIMAL(26, 6), comment='占总股本比例')
    match_qty_avg = Column(BigInteger, comment='日均成交量(近一个月)')
    force_trade_out_days = Column(DECIMAL(26, 6), comment='理论平仓天数')
    sec_shares_mkt_val = Column(DECIMAL(26, 4), comment='信用账户持仓市值')
    sec_shares_mkt_val_change = Column(DECIMAL(9, 4), comment='信用账户持仓市值较上日增减')
    total_mkt_val = Column(DECIMAL(26, 4), comment='证券总市值')
    sec_shares_mkt_val_ratio = Column(DECIMAL(9, 4), comment='占信用账户总市值比例')
    is_collateral = Column(CHAR(1), comment='是否为担保物')
    value_rate = Column(DECIMAL(9, 4), comment='折算率')
    risk_score = Column(DECIMAL(9, 4), comment='风险评分')
    board_code = Column(VARCHAR(32), comment='板块代码')
    secu_cate_code = Column(CHAR(1), comment='证券类别（S：股票，F：基金，B：债券）')


class SecConfig(Base):
    __tablename__ = 'sec_config'
    __table_args__ = {'comment': '配置信息表'}

    key = Column(VARCHAR(100), primary_key=True)
    json_data = Column(JSON)
    is_allow_edit = Column(TINYINT, server_default=text("'0'"))


class SecContract(Base):
    __tablename__ = 'sec_contract'
    __table_args__ = {'comment': '两融合约表'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    sno = Column(VARCHAR(50), primary_key=True, nullable=False, comment='合约编号')
    data_label = Column(VARCHAR(4), primary_key=True, nullable=False, comment='数据标签')
    credit_direct = Column(CHAR(1), comment='融资方向（0：融资，1：融券）')
    open_date = Column(Date, primary_key=True, nullable=False, comment='合约开仓日期')
    close_date = Column(Date, comment='合约到期日期')
    countdown_day = Column(Integer, comment='剩余到期天数')
    unrepaid_amt = Column(DECIMAL(26, 4), comment='未还融资本金')
    unrepaid_mkt = Column(DECIMAL(26, 4), comment='未还证券市值')
    unrepaid_qtty = Column(DECIMAL(26, 0), comment='未还证券数量')
    unrepaid_other = Column(DECIMAL(26, 4), comment='未还其他费用合计')
    clear_amt = Column(DECIMAL(26, 4), comment='清算金额')
    creditrepay = Column(DECIMAL(26, 4), comment='t日之前归还金额')
    creditrepayunfrz = Column(DECIMAL(26, 4), comment='当日开仓当日直接还款金额')
    fee = Column(DECIMAL(26, 4), comment='融资利息或融券费用')
    feeunfrz = Column(DECIMAL(26, 4), comment='白天实时偿还费用')
    overduefee = Column(DECIMAL(26, 4), comment='累计融资逾期利息或融券逾期费用')
    overduefeeunfrz = Column(DECIMAL(26, 4), comment='当日融资逾期利息或融券逾期费用')
    punidebts = Column(DECIMAL(26, 4), comment='逾期本金罚息')
    punidebtsunfrz = Column(DECIMAL(26, 4), comment='当日逾期本金罚息')
    punifee = Column(DECIMAL(26, 4), comment='逾期息费罚息')
    punifeeunfrz = Column(DECIMAL(26, 4), comment='当日逾期息费罚息')
    unrepay_fee = Column(DECIMAL(26, 4), comment='未还利息')
    stk_code = Column(CHAR(8), comment='证券代码')
    match_share = Column(DECIMAL(26, 0), comment='成交数量')
    match_amt = Column(DECIMAL(26, 4), comment='成交金额')
    ext_flag = Column(CHAR(1), comment='是否展期')


class SecContractReal(Base):
    __tablename__ = 'sec_contract_real'
    __table_args__ = {'comment': '合约变动表(实时)'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    sno = Column(VARCHAR(50), primary_key=True, nullable=False, comment='合约编号')
    credit_direct = Column(Integer, comment='融资方向(0融资1融券)')
    open_date = Column(Date, primary_key=True, nullable=False, comment='合约开仓日期')
    close_date = Column(Date, comment='合约到期日期')
    countdown_day = Column(Integer, comment='剩余到期时间')
    clear_amt = Column(DECIMAL(26, 4), comment='清算金额')
    match_qty = Column(BigInteger, comment='成交数量')
    match_amt = Column(DECIMAL(26, 4), comment='成交金额')
    match_amt_repay = Column(DECIMAL(26, 4), comment='已还成交金额')
    creditrepay = Column(DECIMAL(26, 4), comment='t日之前归还金额(融资总负债/融券总负债)')
    creditrepayunfrz = Column(DECIMAL(26, 4), comment='t日归还金额')
    stkrepay = Column(BigInteger, comment='t日之前归还数量')
    stkrepayunfrz = Column(BigInteger, comment='t实时归还数量')
    fee = Column(DECIMAL(26, 4), comment='融资利息或融券费用')
    feeunfrz = Column(DECIMAL(26, 4), comment='当日息费偿还总额')
    overduefee = Column(DECIMAL(26, 4), comment='融资逾期利息或融券逾期费用')
    overduefeeunfrz = Column(DECIMAL(26, 4), comment='融资逾期利息或融券逾期费用')
    punidebts = Column(DECIMAL(26, 4), comment='逾期本金罚息')
    punidebtsunfrz = Column(DECIMAL(26, 4), comment='逾期本金罚息')
    punifee = Column(DECIMAL(26, 4), comment='逾期息费罚息')
    punifeeunfrz = Column(DECIMAL(26, 4), comment='逾期息费罚息')
    punirights = Column(DECIMAL(26, 4), comment='逾期权益罚息')
    punirightsunfrz = Column(DECIMAL(26, 4), comment='逾期权益罚息')
    rights = Column(DECIMAL(26, 4), comment='在途权益金额')
    stk_code = Column(VARCHAR(32), comment='证券代码')
    ext_num = Column(Integer, comment='已展期次数')
    overduerights = Column(DECIMAL(26, 4), comment='应付权益金额')
    rights_repay = Column(DECIMAL(26, 4), comment='己偿还权益')
    rightsunfrz = Column(DECIMAL(26, 4), comment='实时偿还')
    overduerightsunfrz = Column(DECIMAL(26, 4), comment='融券逾期权益，对扣收不到的融券权益转逾期权益息费')
    rightsqty = Column(BigInteger, comment='在途权益数量')
    overduerightsqty = Column(BigInteger, comment='应付权益数量')
    rightsqty_repay = Column(BigInteger, comment='己偿还权益数量')
    rightsqtyunfrz = Column(BigInteger, comment='实时偿还')
    overduerightsqtyunfrz = Column(BigInteger, comment='实时偿还逾期权益数量')
    serverid = Column(VARCHAR(32))
    updated_at = Column(DateTime, comment='更新时间')
    data_label = Column(CHAR(1), comment='数据标签，0：redis,1:XCB')


class SecCreditMargin(Base):
    __tablename__ = 'sec_credit_margin'
    __table_args__ = {'comment': '信用保证金比例参数表'}

    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    trade_mrkt = Column(VARCHAR(4), primary_key=True, nullable=False, comment='交易市场')
    fi_guar_rate = Column(DECIMAL(26, 8), comment='融资保证金比例')
    sl_guar_rate = Column(DECIMAL(26, 8), comment='客户初始融券保证金比例')
    mkt_fi_guar_rate = Column(DECIMAL(26, 8), comment='市场-融资保证金比例（%）')
    mkt_sl_guar_rate = Column(DECIMAL(26, 8), comment='市场-融券保证金比例（%）')
    value_factorfund = Column(DECIMAL(26, 8), comment='融资市场估值因子')
    value_factorstk = Column(DECIMAL(26, 8), comment='融券市场估值因子')


class SecCreditassetdebtsReal(Base):
    __tablename__ = 'sec_creditassetdebts_real'
    __table_args__ = {'comment': '客户资产负债变动(实时)'}

    fund_id = Column(VARCHAR(100), primary_key=True, comment='资金账号')
    cust_id = Column(VARCHAR(100), comment='客户ID')
    cap_bal = Column(DECIMAL(26, 4), comment='现金')
    total_asset = Column(DECIMAL(26, 4), comment='信用总资产')
    avl_amt = Column(DECIMAL(19, 2), comment='可用资金')
    sell_frz_amt = Column(DECIMAL(19, 2), comment='融券卖出现金')
    fundbal = Column(DECIMAL(19, 2), comment='到帐余额')
    fundbuysale = Column(DECIMAL(19, 2), comment='买卖差额')
    funduncomebuy = Column(DECIMAL(19, 2), comment='在途买入')
    funduncomesale = Column(DECIMAL(19, 2), comment='在途卖出')
    funddebtsfee = Column(DECIMAL(26, 4), comment='客户级融资费用')
    stkdebtsfee = Column(DECIMAL(26, 4), comment='客户级融券费用')
    funddebtsbal = Column(DECIMAL(19, 2), comment='融资授信额度')
    stkdebtsbal = Column(DECIMAL(19, 2), comment='融券授信额度')
    closeamt = Column(DECIMAL(19, 2), comment='需平仓金额')
    closestatus = Column(CHAR(1), comment='追加平仓状态')
    tradeflag = Column(VARCHAR(128), comment='信用交易属性设置')
    total_debts = Column(DECIMAL(26, 4), comment='信用总负债')
    realcreditstatus = Column(CHAR(10, 'utf8mb4_general_ci'), comment='实时信用状态')
    updated_at = Column(DateTime)
    serverid = Column(VARCHAR(32), comment='服务器编码')


class SecCreditholdscale(Base):
    __tablename__ = 'sec_creditholdscale'
    __table_args__ = {'comment': '信用账户持仓集中度'}

    serverid = Column(Integer, primary_key=True, nullable=False, comment='服务器编号')
    sno = Column(Integer, primary_key=True, nullable=False, comment='序号')
    keepratemin = Column(DECIMAL(19, 4), comment='维持担保比例下限')
    keepratemax = Column(DECIMAL(19, 4), comment='维持担保比例上限')
    holdscale = Column(DECIMAL(26, 4), comment='持仓集中度')
    ctrlflag = Column(CHAR(1), comment='控制标志  0:交易集中度 1:展期集中度')


class SecCreditmixparam(Base):
    __tablename__ = 'sec_creditmixparam'
    __table_args__ = {'comment': '信用参数表'}

    serverid = Column(Integer, primary_key=True, nullable=False, comment='服务器编号')
    paramkinds = Column(Integer, primary_key=True, nullable=False, comment='参数类型')
    paramname = Column(VARCHAR(32), comment='参数名称')
    datalabel = Column(Integer, comment='数据标签')
    amt = Column(DECIMAL(19, 2), comment='净资本')


class SecCustIndicationReal(Base):
    __tablename__ = 'sec_cust_indication_real'
    __table_args__ = {'comment': '客户指标信息表'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账户')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    stock_weigthte_ave = Column(DECIMAL(26, 4), comment='持证券加权平均分')
    market_pledge_ratio = Column(DECIMAL(26, 4), comment='全市场质押率')
    main_guarantee_ratio = Column(DECIMAL(26, 4), comment='维持担保比例')
    net_shorts = Column(DECIMAL(26, 4), comment='净空头占比，净空头/净资产')
    debt_assets_ratio = Column(DECIMAL(26, 4), comment='资产负债率')
    concentration = Column(DECIMAL(20, 4), comment='最大集中度')
    new_rank = Column(VARCHAR(100), comment='新意评级(资信评级)')
    annualized_returns = Column(DECIMAL(26, 4), comment='年化收益')
    sharp_ratio = Column(DECIMAL(26, 4), comment='Sharpe比率')
    alpha = Column(DECIMAL(26, 4), comment='Alpha')
    beta = Column(DECIMAL(26, 4), comment='Beta')
    annualized_volatility = Column(DECIMAL(26, 4), comment='年化波动')
    maximum_drawdown = Column(DECIMAL(26, 4), comment='最大回撤')
    var = Column(DECIMAL(26, 4), comment='VAR 95%')
    interest_income = Column(DECIMAL(26, 4), comment='利息收入(近一年)')
    sec_balance = Column(DECIMAL(26, 4), comment='当前两融余额排名百分比')
    total_asset_size = Column(DECIMAL(26, 4), comment='总资产规模')
    sortino = Column(DECIMAL(26, 4), comment='索提诺比率')
    info_rate = Column(DECIMAL(26, 4), comment='信息比率')
    second_max_drawdown = Column(DECIMAL(26, 4), comment='第二大回撤')
    third_max_drawdown = Column(DECIMAL(26, 4), comment='第三大回撤')
    top_three_concentration = Column(JSON, comment='前三大集中度')
    ps_warning_list = Column(String(1, 'utf8mb4_general_ci'))


class SecCustinfo(Base):
    __tablename__ = 'sec_custinfo'
    __table_args__ = {'comment': '客户信息'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号（信用）')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    cust_id = Column(VARCHAR(19), primary_key=True, nullable=False, server_default=text("'1'"), comment='客户id')
    cust_name = Column(VARCHAR(100), comment='客户名称')
    rela_asset_acct = Column(VARCHAR(16), comment='资金账号（普通）')
    cust_code_arr_cd = Column(Integer, comment='客户类别标签（个人/机构）')
    prod_com_code = Column(VARCHAR(64))
    prod_com_name = Column(VARCHAR(64))
    pro_investor_type_cd = Column(VARCHAR(80), comment='专业投资者分类')
    pro_investor_flag = Column(CHAR(1), comment='是否专业投资者')
    credit_level = Column(VARCHAR(16), comment='当前资信等级')
    credit_test_score = Column(DECIMAL(26, 4), comment='当前资信分数')
    credit_date = Column(Date, comment='评级日期')
    crd_acc_assst = Column(DECIMAL(26, 4), comment='信用账户资产(总资产)')
    ord_acc_assst = Column(DECIMAL(26, 4), comment='普通账户资产(总资产)')
    asset_data_label = Column(VARCHAR(4), comment='数据标签，区分来自宏源(hy)还是申万(sw)的数据')
    cap_bal = Column(DECIMAL(26, 4), comment='资金余额')
    avl_amt = Column(DECIMAL(26, 4), comment='可用资金余额')
    frz_amt = Column(DECIMAL(26, 4), comment='冻结总余额')
    unfrz_amt = Column(DECIMAL(26, 4), comment='解冻总金额')
    trd_frz_amt = Column(DECIMAL(26, 4), comment='交易冻结金额')
    sell_frz_amt = Column(DECIMAL(26, 4), comment='信用卖出冻结金额')
    buy_frz_amt = Column(DECIMAL(26, 4), comment='买入冻结金额')
    uncome_amt = Column(DECIMAL(26, 4), comment='在途资金余额')
    market_val = Column(DECIMAL(26, 4), comment='资产市值')
    tot_asset = Column(DECIMAL(26, 4), comment='总资产')
    tot_debts = Column(DECIMAL(26, 4), comment='总负债')
    net_asset = Column(DECIMAL(26, 4), comment='净资产')
    guar_mkt_val = Column(DECIMAL(26, 4), comment='担保品市值')
    fin_avl_amt = Column(DECIMAL(26, 4), comment='融资余额')
    secu_avl_amt = Column(DECIMAL(26, 4), comment='融券余额')
    fin_debt_tot_amt = Column(DECIMAL(26, 4), comment='融资总负债')
    secu_debt_tot_amt = Column(DECIMAL(26, 4), comment='融券总负债')
    day_interest = Column(DECIMAL(26, 4), comment='当日毛利息')
    year_interest = Column(DECIMAL(26, 4), comment='近一年利息收入')
    day_commis = Column(DECIMAL(26, 4), comment='当日毛佣金')
    year_profit = Column(DECIMAL(26, 4), comment='年内盈利（账户分析）')
    acct_data_label = Column(VARCHAR(4), comment='数据标签')
    belong_org_id = Column(CHAR(4), comment='营业部代码')
    tot_lmt_amt = Column(DECIMAL(26, 4), comment='总额度')
    fin_lmt_amt = Column(DECIMAL(26, 4), comment='融资额度')
    secu_lmt_amt = Column(DECIMAL(26, 4), comment='融券额度')
    last_credit_status = Column(VARCHAR(6), comment='上日信用状态（数据字典待提供）')
    credit_status = Column(VARCHAR(6), comment='信用状态（数据字典待提供）')
    last_notice_status = Column(VARCHAR(6), comment='上日追缴状态（数据字典待提供）')
    notice_status = Column(VARCHAR(6), comment='追缴状态（数据字典待提供）')
    is_vip = Column(CHAR(1), comment='vip标识（数据字典待提供）')
    noext_flag = Column(VARCHAR(200), comment='禁止外围展期标记')
    halfyear_close_pos_num = Column(Integer, comment='180日内平仓次数（资金账户级别）')
    fund_initrate = Column(DECIMAL(12, 8), index=True, comment='初始线')
    clear_rate = Column(DECIMAL(12, 8), index=True, comment='清偿平仓线系统目前设置为1(1%)维持担保比例低于1%直接进入清偿平仓程序。')
    fund_alarmrate = Column(DECIMAL(12, 8), index=True, comment='警戒线')
    fund_forcerate = Column(DECIMAL(12, 8), index=True, comment='最低担保线')
    fund_control = Column(DECIMAL(12, 8), index=True, comment='提款保证金比例')
    guar_data_label = Column(VARCHAR(4), comment='数据标签，区分来自宏源(hy)还是申万(sw)的数据')
    curr_cd = Column(CHAR(1), comment='币种')
    secu_mrkt_val = Column(DECIMAL(26, 4), comment='担保品市值')
    fi_total_liab = Column(DECIMAL(26, 4), comment='融资负债')
    sl_total_liab = Column(DECIMAL(26, 4), comment='融券负债市值')
    keeprate = Column(DECIMAL(26, 4), comment='维持担保比例')
    fi_bal = Column(DECIMAL(26, 4), comment='融资余额(不含费用利息)')
    cust_margin = Column(DECIMAL(26, 4), comment='客户保证金')
    data_label = Column(VARCHAR(4), comment='0：申万宏源证券\\r\\n1：西部证券标识')


class SecCuststkholdscale(Base):
    __tablename__ = 'sec_custstkholdscale'
    __table_args__ = {'comment': '客户集中度'}

    serverid = Column(Integer, primary_key=True, nullable=False, comment='服务器编号')
    sno = Column(Integer, primary_key=True, nullable=False, comment='序号')
    orgid = Column(CHAR(4), comment='机构编码')
    fundid = Column(BigInteger, comment='资金账号')
    market = Column(CHAR(1), comment='市场代码')
    stkcode = Column(CHAR(8), comment='证券代码')
    keepratemin = Column(DECIMAL(19, 4), comment='维持担保比例下限')
    keepratemax = Column(DECIMAL(19, 4), comment='维持担保比例上限')
    holdscale = Column(DECIMAL(12, 8), comment='持仓集中度')


class SecExceptionalStkAm(Base):
    __tablename__ = 'sec_exceptional_stk_am'
    __table_args__ = {'comment': '异常证券处理配置表（exceptionalstk）'}

    serverid = Column(BigInteger, primary_key=True, nullable=False, comment='服务器编号')
    market = Column(VARCHAR(4), primary_key=True, nullable=False, comment='市场代码')
    stkcode = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    excpttype = Column(VARCHAR(4), primary_key=True, nullable=False, comment='异常原因')
    dealway = Column(VARCHAR(4), primary_key=True, nullable=False, comment='异常处理方式')
    operdate = Column(Date, comment='设置日期')
    dealdate = Column(Date, comment='生效起始日')
    enddate = Column(Date, comment='生效截止日')
    mktvaluerate = Column(DECIMAL(12, 8), comment='市值折算率')
    remark = Column(VARCHAR(32), comment='备注')


class SecForceHistory(Base):
    __tablename__ = 'sec_force_history'
    __table_args__ = {'comment': '两融平仓明细表'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    cust_id = Column(VARCHAR(20), comment='客户号')
    cust_name = Column(VARCHAR(200), comment='客户名称')
    biz_name = Column(VARCHAR(20), comment='业务名称（融资融券）')
    biz_subj = Column(VARCHAR(20), comment='业务主体（北京/上海）')
    org_code = Column(VARCHAR(200), comment='营业部名称')
    org_name = Column(VARCHAR(100), comment='营业部代码')
    cert_id = Column(VARCHAR(50), comment='证件号')
    amt = Column(DECIMAL(22, 2), comment='平仓金额')
    reason = Column(VARCHAR(100), comment='平仓原因(空值)')
    risk_result = Column(VARCHAR(50), comment='风险结果（强制平仓/强制还款）')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='强平日期')
    dzszq = Column(DECIMAL(22, 2), comment='待追索债权（融资负债+融券负债）')


class SecIndexStat(Base):
    __tablename__ = 'sec_index_stat'
    __table_args__ = {'comment': '指标统计表'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资产账户')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    defer_times = Column(Integer, comment='展期次数')
    force_times = Column(Integer, comment='平仓次数')
    overdue_times = Column(Integer, comment='逾期次数')
    defer_amt = Column(DECIMAL(26, 4), comment='展期金额')
    force_amt = Column(DECIMAL(26, 4), comment='平仓金额')
    overdue_amt = Column(DECIMAL(26, 4), comment='逾期金额')
    defer_contrcount = Column(Integer, comment='展期合约数')
    force_contrcount = Column(Integer, comment='平仓合约数')
    overdue_contrcount = Column(Integer, comment='逾期合约数')
    frequency = Column(Integer, comment='频度(90,180,360)')


class SecKeeprateReal(Base):
    __tablename__ = 'sec_keeprate_real'
    __table_args__ = {'comment': '实时维保比例表'}

    fund_id = Column(VARCHAR(100), primary_key=True)
    keeprate = Column(DECIMAL(26, 4), nullable=False)
    updated_at = Column(DateTime)


class SecLogbanktranReal(Base):
    __tablename__ = 'sec_logbanktran_real'
    __table_args__ = {'comment': '银证转账(实时)'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    serverid = Column(BigInteger, comment='机器编码')
    sysdate = Column(Date, comment='操作的交易日期')
    operdate = Column(Date, comment='发生日期')
    opertime = Column(DateTime, comment='发生时间')
    sno = Column(VARCHAR(32), primary_key=True, nullable=False, comment='流水号')
    moneytype = Column(CHAR(1), comment='货币代码')
    banktranid = Column(CHAR(1, 'utf8mb4_general_ci'), primary_key=True, nullable=False, comment="业务类型，'1'--银行转证券'2'--证券转银行'3'--查证券余额'4'--查银行余额'5'--冲银行转证券'6'--冲证券转银行'7'--开户")
    fundeffect = Column(DECIMAL(19, 2), comment='转帐发生金额')
    fundbal = Column(DECIMAL(19, 2), comment='发生后余额')
    status = Column(CHAR(1), comment='" 交易状态\\n\t\'0\',\'未报\'\\n\t\'1\',\'已报\'\\n\t\'2\',\'成功\'\\n\t\'3\',\'失败\'\\n\t\'4\',\'超时\'\\n\t\'5\',\'待冲正\'\\n\t\'6\',\'已冲正\'\\n\t\'7\',\'调整为成功\'\\n\t\'8\',\'调整为失败\'\\n\t\'9\',\'单边销户\'"')
    updated_at = Column(DateTime)


class SecMapInfo(Base):
    __tablename__ = 'sec_map_info'
    __table_args__ = {'comment': '营业部地图数据'}

    id = Column(VARCHAR(64), primary_key=True, comment='主键')
    branch_name = Column(VARCHAR(50), nullable=False, comment='营业部名称')
    branch_code = Column(VARCHAR(10), nullable=False, comment='营业部代码')
    order_num = Column(VARCHAR(10), comment='排序值')
    is_display = Column(CHAR(1), comment='是否显示,0:显示，1:不显示')
    area_id = Column(VARCHAR(64), comment='所属区域编号')
    address = Column(VARCHAR(500), comment='营业部地址')
    traffic_info = Column(VARCHAR(1000), comment='营业部交通信息')
    branch_phone = Column(VARCHAR(40), comment='营业部电话')
    branch_info = Column(TEXT, comment='营业部介绍')
    lat = Column(VARCHAR(64), comment='经度')
    lnt = Column(VARCHAR(64), comment='纬度')
    companyno = Column(VARCHAR(20), comment='分公司ID')
    branch_type = Column(CHAR(1), comment='营业部类型 1：原申万 2：原宏源')
    create_by = Column(VARCHAR(64))
    create_date = Column(Date)
    update_by = Column(VARCHAR(64))
    update_date = Column(Date)
    remarks = Column(VARCHAR(255))
    del_flag = Column(CHAR(1))
    area_id1 = Column(VARCHAR(64))
    area_id2 = Column(VARCHAR(64))
    company_type = Column(VARCHAR(64))
    parent_branch_code = Column(VARCHAR(64))


class SecMargPledInfo(Base):
    __tablename__ = 'sec_marg_pled_info'
    __table_args__ = {'comment': '产品折算率与保证金比例 表'}

    serverid = Column(Integer, primary_key=True, nullable=False, comment=' 服务器编号')
    market = Column(CHAR(1), primary_key=True, nullable=False, comment=' 市场代码')
    stk_code = Column(VARCHAR(8), primary_key=True, nullable=False, comment=' 证券代码')
    stkname = Column(VARCHAR(8), comment=' 证券简称')
    mkt_pledgerate = Column(DECIMAL(12, 8), comment=' 折算率-交易所')
    mkt_upddate = Column(Date, comment=' 交易所折算率最后更新日期')
    mkt_gage_flag = Column(CHAR(1), comment=' 是否可作为融资融券可冲抵保证金证券-交易所')
    pledgerate = Column(DECIMAL(12, 8), comment='折算率 ')
    upddate = Column(Date, comment=' 折算率最后更新日期')
    gage_flag = Column(CHAR(1), comment=' 是否可作为融资融券可冲抵保证金证券-券商')
    creditfundctrl = Column(CHAR(1), comment=' 融资状态')
    creditstkctrl = Column(CHAR(1), comment=' 融券状态')
    fundcalkind = Column(CHAR(1), comment=' 融资保证金比例计算方式')
    marginratefund = Column(DECIMAL(12, 8), comment=' 融资保证金比例')
    stkcalkind = Column(CHAR(1), comment=' 融券保证金比例计算方式')
    marginratestk = Column(DECIMAL(12, 8), comment=' 融券保证金比例')
    stkpricekind = Column(CHAR(1), comment=' 融券卖出价格控制方式')
    fundlimit = Column(CHAR(1), comment=' 融资受限')
    stklimit = Column(CHAR(1), comment=' 融券受限')
    mkt_creditfundctrl = Column(CHAR(1), comment=' 融资状态-交易所')
    mkt_creditstkctrl = Column(CHAR(1), comment=' 融券状态-交易所')
    mkt_stkpricekind = Column(CHAR(1), comment=' 融券卖出价格控制方式-交易所')


class SecMatchReal(Base):
    __tablename__ = 'sec_match_real'
    __table_args__ = (
        Index('sec_match_real_stkcode_test', 'creditflag', 'matchtype', 'stkcode'),
        {'comment': '客户成交记录变动 实时表'}
    )

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    serverid = Column(BigInteger, comment='机器编码')
    custid = Column(BigInteger, comment='客户ID')
    matchsno = Column(VARCHAR(100), comment='合同序号')
    trddate = Column(Date, comment='交易时间')
    market = Column(CHAR(1), primary_key=True, nullable=False, comment='市场')
    stkcode = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    creditflag = Column(CHAR(1), comment='交易类型')
    matchamt = Column(DECIMAL(19, 2), comment='成交金额')
    matchtime = Column(Integer)
    matchcode = Column(VARCHAR(20), primary_key=True, nullable=False, comment='成交编号')
    matchprice = Column(DECIMAL(26, 4), comment='成交价格')
    matchqty = Column(Integer, comment='成交数量')
    matchtype = Column(CHAR(1), comment='成交类型')
    updated_at = Column(DateTime)
    data_label = Column(CHAR(1), comment='数据来源，0：redis， 1：XCB')


class SecPledgeContract(Base):
    __tablename__ = 'sec_pledge_contract'
    __table_args__ = {'comment': '质押合约信息表'}

    sno = Column(VARCHAR(100), primary_key=True, nullable=False, comment='合约序号')
    market = Column(VARCHAR(4), comment='交易市场')
    prod_id = Column(VARCHAR(80), comment='产品编号')
    amt = Column(DECIMAL(26, 4), comment='合约金额')
    repaid_prin_amt = Column(DECIMAL(26, 4), comment='已还本金金额')
    lender_cls = Column(VARCHAR(4), comment='融出方类别')
    in_cust_char = Column(VARCHAR(4), comment='融入方客户性质')
    in_cust_name = Column(VARCHAR(100), comment='融入方客户名称')
    fund_id = Column(VARCHAR(100), comment='融入方资金账号')
    in_belong_org_id = Column(VARCHAR(100), comment='融入方营业部编号')
    out_cust_char = Column(VARCHAR(4), comment='融出方客户性质')
    out_cust_name = Column(VARCHAR(100), comment='融出方客户名称')
    data_label = Column(VARCHAR(4), primary_key=True, nullable=False, comment='数据标签，区分来自宏源(HY)还是申万(SW)的数据')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='数据日期')


class SecPledgecustinfo(Base):
    __tablename__ = 'sec_pledgecustinfo'
    __table_args__ = {'comment': '质押客户信息表'}

    cust_id = Column(VARCHAR(32), primary_key=True, nullable=False, comment='客户编号')
    cust_name = Column(VARCHAR(100), comment='客户姓名')
    cert_type_cd = Column(VARCHAR(4), comment='证件类型代码')
    cert_id = Column(VARCHAR(32), primary_key=True, nullable=False, comment='证件号码')
    cust_code_arr_cd = Column(VARCHAR(32), comment='客户性质代码')
    datalabel = Column(VARCHAR(4), comment='数据标签')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='数据日期')


class SecRightsadjustassetReal(Base):
    __tablename__ = 'sec_rightsadjustasset_real'
    __table_args__ = {'comment': '权益资产调整表 实时表'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号')
    serverid = Column(BigInteger, comment='服务器编号')
    custid = Column(BigInteger, comment='客户代码')
    orgid = Column(CHAR(4), comment='机构编码')
    moneytype = Column(CHAR(1), comment='货币代码')
    market = Column(CHAR(1), primary_key=True, nullable=False, comment='交易市场')
    secuid = Column(CHAR(10), comment='股东代码')
    stkcode = Column(CHAR(8), primary_key=True, nullable=False, comment='权益证券代码')
    relastkcode = Column(CHAR(8), comment='正股证券代码')
    rightskind = Column(CHAR(1), primary_key=True, nullable=False, comment='权益类型')
    adjustflag = Column(CHAR(1), comment='调整方式')
    adjustqty = Column(Integer, comment='股份调整数量')
    adjustprice = Column(DECIMAL(19, 2))
    adjustamt = Column(DECIMAL(19, 2), comment='调整金额')
    remark = Column(VARCHAR(64), comment='备注')
    updated_at = Column(DateTime)


class SecSharePo(Base):
    __tablename__ = 'sec_share_pos'
    __table_args__ = {'comment': '股东账户持仓表'}

    secu_acct = Column(VARCHAR(100), primary_key=True, nullable=False, server_default=text("'1111'"), comment='股东账号')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    stk_code = Column(VARCHAR(19), primary_key=True, nullable=False, comment='证券代码')
    share_bal = Column(BigInteger, comment='持仓证券数量')
    lim_amt = Column(BigInteger, comment='限售股份数量')
    is_major_holder = Column(CHAR(1), comment='5%以上大股东标志（数据字典待提供）')
    is_lim_holder = Column(CHAR(1), comment='解除限售流通股东标志（数据字典待提供）')


class SecSpstkposicontractReal(Base):
    __tablename__ = 'sec_spstkposicontract_real'
    __table_args__ = {'comment': '实时专项券源合约表'}

    serverid = Column(VARCHAR(32), primary_key=True, nullable=False, comment='机器编码')
    sysdate = Column(Date, primary_key=True, nullable=False, comment='合约日期')
    sno = Column(VARCHAR(50), primary_key=True, nullable=False, comment='合约编号')
    reqdate = Column(Date, comment='申请日期')
    reqsno = Column(VARCHAR(50), comment='申请编号')
    sourcetype = Column(CHAR(1), comment='券源类型Erqqylx  0：转融通券源 1：自营券源')
    positionid = Column(BigInteger, comment='头寸编号')
    market = Column(CHAR(1), comment='交易市场 0.深交所  1.上交所')
    stk_code = Column(VARCHAR(8), comment='证券代码')
    stk_name = Column(VARCHAR(128), comment='证券名称')
    stktotal = Column(BigInteger, comment='头寸数量')
    stkused = Column(BigInteger, comment='已使用数量')
    stkavl = Column(BigInteger, comment='可用数量')
    unlockqty = Column(BigInteger, comment='已解锁数量')
    rightsqty = Column(BigInteger, comment='权益数量')
    unpaidrightsqty = Column(BigInteger, comment='未付权益数量')
    interatemodel = Column(CHAR(1), comment='计息模式  Ezxjxms--ZQFIS-972, gaoq, 20181107 落地客户的计息模式，计息以申请时刻为准')
    fullrate = Column(DECIMAL(12, 8), comment='全额占用费率')
    unuserate = Column(DECIMAL(12, 8), comment='空闲占用费率')
    userate = Column(DECIMAL(12, 8), comment='使用费率')
    orgid = Column(CHAR(4), comment='机构名称')
    fund_id = Column(VARCHAR(100), comment='资金账号')
    fund_name = Column(VARCHAR(16), comment='客户姓名')
    contractno = Column(BigInteger, comment='证金合约编号，转融通券源为证金合约编号 自营券源按照系统日期 *1000000+合约编号生成')
    enddate = Column(Date, comment='到期日期')
    assigndate = Column(Date, comment='分派日期')
    intrdate = Column(Date, comment='计息日期')
    posistkprice = Column(DECIMAL(9, 3), comment='计息价格  转融通券源与证金收盘价一致，自有券源为分派日收盘价')
    fee = Column(DECIMAL(19, 2), comment='累计息费  --该券源合约产生的全额占用费、使用费、空闲占用费')
    regstkavl = Column(BigInteger, comment='登记日未开仓数量  ZQFIS-1374, gaoq, 20191130')
    unuserights = Column(DECIMAL(19, 2), comment='累积未开仓部分权益金额， 未开仓部分权益金额汇总')
    closedate = Column(Date, comment='了结日期')
    status = Column(CHAR(1), comment='合约状态 Hyljbz 0：未了结 1：已了结')
    remark = Column(VARCHAR(128), comment='备注')
    deferqty = Column(BigInteger, comment='在途展期数量')
    overduedeferqty = Column(BigInteger, comment='展期数量')
    defersysdate = Column(Date, comment='展期新合约日期')
    defersno = Column(VARCHAR(50), comment='展期新合约编号')
    prereqsno = Column(BigInteger, comment='券源预约申请编号')
    preparedate = Column(Date, comment='筹券日期 ZQFIS-1524, caosy, 20200811')
    lenderid = Column(VARCHAR(50), comment='出借人ID')
    lendername = Column(VARCHAR(64), comment='出借人名称')
    updated_at = Column(DateTime, comment='数据更新时间')


class SecStkForbidext(Base):
    __tablename__ = 'sec_stk_forbidext'
    __table_args__ = {'comment': '限制展期的证券'}

    stk_code = Column(CHAR(8), primary_key=True)
    update_at = Column(VARCHAR(100))
    update_by = Column(VARCHAR(50))


class SecStkassetReal(Base):
    __tablename__ = 'sec_stkasset_real'
    __table_args__ = {'comment': '客户股份变动（实时）'}

    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号ID')
    market = Column(CHAR(1), comment='市场')
    stk_code = Column(CHAR(8), primary_key=True, nullable=False, comment='持仓证券代码')
    serverid = Column(BigInteger, comment='服务器编号')
    org_id = Column(CHAR(4), comment='机构编码')
    secuid = Column(CHAR(10), comment='股东代码')
    stkavl = Column(BigInteger, comment='股份可用')
    creditstkbal = Column(BigInteger, comment='融资买入股份余额')
    creditstkavl = Column(BigInteger, comment='融资买入股份可用')
    stkremain = Column(Integer, comment='客户余券')
    stkbuy = Column(BigInteger, comment='股份买入解冻')
    stksale = Column(BigInteger, comment='股份卖出冻结')
    stkfrz = Column(BigInteger, comment='股份冻结')
    stkcorpremain = Column(Integer, comment='融券专户余券数量')
    stkqty = Column(Integer, comment='持仓证券数量')
    mktval = Column(DECIMAL(26, 4), comment='持仓证券市值')
    stkbal = Column(BigInteger, comment='股份余额')
    stkbuysale = Column(BigInteger, comment='股份实时买卖差额')
    stkuncomebuy = Column(BigInteger, comment='在途股份买入解冻')
    stkuncomesale = Column(BigInteger, comment='在途股份卖出冻结')
    updated_at = Column(DateTime)
    data_label = Column(CHAR(1), comment='数据来源，0：redis， 1：XCB')


class SecStkpositionstockReal(Base):
    __tablename__ = 'sec_stkpositionstock_real'
    __table_args__ = {'comment': '实时-融券头寸证券明细表'}

    serverid = Column(VARCHAR(32), primary_key=True, nullable=False, comment='机器编码')
    positionid = Column(BigInteger, primary_key=True, nullable=False, comment='头寸编号')
    market = Column(CHAR(1), primary_key=True, nullable=False, comment='交易市场')
    stk_code = Column(VARCHAR(8), primary_key=True, nullable=False, comment='证券代码')
    stktotal = Column(BigInteger, comment='头寸数量（额度）')
    stklast = Column(BigInteger, comment='昨日数量')
    stkavl = Column(BigInteger, comment='头寸实时可用数量 --算可用时，扣除待解冻数量，保证当天到期的券源当天无法开仓')
    stkreserve = Column(BigInteger, comment='预留证券')
    lockqty = Column(BigInteger, comment='锁定数量 ZQFIS-972, gaoq, 20181121 专项券源第二天要到期的时候冻结数量，解锁后释放')
    stkused = Column(BigInteger, comment='头寸已使用数量')
    stkusedreal = Column(BigInteger, comment='头寸实时使用数量')
    stkrepayreal = Column(BigInteger, comment='头寸实时还数量')
    fullrate = Column(DECIMAL(12, 8), comment='全额占用费率')
    unuserate = Column(DECIMAL(12, 8), comment='闲置费率')
    userate = Column(DECIMAL(12, 8), comment='使用费率')
    intrrate = Column(DECIMAL(12, 8), comment='开仓费率')
    punirate = Column(DECIMAL(12, 8), comment='罚息费率')
    intrkind = Column(CHAR(1), comment='是否要计算央行利率 Bllfs 0 不计 1 计  ')
    flowin = Column(CHAR(1), comment='吸收特性')
    flowback = Column(CHAR(1), comment='回收特性')
    trdflag = Column(VARCHAR(128), comment='交易属性 Etcjysx（0|到期开仓控制，1|禁止合约展期）')
    begindate = Column(Date, comment='生效开始日期')
    enddate = Column(Date, comment='生效截至日期')
    debtendmode = Column(CHAR(1), comment='合约到期模式')
    debtenddate = Column(Date, comment='负债合约到期日')
    debtterm = Column(Integer, comment='合约期限')
    sourcetype = Column(CHAR(1), comment="数据来源 '0'自有券源 '1'专项券源")
    status = Column(CHAR(1), comment='状态 Btczt (0 未到期 1 已了结 2 到期未了结)')
    posistkprice = Column(DECIMAL(9, 3), comment='首次调拨的收盘价')
    intrdate = Column(Date, comment='计息日期 ')
    stkpricemode = Column(CHAR(1), comment='计息价格模式')
    updated_at = Column(DateTime, comment='更新时间')


class SecStkprice(Base):
    __tablename__ = 'sec_stkprice'
    __table_args__ = {'comment': '行情库（日终）客户'}

    stk_code = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    market = Column(VARCHAR(4), comment='交易市场')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    stk_name = Column(VARCHAR(200), comment='证券名称')
    last_close_price = Column(DECIMAL(26, 8), comment='昨日收盘')
    close_price = Column(DECIMAL(26, 8), comment='收盘价')
    open_price = Column(DECIMAL(26, 8), comment='今日开盘')
    last_price = Column(DECIMAL(26, 8), comment='最近成交')
    high_price = Column(DECIMAL(26, 8), comment='最高成交')
    low_price = Column(DECIMAL(26, 8), comment='最低价')
    match_qty = Column(DECIMAL(26, 0), comment='成交数量')
    match_amt = Column(DECIMAL(26, 4), comment='成交金额')
    stk_cls_level_I = Column(VARCHAR(12), comment='一级分类')
    stk_cls_level_II = Column(VARCHAR(12), comment='二级分类(产品类型代码)')
    total_share = Column(DECIMAL(26, 4), comment='证券总股本')
    tra_shares = Column(DECIMAL(26, 4), comment='流通股')
    mkt_fi_convert_flag = Column(CHAR(1), comment='融资标的-交易所')
    mkt_sl_convert_flag = Column(CHAR(1), comment='融券标的-交易所')
    mkt_convert_update_dt = Column(Date, comment='交易所标的证券最后更新日期')
    mkt_gage_flag = Column(CHAR(1), comment='是否可作为融资融券可冲抵保证金证券-交易所')
    mkt_value_rate = Column(DECIMAL(26, 8), comment='折算率-交易所')
    mkt_collat_update_dt = Column(Date, comment='交易所证券担保费率更新日期')
    fi_convert_flag = Column(CHAR(1), comment='融资标的-券商')
    sl_convert_flag = Column(CHAR(1), comment='融券标的-券商')
    fi_guar_rate = Column(DECIMAL(26, 8), comment='融资保证金比例（%）-券商')
    sl_guar_rate = Column(DECIMAL(26, 8), comment='融券保证金比例（%）-券商')
    convert_update_dt = Column(Date, comment='标的证券最后更新日期-券商')
    gage_flag = Column(CHAR(1), comment='是否可作为融资融券可冲抵保证金证券-券商')
    collat_update_dt = Column(Date, comment='证券担保费率更新日期-券商')
    value_rate = Column(DECIMAL(26, 8), comment='折算率-券商')
    risk_score = Column(DECIMAL(9, 3), comment='风险评分')
    match_amt_avg = Column(DECIMAL(19, 2), comment='最近30天平均成交额（日终算一次）')


class SecStkpriceAm(Base):
    __tablename__ = 'sec_stkprice_am'
    __table_args__ = {'comment': '行情库am（stkprice）'}

    serverid = Column(BigInteger, primary_key=True, nullable=False, comment='机器编码')
    market = Column(VARCHAR(4), primary_key=True, nullable=False, comment='交易市場')
    stkcode = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    closeprice = Column(DECIMAL(26, 4), comment='收盘价')
    openprice = Column(DECIMAL(26, 4), comment='开盘价')
    lastprice = Column(DECIMAL(26, 4), comment='最近成交')
    highprice = Column(DECIMAL(26, 4), comment='最高成交')
    lowprice = Column(DECIMAL(26, 4), comment='最低价')
    matchqty = Column(BigInteger)
    matchamt = Column(DECIMAL(19, 2))
    bondintr = Column(DECIMAL(12, 8))
    mtkcalflag = Column(VARCHAR(4))
    fairprice = Column(DECIMAL(26, 4), comment='公允价')


class SecStkpriceReal(Base):
    __tablename__ = 'sec_stkprice_real'
    __table_args__ = {'comment': '行情库（实时）'}

    stk_code = Column(CHAR(8), primary_key=True, comment='证券代码')
    close_price = Column(DECIMAL(26, 4), comment='昨日收盘')
    curr_price = Column(DECIMAL(26, 4), comment='现价')
    open_price = Column(DECIMAL(26, 4), comment='开盘价')
    high_price = Column(DECIMAL(26, 4), comment='最高价')
    low_price = Column(DECIMAL(26, 4), comment='最低价')
    match_qty = Column(BigInteger, comment='成交数量')
    match_amt = Column(DECIMAL(26, 4), comment='成交金额')
    market = Column(CHAR(1), comment='0深圳 1上海')
    stk_type = Column(CHAR(1), comment='S股票 B债券 F基金')
    high_limit_price = Column(DECIMAL(26, 4), comment='涨停价')
    low_limit_price = Column(DECIMAL(26, 4), comment='跌停价')


class SecStopstkcodeAm(Base):
    __tablename__ = 'sec_stopstkcode_am'
    __table_args__ = {'comment': '停牌证券信息（stopstkcode）'}

    serverid = Column(BigInteger, primary_key=True, nullable=False, comment='机器编码')
    market = Column(VARCHAR(4), primary_key=True, nullable=False, comment='市场代码')
    stkcode = Column(CHAR(8), primary_key=True, nullable=False, comment='证券代码')
    fairvaluemode = Column(VARCHAR(4), comment='公允价计算模式')
    calcudate = Column(Date, comment='开始公允计算日期')
    endcalcudate = Column(Date, comment='停止公允计算日期')
    fairvalue = Column(DECIMAL(26, 4), comment='公允价')
    stopdate = Column(Date, comment='停牌日期')
    industcode = Column(CHAR(8), comment='行业指数代码')
    industexponent = Column(DECIMAL(26, 4), comment='停牌时行业指数')
    industlastprice = Column(DECIMAL(26, 4), comment='行业指数最近收盘价格')
    sourcetype = Column(VARCHAR(4), comment='数据来源')


class SecVipCustomer(Base):
    __tablename__ = 'sec_vip_customers'
    __table_args__ = {'comment': 'VIP客户信息表'}

    serverid = Column(VARCHAR(32), primary_key=True, nullable=False, comment='服务器编号')
    belong_org_id = Column(VARCHAR(12), comment='缺省的机构')
    cust_id = Column(VARCHAR(19), comment='客户代码')
    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金帐户')
    vip_id = Column(VARCHAR(32), comment='开通VIP标识')
    batchsync = Column(CHAR(1), comment='批量同步 ')
    biz_date = Column(Date, primary_key=True, nullable=False, comment='数据日期')


class Security(Base):
    __tablename__ = 'securities'
    __table_args__ = {'comment': '全市场证券基础信息'}

    code = Column(VARCHAR(20), primary_key=True, comment='证券代码')
    cn_name = Column(VARCHAR(128), comment='证券全称')
    cn_short_name = Column(VARCHAR(128), comment='证券简称')
    type = Column(Integer, comment='证券类型(0: 股票;1：基金;2：债券)')
    board = Column(VARCHAR(32), comment='板块')
    industry_sw_1 = Column(VARCHAR(64), comment='申万一级行业')
    industry_sw_2 = Column(VARCHAR(64))
    updated_at = Column(DateTime, comment='更新时间')
    biz_date = Column(Date, comment='业务日期')
    listed_at = Column(Date, comment='上市时间')
    created_at = Column(DateTime)
    datetime = Column(DateTime)
    ipo_type = Column(VARCHAR(32), comment='发行制度')
    status = Column(Integer, server_default=text("'1'"), comment='发行状态：1发行中、2发行失败 、3发行完待上市、4已成立或存续、5暂停上市、6终止上市、7正常上市、8退市中、9拟发行、10已退市')
    is_guarantees = Column(Integer, server_default=text("'0'"))
    stk_sort = Column(VARCHAR(32), comment='证券分类(股票-主板、创业版等  债券-可转债等)')
    market = Column(VARCHAR(20), comment='证券市场')
    bond_stk_code = Column(VARCHAR(32), comment='债券正股代码')
    delisted_at = Column(Date, comment='退市日期')


class SecuritiesChange(Base):
    __tablename__ = 'securities_change'
    __table_args__ = {'comment': '证券变动（深证信）'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False)
    stk_name = Column(VARCHAR(20), comment='证券简称')
    stk_type = Column(VARCHAR(1), comment='证券类型(S: 股票;F：基金;B：债券)')
    change_date = Column(Date, primary_key=True, nullable=False, comment='变动日期')
    change_thing = Column(VARCHAR(20), comment='变动事项')
    change_status = Column(VARCHAR(20), comment='变动后状态')
    change_reason = Column(TEXT, comment='变动原因')
    declaration_date = Column(Date, comment='公告日期')
    sec_code = Column(VARCHAR(30), comment='带后缀的code')


class SecuritiesConversionRate(Base):
    __tablename__ = 'securities_conversion_rate'
    __table_args__ = {'comment': '证券折算率管理'}

    code = Column(VARCHAR(12), primary_key=True, comment='证券代码')
    is_guarantees = Column(Integer, nullable=False, comment='是否是担保券')
    cn_short_name = Column(VARCHAR(24), nullable=False, comment='中文简称')
    ceiling = Column(Float, comment='折算率上限')
    basic = Column(Float, comment='基础折算率')
    mmpairment = Column(Float, comment='折算率减值')
    custom = Column(Float, comment='手动调整')
    before = Column(Float, comment='调整前折算率')
    after = Column(Float, comment='调整后折算率')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    source = Column(Float, comment='原始折算率')


class SecuritiesConversionRateHistory(Base):
    __tablename__ = 'securities_conversion_rate_history'
    __table_args__ = {'comment': '证券折算率管理历史'}

    code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    is_guarantees = Column(Integer, nullable=False, comment='是否是担保券')
    cn_short_name = Column(VARCHAR(12), nullable=False, comment='中文简称')
    ceiling = Column(Float, comment='折算率上限')
    basic = Column(Float, comment='基础折算率')
    mmpairment = Column(Float, comment='折算率减值')
    custom = Column(Float, comment='手动调整')
    before = Column(Float, comment='调整前折算率')
    after = Column(Float, comment='调整后折算率')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    date = Column(Date, primary_key=True, nullable=False, comment='日期')


class SecuritiesMetricsByConfig(Base):
    __tablename__ = 'securities_metrics_by_config'
    __table_args__ = (
        Index('idx_department_metrics', 'department_id', 'data_dictionary_metrics_id', unique=True),
        {'comment': '指标分类'}
    )

    id = Column(Integer, primary_key=True, comment='ID')
    department_id = Column(Integer, nullable=False, comment='部门ID')
    type_id = Column(Integer, index=True, comment='类别ID')
    data_dictionary_metrics_id = Column(Integer, nullable=False, index=True, comment='指标ID')
    updated_at = Column(DateTime, nullable=False, comment='更新时间')
    created_at = Column(DateTime, nullable=False, comment='创建时间')


class SecuritiesScore(Base):
    __tablename__ = 'securities_score'
    __table_args__ = (
        Index('idx_com_date_score', 'securities_code', 'plan_copy_id', 'date', unique=True),
        {'comment': '证券评分'}
    )

    id = Column(Integer, primary_key=True, comment='ID')
    securities_code = Column(VARCHAR(12), nullable=False, index=True, comment='证券代码')
    department_id = Column(Integer, nullable=False, index=True, comment='部门ID')
    final_score = Column(Float, comment='最终得分')
    total_score = Column(JSON, nullable=False, comment='汇总分列表')
    rating_score = Column(JSON, nullable=False, comment='评分项列表')
    rating_type_score = Column(JSON, nullable=False, comment='评分项类别平均分列表')
    industry_score = Column(JSON, comment='基于行业分数')
    plan_copy_id = Column(Integer, nullable=False, index=True, comment='方案快照表ID')
    date = Column(Date, nullable=False, index=True, comment='得分日期')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    final_detail = Column(JSON, comment='最终得分')


class SecuritiesScorePlan(Base):
    __tablename__ = 'securities_score_plan'
    __table_args__ = {'comment': '评分方案列表'}

    id = Column(Integer, primary_key=True, comment='ID')
    department_id = Column(Integer, nullable=False, index=True, comment='部门ID')
    name = Column(VARCHAR(64), nullable=False, comment='方案名称')
    describe = Column(VARCHAR(255), comment='描述')
    status = Column(Integer, nullable=False, server_default=text("'1'"), comment='状态（0：删除；1：正常）')
    is_safe = Column(Integer, comment='是否是安全方案（1：是;0：不是）')
    created_by = Column(Integer, nullable=False, comment='创建人')
    updated_at = Column(DateTime, nullable=False, comment='更新时间')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    risk_grade_status = Column(Integer)
    created_by_name = Column(VARCHAR(120), comment='创建人姓名')
    updated_by_name = Column(VARCHAR(120), comment='编辑者姓名')


class SecuritiesScorePlanCopy(Base):
    __tablename__ = 'securities_score_plan_copy'
    __table_args__ = {'comment': '评分方案详细'}

    id = Column(Integer, primary_key=True, comment='ID')
    plan_id = Column(Integer, index=True, comment='方案ID')
    department_id = Column(Integer, nullable=False, index=True, comment='部门ID')
    status = Column(Integer, nullable=False, comment='状态')
    rating_item_list = Column(JSON, nullable=False, comment='评分项配置')
    total_score_list = Column(JSON, nullable=False, comment='汇总分配置')
    total_score_process_list = Column(JSON, nullable=False, comment='后处理配置')
    securities_metrics_list = Column(JSON, nullable=False, comment='指标列表')
    securities_plan_created_by = Column(Integer, nullable=False, comment='创建人')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    plan_name = Column(VARCHAR(64), comment='方案名称')
    securities_plan_created_by_name = Column(String(120), comment='创建人')
    period = Column(String(32), comment='计算周期')


class StBadDebtsCust(Base):
    __tablename__ = 'st_bad_debts_cust'
    __table_args__ = {'comment': '坏账客户'}

    task_id = Column(BigInteger, primary_key=True, nullable=False, comment='任务ID')
    flag = Column(TINYINT, primary_key=True, nullable=False, comment='标识 -1-无含义 自定义压测类型的象征')
    bad_debts_cust_num_before = Column(DECIMAL(26, 4), comment='坏账客户数_压测前')
    bad_debts_cust_num_after = Column(DECIMAL(26, 4), comment='坏账客户数_压测后')
    bad_debts_cust_avg_keeprate_before = Column(DECIMAL(26, 4), comment='坏账客户平均维保比例_压测前   ')
    bad_debts_cust_avg_keeprate_after = Column(DECIMAL(26, 4), comment='坏账客户平均维保比例_压测后 ')
    bad_debts_cust_debt_before = Column(DECIMAL(26, 4), comment='坏账客户负债金额_压测前  ')
    bad_debts_cust_debt_after = Column(DECIMAL(26, 4), comment='坏账客户负债金额_压测后')
    expect_bad_debts_amt_before = Column(DECIMAL(26, 4), comment='预计坏账金额_压测前 ')
    expect_bad_debts_amt_after = Column(DECIMAL(26, 4), comment='预计坏账金额_压测后')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建日期')
    gmt_modified = Column(DateTime)


class StCustAccountDetail(Base):
    __tablename__ = 'st_cust_account_detail'
    __table_args__ = {'comment': '客户账户明细'}

    task_id = Column(BigInteger, primary_key=True, nullable=False, comment='主键-作为唯一标识')
    fund_id = Column(VARCHAR(100), primary_key=True, nullable=False, comment='资金账号 ')
    flag = Column(TINYINT, primary_key=True, nullable=False, comment='标识 -1-无含义  1-轻度5%  2-中度10% 3-重度-20% ')
    cust_name = Column(VARCHAR(100), comment='客户名称')
    cust_type = Column(VARCHAR(100), comment='客户类型')
    cust_risk_score = Column(DECIMAL(26, 4), comment='客户风险评分')
    org_name = Column(VARCHAR(100), comment='营业部名称')
    keeprate_before = Column(DECIMAL(26, 4), comment='维持担保比例_压测前')
    keeprate_after = Column(DECIMAL(26, 4), comment='维持担保比例_压测后')
    keeprate_change = Column(DECIMAL(26, 4), comment='维持担保比例_变动率')
    expect_keeprate_amt_before = Column(DECIMAL(26, 4), comment='预计追保金额_压测前（万元）')
    expect_keeprate_amt_after = Column(DECIMAL(26, 4), comment='预计追保金额_压测后（万元）')
    expect_bad_debts_amt_before = Column(DECIMAL(26, 4), comment='预计坏账金额_压测前（万元）')
    expect_bad_debts_amt_after = Column(DECIMAL(26, 4), comment='预计坏账金额_压测后（万元）')
    total_asset_before = Column(DECIMAL(26, 4), comment='总资产(万元) _ 压测前')
    total_asset_after = Column(DECIMAL(26, 4), comment='总资产(万元) _压测后')
    total_debts_before = Column(DECIMAL(26, 4), comment='总负债(万元)_压测前')
    total_debts_after = Column(DECIMAL(26, 4), comment='总负债(万元)_压测后')
    rz_bal = Column(DECIMAL(26, 4), comment='融资余额（万元）')
    rq_bal_before = Column(DECIMAL(26, 4), comment='融券余额（万元）_压测前')
    rq_bal_after = Column(DECIMAL(26, 4), comment='融券余额（万元）_压测后')
    rq_bal_before_after_diff_val = Column(VARCHAR(255), comment='融券余额前后差值')
    lr_bal_before = Column(DECIMAL(26, 4), comment='压测前两融余额')
    lr_bal_after = Column(DECIMAL(26, 4), comment='压测后两融余额')
    awkward_stk_code = Column(VARCHAR(20), comment='重仓证券代码')
    awkward_stk_name = Column(VARCHAR(30), comment='重仓证券名称')
    pos_concentration = Column(DECIMAL(26, 4), comment='持仓集中度')
    pos_price = Column(DECIMAL(26, 4), comment='持仓市值 (万元)')
    close_mkt_keeprate = Column(DECIMAL(26, 4), comment='收市维保')
    resist_stop_times = Column(DECIMAL(26, 4), comment='抗跌停次数')
    st_cust_range = Column(VARCHAR(100), comment='压测客户范围 ')
    st_cust_type = Column(VARCHAR(100), comment='压测客户类型  ')
    biz_date = Column(Date, comment='业务日期 (结果表 需要)')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建日期')
    gmt_modified = Column(DateTime)


class StCustKeeprateChange(Base):
    __tablename__ = 'st_cust_keeprate_change'
    __table_args__ = {'comment': '客户维保比例变动'}

    task_id = Column(BigInteger, primary_key=True, nullable=False, comment='任务ID')
    flag = Column(TINYINT, primary_key=True, nullable=False, comment='标识 -1-无含义  1-轻度5%  2-中度10% 3-重度-20%')
    cust_keep_rate = Column(VARCHAR(100), primary_key=True, nullable=False, comment='客户维保比例')
    stress_test_before_cust_num = Column(DECIMAL(26, 4), comment='压测前客户数')
    stress_test_after_cust_num = Column(DECIMAL(26, 4), comment='压测后客户数')
    change_rate = Column(DECIMAL(26, 4), comment='变动率（%）')
    stress_test_before_lr_bal = Column(DECIMAL(26, 4), comment='压测前两融余额（万元）')
    stress_test_after_lr_bal = Column(DECIMAL(26, 4), comment='压测后两融余额（万元）')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建日期')
    gmt_modified = Column(DateTime)


class StCustRangeDatum(Base):
    __tablename__ = 'st_cust_range_data'
    __table_args__ = {'comment': '客户范围修改临时表'}

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    biz_date = Column(Date, comment='业务时间')
    fund_id = Column(VARCHAR(32), unique=True, comment='资金账号')
    total_asset = Column(DECIMAL(26, 4), comment='总资产')
    keeprate_real = Column(DECIMAL(26, 4), comment='实时维保比例')
    cust_name = Column(VARCHAR(32), comment='客户名称')
    keeprate = Column(DECIMAL(26, 4), comment='收市维保比例')
    credit_test_score = Column(DECIMAL(26, 4), comment='客户风险评分')
    stk_code = Column(VARCHAR(32), comment='持仓证券代码')
    mktval = Column(DECIMAL(26, 4), comment='持仓证券市值')
    stk_name = Column(VARCHAR(32), comment='证券名称')
    sum_fund_id_rz_bal = Column(DECIMAL(26, 4), comment='融资余额（同一资金账户）')
    sum_fund_id_rq_bal = Column(DECIMAL(26, 4), comment='融券余额（同一资金账户）')
    pos_concentration = Column(DECIMAL(26, 4), comment='持仓集中度')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)


class StCustRangeSet(Base):
    __tablename__ = 'st_cust_range_set'
    __table_args__ = {'comment': '客户范围修改临时表'}

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    task_id = Column(BigInteger, comment='任务ID')
    fund_id = Column(VARCHAR(100), comment='资金账户')
    keeprate_real = Column(DECIMAL(26, 4), comment='实时维保比例')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)


class StCustomRiseFallRange(Base):
    __tablename__ = 'st_custom_rise_fall_range'
    __table_args__ = (
        Index('uk_task_id_stk_code', 'task_id', 'stk_code', unique=True),
        {'comment': '自定义个券涨跌幅'}
    )

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    task_id = Column(BigInteger, comment='任务ID')
    stk_code = Column(VARCHAR(12), comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    rise_fall_range = Column(DECIMAL(26, 4), comment='涨跌幅(跌负数，涨正数)')
    control_panel_num = Column(DECIMAL(26, 4), comment='调控板设定天数(是负就负数，是正就正数)')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)
    stage = Column(Integer, comment='场景标记，1：场景1；2：场景2；3：场景3')


class StFullMktRiseFallRange(Base):
    __tablename__ = 'st_full_mkt_rise_fall_range'
    __table_args__ = {'comment': '全市场涨跌幅'}

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    task_id = Column(BigInteger, comment='任务ID')
    full_mkt = Column(VARCHAR(64), comment='全市场')
    rise_fall_range = Column(DECIMAL(26, 4), comment='涨跌幅')
    control_panel_num = Column(DECIMAL(26, 4), comment='涨跌幅个数')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)
    stage = Column(Integer, comment='场景标记;1:场景1；2:场景2；3：场景3')
    is_beta = Column(TINYINT, server_default=text("'0'"), comment='贝塔系数校正，0-否 1-是，默认0')


class StInduRiseFallRange(Base):
    __tablename__ = 'st_indu_rise_fall_range'
    __table_args__ = (
        Index('uk_task_id_indu_code', 'task_id', 'indu_code', unique=True),
        {'comment': '行业涨跌幅'}
    )

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    task_id = Column(BigInteger, comment='任务ID')
    indu_code = Column(VARCHAR(64), comment='以及行业代码')
    rise_fall_range = Column(DECIMAL(26, 4), comment='涨跌幅')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)
    is_beta = Column(TINYINT, server_default=text("'0'"), comment='贝塔系数校正，0-否 1-是，默认0')
    control_panel_num = Column(DECIMAL(26, 4), comment='涨跌幅个数')
    stage = Column(Integer, comment='场景标记；1:场景1；2:场景2；3:场景3')
    group_id = Column(Integer, server_default=text("'0'"), comment='标识行业分组，同个值为同个分组，默认值为0')


class StInspectSubmitCustKeeprateChange(Base):
    __tablename__ = 'st_inspect_submit_cust_keeprate_change'
    __table_args__ = {'comment': '监管报送 > 客户维保比例变动'}

    task_id = Column(BigInteger, primary_key=True, nullable=False, comment='任务ID')
    flag = Column(TINYINT, primary_key=True, nullable=False, comment='标识 -1-无含义 0-压测前数据 1-轻度5%  2-中度10% 3-重度-20%')
    data = Column(JSON, comment='指标 > 设定为 json 格式数据')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建日期')
    gmt_modified = Column(DateTime)


class StMktBoardRiseFallRange(Base):
    __tablename__ = 'st_mkt_board_rise_fall_range'
    __table_args__ = {'comment': '市场板块涨跌幅'}

    id = Column(BIGINT, primary_key=True, comment='自增ID')
    task_id = Column(BigInteger, comment='任务ID')
    board_code = Column(VARCHAR(64), comment='板块代码')
    board_name = Column(VARCHAR(32), comment='板块名称')
    rise_fall_range = Column(DECIMAL(26, 4), comment='涨跌幅')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)
    is_beta = Column(TINYINT, server_default=text("'0'"), comment='贝塔系数校正，0-否 1-是，默认0')
    control_panel_num = Column(DECIMAL(26, 4), comment='涨跌幅个数')
    stage = Column(Integer, comment='场景标记；1：场景-1；2：场景2；3：场景3')
    group_id = Column(Integer, server_default=text("'0'"), comment='标识板块场景分组，同个值为同个分组，默认值为0')


class StNeedToKeeprateCust(Base):
    __tablename__ = 'st_need_to_keeprate_cust'
    __table_args__ = {'comment': '需追保客户'}

    task_id = Column(BigInteger, primary_key=True, nullable=False, comment='任务ID')
    flag = Column(TINYINT, primary_key=True, nullable=False, comment='标识 -1-无含义  1-轻度5%  2-中度10% 3-重度-20% ')
    need_to_keeprate_cust_num_before = Column(DECIMAL(26, 4), comment='需追保客户数_压测前 ')
    need_to_keeprate_cust_num_after = Column(DECIMAL(26, 4), comment='需追保客户数_压测后')
    need_to_avg_keeprate_cust_before = Column(DECIMAL(26, 4), comment='需追保客户平均维保比例_压测前 ')
    need_to_avg_keeprate_cust_after = Column(DECIMAL(26, 4), comment='需追保客户平均维保比例_压测后 ')
    need_to_keeprate_cust_debt_amt_before = Column(DECIMAL(26, 4), comment='需追保客户负债金额_压测前')
    need_to_keeprate_cust_debt_amt_after = Column(DECIMAL(26, 4), comment='需追保客户负债金额_压测后')
    expect_keeprate_amt_before = Column(DECIMAL(26, 4), comment='预计追保金额_压测前 ')
    expect_keeprate_amt_after = Column(DECIMAL(26, 4), comment='预计追保金额_压测后 ')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建日期')
    gmt_modified = Column(DateTime)


class StSituationPreview(Base):
    __tablename__ = 'st_situation_preview'
    __table_args__ = {'comment': '压测情景预览表'}

    task_id = Column(BigInteger, primary_key=True, nullable=False, comment='任务ID')
    stk_code = Column(VARCHAR(12), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(128), nullable=False, comment='证券简称\\r\\n')
    base_period_close_price = Column(DECIMAL(26, 4), comment='基期收盘价')
    rise_fall_range = Column(DECIMAL(26, 4), comment='涨跌幅')
    last_period_close_price = Column(DECIMAL(26, 4), comment='末期收盘价')
    flag = Column(TINYINT, primary_key=True, nullable=False, comment='标识 -1-无含义  1-轻度5%  2-中度10% 3-重度-20% ')
    biz_date = Column(Date, comment='业务日期 (开始压测的日期)')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建日期')
    gmt_modified = Column(DateTime)


class StTask(Base):
    __tablename__ = 'st_task'
    __table_args__ = {'comment': '压力测试任务表'}

    task_id = Column(BIGINT, primary_key=True, comment='自增主键')
    task_name = Column(VARCHAR(64), comment='任务名称')
    created_by = Column(Integer, comment='创建人ID')
    created_by_name = Column(VARCHAR(32), comment='创建人姓名')
    task_type = Column(TINYINT, comment='任务类型1-自定义压测 2-全市场压测（监管报送）')
    flag_desc = Column(VARCHAR(255), comment='从sec_config中读入')
    created_at = Column(DateTime, comment='任务创建时间')
    begin_at = Column(DateTime, comment='压测开始时间')
    finish_at = Column(DateTime, comment='压测结束时间')
    task_status = Column(TINYINT, comment='状态，1-等待开始 2-压测中 3-已完成 4-计算失败 5-已取消')
    situation_type = Column(TINYINT, comment='情景类型，1-全市场统一模拟 2-单券/多券模拟 3-自定义模拟')
    biz_date = Column(Date, comment='业务日期 - 压测开始时间 不需要时分秒')
    base_period = Column(Date, comment='基期')
    last_period = Column(Date, comment='末期')
    time_span = Column(Integer, comment='时间跨度')
    rise_fall_range_limit = Column(VARCHAR(255), comment='涨跌幅限制')
    is_beta = Column(TINYINT, comment='贝塔系数校正，0-否 1-是，默认0')
    force_line = Column(DECIMAL(26, 4), comment='平仓线')
    warn_line = Column(DECIMAL(26, 4), comment='预警线')
    wear_pos_cust_break_contract_rate = Column(DECIMAL(26, 4), comment='穿仓户违约率')
    is_deleted = Column(TINYINT, server_default=text("'0'"), comment='是否删除，0-否 1-是')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime)
    cust_range = Column(VARCHAR(10), server_default=text("'all'"), comment='客户范围')
    rise_fall_range_type = Column(Integer, comment='涨跌幅类型；0-涨跌幅；1-涨跌停个数')


class StkListImport(Base):
    __tablename__ = 'stk_list_import'
    __table_args__ = {'comment': '两融折算率名单'}

    stk_code = Column(VARCHAR(20), primary_key=True, comment='证券代码')
    stk_name = Column(VARCHAR(30), comment='证券简称')
    stk_status = Column(VARCHAR(60), comment='证券状态')
    import_time = Column(DateTime, nullable=False, comment='导入时间')
    pledgerate_limit = Column(DECIMAL(26, 4), comment='限定折算率')
    rz_guarantee_rate_limit = Column(DECIMAL(26, 4), comment='限定融资保证金比例')
    rq_guarantee_rate_limit = Column(DECIMAL(26, 4), comment='限定融券保证金比例')
    concentration_limit = Column(DECIMAL(26, 4), comment='限定集中度')
    biz_date = Column(Date, nullable=False, comment='业务日期')
    gmt_create = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    gmt_modified = Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')


class StkSecLimitExtList(Base):
    __tablename__ = 'stk_sec_limit_ext_list'
    __table_args__ = {'comment': '限制融券展期证券'}

    stk_code = Column(String(20, 'utf8mb4_general_ci'), primary_key=True, comment='证券代码')
    stk_name = Column(String(50, 'utf8mb4_general_ci'), nullable=False, comment='证券名称')
    stk_status = Column(String(100, 'utf8mb4_general_ci'), comment='证券状态')
    import_time = Column(DateTime, comment='导入时间')
    biz_date = Column(Date, comment='业务日期')


class StockDayPrice(Base):
    __tablename__ = 'stock_day_price'
    __table_args__ = (
        Index('uk_date_stk_code', 'date', 'stk_code', unique=True),
        {'comment': '东财上市日股票状态行情'}
    )

    stk_code = Column(VARCHAR(20), primary_key=True, nullable=False, comment='证券代码')
    date = Column(String(8, 'utf8mb4_general_ci'), primary_key=True, nullable=False, comment='交易日期')
    open_price = Column(DECIMAL(26, 4), comment='开盘价')
    pre_close_price = Column(DECIMAL(26, 4), comment='前收盘价')
    high_limit_price = Column(DECIMAL(26, 4), comment='涨停价')
    low_limit_price = Column(DECIMAL(26, 4), comment='跌停价')
    stock_type = Column(Integer, comment='类型, 1:A股; 2:B股;3:新三板')


class StockFinIdx(Base):
    __tablename__ = 'stock_fin_idx'
    __table_args__ = (
        Index('code_latest_period_index', 'stk_code', 'latest_period_fin_dt'),
        {'comment': '财务指标'}
    )

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='股票代码')
    trd_mkt_code = Column(VARCHAR(10), comment='交易市场代码')
    coid = Column(VARCHAR(10), comment='公司id')
    wind_code = Column(VARCHAR(10), comment='wind代码')
    trd_date = Column(DECIMAL(10, 0), comment='交易日期')
    sw_sec_code = Column(VARCHAR(12), comment='申万二级行业代码')
    latest_period_fin_dt = Column(Integer, comment='最新财报日期')
    latest_yperiod_fin_dt = Column(Integer, comment='最近财年日期')
    last_yperiod_fin_dt = Column(Integer, comment='上个财年日期')
    cash_cash_equ_end_period = Column(DECIMAL(26, 4), comment='期末现金及现金等价物余额')
    depr_fa_coga_dpba = Column(DECIMAL(26, 4), comment='固定资产和投资性房地产折旧')
    amort_intang_assets = Column(DECIMAL(26, 4), comment='无形资产摊销')
    amort_lt_deferred_exp = Column(DECIMAL(26, 4), comment='长期待摊费用摊销')
    net_cash_flows_oper_act = Column(DECIMAL(26, 4), comment='经营活动现金流量净额')
    la1ysp_net_cash_flows_oper_act = Column(DECIMAL(26, 4), comment='去年同期经营活动现金流量净额')
    la2ysp_net_cash_flows_oper_act = Column(DECIMAL(26, 4), comment='前年同期经营活动现金流量净额')
    la3ysp_net_cash_flows_oper_act = Column(DECIMAL(26, 4), comment='大前年同期经营活动现金流量净额')
    cash_recp_sg_and_rs = Column(DECIMAL(26, 4), comment='销售商品、提供劳务收到的现金')
    net_cash_flows_inv_act = Column(DECIMAL(26, 4), comment='投资活动现金流量净额')
    la1ysp_net_cash_flows_inv_act = Column(DECIMAL(26, 4), comment='去年同期投资活动现金流量净额')
    la2ysp_net_cash_flows_inv_act = Column(DECIMAL(26, 4), comment='前年同期投资活动现金流量净额')
    la3ysp_net_cash_flows_inv_act = Column(DECIMAL(26, 4), comment='大前年同期投资活动现金流量净额')
    ncfo_bcom_prop_3ymin = Column(DECIMAL(26, 4), comment='近3年经营活动/营业收入最小值')
    asset_liab_rate = Column(DECIMAL(26, 4), comment='资产负债率')
    debt_asset_liab_rate = Column(DECIMAL(26, 4), comment='剔除预收账款后的资产负债率')
    weight_avg_net_asset_inco_rate = Column(DECIMAL(26, 4), comment='净资产收益率(加权)')
    launch_cptl_repay_rate = Column(DECIMAL(26, 4), comment='投入资本回报率')
    sale_net_intr_rate = Column(DECIMAL(26, 4), comment='销售净利率')
    sale_net_intr_rate_3yinc = Column(DECIMAL(26, 4), comment='最近3年销售净利率复合增长率')
    salegross_profit_margin = Column(DECIMAL(26, 4), comment='销售毛利率')
    gro_sal_diff = Column(DECIMAL(26, 4), comment='毛销差')
    salegross_profit_margin_3yinc = Column(DECIMAL(26, 4), comment='近3年销售毛利率复合增长率')
    dednlos_netpft = Column(DECIMAL(26, 4), comment='扣除非经常性损益后的净利润')
    dn_bi_prop = Column(DECIMAL(26, 4), comment='扣除非经常性损益后的净利率')
    dednlos_netpft_recyport = Column(DECIMAL(26, 4), comment='最新年报扣除非经常性损益后的净利润')
    dednlos_netpft_rec3yinc = Column(DECIMAL(26, 4), comment='最近3年扣除非经常性损益后的净利润复合增长率')
    totl_asset_net_profit = Column(DECIMAL(26, 4), comment='总资产报酬率')
    totl_asset_net_profit_3yinc = Column(DECIMAL(26, 4), comment='最近3年总资产报酬率复合增速')
    net_asset_payoff_rate = Column(DECIMAL(26, 4), comment='净资产收益率')
    net_asset_payoff_rate_3yinc = Column(DECIMAL(26, 4), comment='最近3年净资产收益率复合增速')
    biz_out_inco_exp_net_profit = Column(DECIMAL(26, 4), comment='营业外收支净额/利润总额')
    sale_prd_srv_rec_cash_inco = Column(DECIMAL(26, 4), comment='销售商品提供劳务收到的现金/营业收入')
    already_get_intr_mul = Column(DECIMAL(26, 4), comment='已获利息倍数(EBIT/利息费用)')
    intr_tax_before_profit = Column(DECIMAL(26, 4), comment='息税前利润ebit')
    intr_tax_depr_amor_bef_profit = Column(DECIMAL(26, 4), comment='息税折旧摊销前利润ebitda')
    sale_exps_biz_all_income = Column(DECIMAL(26, 4), comment='销售费用率')
    finance_exps_biz_all_income = Column(DECIMAL(26, 4), comment='财务费用率')
    receive_turnover = Column(DECIMAL(26, 4), comment='应收账款周转率')
    receive_turnover_3yinc = Column(DECIMAL(26, 4), comment='近3年应收账款周转率复合增长率')
    preapy_turnover = Column(DECIMAL(26, 4), comment='预付账款周转率')
    inv_turnover = Column(DECIMAL(26, 4), comment='存货周转率')
    inv_turnover_3yinc = Column(DECIMAL(26, 4), comment='最近3年存货周转率复合增速')
    current_ratio = Column(DECIMAL(26, 4), comment='流动比率')
    quick_ratio = Column(DECIMAL(26, 4), comment='速动比率')
    cash_ratio = Column(DECIMAL(26, 4), comment='现金比')
    flow_asset_turnover = Column(DECIMAL(26, 4), comment='流动资产周转率')
    flow_asset_turnover_recyport = Column(DECIMAL(26, 4), comment='最新年度流动资产周转率')
    flow_asset_turnover_rec1yport = Column(DECIMAL(26, 4), comment='最新1年度流动资产周转率')
    flow_asset_turnover_rec2yport = Column(DECIMAL(26, 4), comment='最新2年度流动资产周转率')
    flow_asset_turnover_rec3yport = Column(DECIMAL(26, 4), comment='最新3年度流动资产周转率')
    flow_asset_turnover_days = Column(Integer, comment='流动资产周天数')
    flow_asset_turnover_recy_days = Column(Integer, comment='最新年度流动资产周天数')
    flow_asset_turnover_rec1y_days = Column(Integer, comment='最新1年度流动资产周天数')
    flow_asset_turnover_rec2y_days = Column(Integer, comment='最新2年度流动资产周天数')
    flow_asset_turnover_rec3y_days = Column(Integer, comment='最新3年度流动资产周天数')
    fix_asset_turnover = Column(DECIMAL(26, 4), comment='固定资产周转率')
    fix_asset_turnover_recyport = Column(DECIMAL(26, 4), comment='最新年度固定资产周转率')
    fix_asset_turnover_rec1yport = Column(DECIMAL(26, 4), comment='最新1年度固定资产周转率')
    fix_asset_turnover_rec2yport = Column(DECIMAL(26, 4), comment='最新2年度固定资产周转率')
    fix_asset_turnover_rec3yport = Column(DECIMAL(26, 4), comment='最新3年度固定资产周转率')
    fix_asset_turnover_days = Column(Integer, comment='固定资产周转天数')
    fix_asset_turnover_recy_days = Column(Integer, comment='最新年度固定资产周转天数')
    fix_asset_turnover_rec1y_days = Column(Integer, comment='最新1年度固定资产周转天数')
    fix_asset_turnover_rec2y_days = Column(Integer, comment='最新2年度固定资产周转天数')
    fix_asset_turnover_rec3y_days = Column(Integer, comment='最新3年度固定资产周转天数')
    totl_asset_turnover = Column(DECIMAL(26, 4), comment='总资产周转率')
    totl_asset_turnover_recyport = Column(DECIMAL(26, 4), comment='最新年总资产周转率')
    totl_asset_turnover_rec1yport = Column(DECIMAL(26, 4), comment='最新1年总资产周转率')
    totl_asset_turnover_rec2yport = Column(DECIMAL(26, 4), comment='最新2年总资产周转率')
    totl_asset_turnover_rec3yport = Column(DECIMAL(26, 4), comment='最新3年总资产周转率')
    totl_asset_turnover_days = Column(Integer, comment='总资产周转天数')
    totl_asset_turnover_recy_days = Column(Integer, comment='最新年总资产周转天数')
    totl_asset_turnover_rec1y_days = Column(Integer, comment='最新1年总资产周转天数')
    totl_asset_turnover_rec2y_days = Column(Integer, comment='最新2年总资产周转天数')
    totl_asset_turnover_rec3y_days = Column(Integer, comment='最新3年总资产周转天数')
    have_intr_debt = Column(DECIMAL(26, 4), comment='带息债务')
    hid_ta_prop = Column(DECIMAL(26, 4), comment='有息负债占总资产比例')
    st_rigid_liab = Column(DECIMAL(26, 4), comment='短期刚性负债')
    mc_srl_prop = Column(DECIMAL(26, 4), comment='货币资金/短期刚性负债')
    tangible_asset_liab_total = Column(DECIMAL(26, 4), comment='有形资产/负债合计')
    income_tax_profit_gross = Column(DECIMAL(26, 4), comment='所得税/利润总额')
    goodwill = Column(DECIMAL(26, 4), comment='商誉')
    gw_tseim_prop = Column(DECIMAL(26, 4), comment='商誉/净资产(所有者权益合计)')
    gw_np_prop = Column(DECIMAL(26, 4), comment='商誉/归母利润(归属于母公司所有者的净利润)')
    tot_shrhldr_eqy_incl_min_int = Column(DECIMAL(26, 4), comment='所有者权益合计')
    tot_assets = Column(DECIMAL(26, 4), comment='资产总计')
    tot_assets_recyport = Column(DECIMAL(26, 4), comment='最新年度资产总计')
    tot_assets_3yagos = Column(DECIMAL(26, 4), comment='3年前资产总计')
    tot_assets_3yinc = Column(DECIMAL(26, 4), comment='最近3年资产总计复合增速')
    acct_rcv = Column(DECIMAL(26, 4), comment='应收账款')
    acct_rcv_lastperiod = Column(DECIMAL(26, 4), comment='上期应收账款')
    bad_debt_tot = Column(DECIMAL(26, 4), comment='最新年度应收账款坏账准备')
    bdt_ar_prop = Column(DECIMAL(26, 4), comment='应收账款坏账准备/应收账款(坏账计提比例)')
    const_in_prog = Column(DECIMAL(26, 4), comment='在建工程')
    cip_ta_prop = Column(DECIMAL(26, 4), comment='在建工程/资产总计')
    intang_assets = Column(DECIMAL(26, 4), comment='无形资产')
    ia_ta_prop = Column(DECIMAL(26, 4), comment='无形资产/资产总计')
    prepay = Column(DECIMAL(26, 4), comment='预付款项')
    ppm_ca_prop = Column(DECIMAL(26, 4), comment='预付款项/流动资产合计')
    tot_cur_assets = Column(DECIMAL(26, 4), comment='流动资产合计')
    inventories = Column(DECIMAL(26, 4), comment='存货')
    tot_cur_liab = Column(DECIMAL(26, 4), comment='流动负债合计')
    oth_rcv = Column(DECIMAL(26, 4), comment='其他应收款')
    or_tseim_prop = Column(DECIMAL(26, 4), comment='其他应收款/净资产(所有者权益合计)')
    accounts_payable = Column(DECIMAL(26, 4), comment='应收票据及应收账款')
    stm_bs_tot = Column(DECIMAL(26, 4), comment='固定资产')
    lt_borrow = Column(DECIMAL(26, 4), comment='长期借款')
    bonds_payable = Column(DECIMAL(26, 4), comment='应付债券')
    int_payable = Column(DECIMAL(26, 4), comment='应付利息')
    monetary_cap = Column(DECIMAL(26, 4), comment='货币资金')
    mc_ta_prop = Column(DECIMAL(26, 4), comment='货币资金/资产总计')
    st_borrow = Column(DECIMAL(26, 4), comment='短期借款')
    notes_payable = Column(DECIMAL(26, 4), comment='应付票据')
    non_cur_liab_due_within_1y = Column(DECIMAL(26, 4), comment='一年内到期的非流动负债')
    tot_liab = Column(DECIMAL(26, 4), comment='负债合计')
    adv_from_cust = Column(DECIMAL(26, 4), comment='预收款项')
    synthetic_payoff_gross_parent = Column(DECIMAL(26, 4), comment='最新财报归属于母公司所有者的净利润')
    sync_pof_gros_prt_recyport = Column(DECIMAL(26, 4), comment='最新年度归属于母公司所有者的净利润')
    sync_pof_gros_prt_3yagos = Column(DECIMAL(26, 4), comment='3年前归属于母公司所有者的净利润')
    sync_pof_gros_prt_3yinc = Column(DECIMAL(26, 4), comment='最近3年归属于母公司所有者的净利润复合增长率')
    biz_income = Column(DECIMAL(26, 4), comment='营业收入')
    income_overseas = Column(DECIMAL(26, 4), comment='海外营业收入')
    io_bi_prop = Column(DECIMAL(26, 4), comment='海外业务/营业收入')
    biz_income_recyport = Column(DECIMAL(26, 4), comment='最新年度营业总收入')
    biz_income_rec1yport = Column(DECIMAL(26, 4), comment='最新1年度营业总收入')
    biz_income_rec2yport = Column(DECIMAL(26, 4), comment='最新2年度营业总收入')
    biz_income_rec3yport = Column(DECIMAL(26, 4), comment='最新3年度营业总收入')
    biz_income_lastperiod = Column(DECIMAL(26, 4), comment='上期营业收入')
    bi_inc_ar_inc_prop = Column(DECIMAL(26, 4), comment='营业收入增长/应收款增长')
    biz_income_3yagos = Column(DECIMAL(26, 4), comment='3年前营业总收入')
    biz_income_3inc = Column(DECIMAL(26, 4), comment='最近3年营业复合增长率')
    less_biz_cost = Column(DECIMAL(26, 4), comment='营业成本')
    net_profit_include_stkhld_pl = Column(DECIMAL(26, 4), comment='净利润')
    add_biz_outside_income = Column(DECIMAL(26, 4), comment='营业外收入')
    less_biz_outside_expense = Column(DECIMAL(26, 4), comment='营业外支出')
    finance_exps_intr_fee = Column(DECIMAL(26, 4), comment='利息费用')
    less_sale_exps = Column(DECIMAL(26, 4), comment='销售费用')
    less_finance_exps = Column(DECIMAL(26, 4), comment='财务费用')
    less_assets_devaluation = Column(DECIMAL(26, 4), comment='资产减值损失')
    biz_profit = Column(DECIMAL(26, 4), comment='营业利润')
    lad_bp_prop = Column(DECIMAL(26, 4), comment='资产减值损失/营业利润')
    income_tax = Column(DECIMAL(26, 4), comment='所得税费用')
    profit_gross = Column(DECIMAL(26, 4), comment='税前利润')
    asset_liab_rate_media = Column(DECIMAL(26, 4), comment='资产负债率行业中位数')
    debt_asset_liab_rate_media = Column(DECIMAL(26, 4), comment='剔除预收账款后的资产负债率行业中位数')
    sale_net_intr_rate_media = Column(DECIMAL(26, 4), comment='销售净利率行业中位数')
    salegross_profit_margin_media = Column(DECIMAL(26, 4), comment='销售毛利率行业中位数')
    dednlos_netpft_recyport_media = Column(DECIMAL(26, 4), comment='最近年报扣除非经常性损益后的净利润行业中位数')
    dedpft_recyport_3yinc_media = Column(DECIMAL(26, 4), comment='最近3年扣除非经常性损益后的净利润复合增长率行业中位数,')
    totl_asset_net_profit_media = Column(DECIMAL(26, 4), comment='总资产报酬率行业中位数')
    net_asset_payoff_rate_media = Column(DECIMAL(26, 4), comment='净资产收益率行业中位数')
    sain_cain_prop_media = Column(DECIMAL(26, 4), comment='销售商品提供劳务收到的现金/营业收入行业中位数')
    already_get_intr_mul_media = Column(DECIMAL(26, 4), comment='已获利息倍数(EBIT/利息费用)行业中位数')
    intr_tax_before_profit_media = Column(DECIMAL(26, 4), comment='息税前利润ebit行业中位数')
    ebitda_media = Column(DECIMAL(26, 4), comment='息税折旧摊销前(ebitda)利润行业中位数')
    sale_exps_biz_all_income_media = Column(DECIMAL(26, 4), comment='销售费用率行业中位数')
    gro_sal_diff_media = Column(DECIMAL(26, 4), comment='毛销差行业中位数')
    fin_exps_biz_all_inco_media = Column(DECIMAL(26, 4), comment='财务费用率行业中位数')
    receive_turnover_media = Column(DECIMAL(26, 4), comment='应收账款周转率中位数')
    preapy_turnover_media = Column(DECIMAL(26, 4), comment='预付账款周转率中位数')
    inv_turnover_media = Column(DECIMAL(26, 4), comment='存货周转率行业中位数')
    current_ratio_media = Column(DECIMAL(26, 4), comment='流动比率行业中位数')
    quick_ratio_media = Column(DECIMAL(26, 4), comment='速动比率行业中位数')
    flow_asset_turnover_days_media = Column(Integer, comment='流动资产周天数行业中位数')
    flaturn_recy_days_media = Column(Integer, comment='最新年度流动资产周天数行业中位数')
    fix_asset_turnover_days_media = Column(Integer, comment='固定资产周转天数中位数')
    fiaturn_recy_days_media = Column(Integer, comment='最新年度固定资产周转天数中位数')
    totl_asset_turnover_days_media = Column(Integer, comment='总资产周转天数行业中位数')
    toaturn_recy_days_media = Column(Integer, comment='最新年度总资产周转天数行业中位数')
    mc_srl_prop_media = Column(DECIMAL(26, 4), comment='货币资金/短期刚性负债中位数')
    tangibl_ast_liab_total_media = Column(DECIMAL(26, 4), comment='有形资产/负债合计行业中位数')
    cip_ta_prop_media = Column(DECIMAL(26, 4), comment='在建工程占总资产比例行业中位数')
    ia_ta_prop_media = Column(DECIMAL(26, 4), comment='无形资产占总资产比例行业中位数')
    ppm_ca_prop_media = Column(DECIMAL(26, 4), comment='预付账款占流动资产比例中位数')
    sync_pof_gros_prt_3yinc_media = Column(DECIMAL(26, 4), comment='3年归属于母公司所有者的净利润复合增长率中位数')
    biz_income_3inc_media = Column(DECIMAL(26, 4), comment='最近3年营业复合增长率中位数')
    less_biz_cost_media = Column(DECIMAL(26, 4), comment='营业成本行业中值')
    less_assets_devaluation_media = Column(DECIMAL(26, 4), comment='同行业资产减值损失中位数')
    tdy_totl_mkt_val_media = Column(DECIMAL(26, 4), comment='个股总市值行业中位数')
    pe_ratio_ttm_media = Column(DECIMAL(26, 4), comment='市盈率(TTM)行业中值')
    pb_ratio_media = Column(DECIMAL(26, 4), comment='市净率(MRQ)行业中值')
    biz_income_media = Column(DECIMAL(26, 4), comment='营业收入行业中值')
    sync_pof_gros_prt_media = Column(DECIMAL(26, 4), comment='归属于母公司所有者的净利润行业中值')
    dn_bi_prop_media = Column(DECIMAL(26, 4), comment='扣除非经常性损益后的净利率中值')
    dednlos_netpft_media = Column(DECIMAL(26, 4), comment='扣除非经常性损益后的净利润中值')
    income_overseas_media = Column(DECIMAL(26, 4), comment='海外业务收入中值')
    io_bi_prop_media = Column(DECIMAL(26, 4), comment='海外业务/营业中值')
    bi_inc_ar_inc_prop_media = Column(DECIMAL(26, 4), comment='营业收入增长/应收款增长中值')
    boi_enp_prop_media = Column(DECIMAL(26, 4), comment='营业外收支净额/利润总额中值')
    ncfo_bcom_prop_3ymin_media = Column(DECIMAL(26, 4), comment='经营活动现金流量净额/营业收入最小值中值')
    ntca_floa_media = Column(DECIMAL(26, 4), comment='经营活动现金流量净额中值')
    lad_bp_prop_media = Column(DECIMAL(26, 4), comment='资产减值损失/营业利润中值')
    bdt_ar_prop_media = Column(DECIMAL(26, 4), comment='坏账计提比例中值')
    or_tseim_prop_media = Column(DECIMAL(26, 4), comment='其他应收款/净资产(所有者权益合计)中值')
    gw_tseim_prop_media = Column(DECIMAL(26, 4), comment='商誉/净资产(所有者权益合计)中值')
    gw_np_prop_media = Column(DECIMAL(26, 4), comment='商誉/归母利润(归属于母公司所有者的净利润)中值')
    mc_ta_prop_media = Column(DECIMAL(26, 4), comment='货币资金/资产总计中值')
    cash_ratio_media = Column(DECIMAL(26, 4), comment='现金比中值')
    hid_ta_prop_media = Column(DECIMAL(26, 4), comment='有息负债占总资产比例中值')
    it_pg_prop_media = Column(DECIMAL(26, 4), comment='所得税/利润总额中值')
    mkt_val_industry_rank = Column(Integer, comment='市值行业排名')
    comp_cnt = Column(Integer, comment='所属行业总公司数')
    turnover = Column(DECIMAL(26, 4), comment='换手率')
    turnover_last3m_avg = Column(DECIMAL(26, 4), comment='最近3个月日均换手率')
    turnover_last6m_avg = Column(DECIMAL(26, 4), comment='最近6个月日均换手率')
    tdy_totl_mkt_val = Column(DECIMAL(26, 4), comment='个股总市值(交易币种)')
    tdy_totl_mkt_val_last6m_avg = Column(DECIMAL(26, 4), comment='最近半年日均个股市值')
    pe_ratio_ttm = Column(DECIMAL(26, 4), comment='市盈率(TTM)')
    pb_ratio = Column(DECIMAL(26, 4), comment='市净率(MRQ)')
    recovered_close_price = Column(DECIMAL(26, 4), comment='收盘价(后复权)')
    recovered_clos_pri_last250trd = Column(DECIMAL(26, 4), comment='250交易日前收盘价(后复权)')
    recovered_gene = Column(DECIMAL(26, 4), comment='累计复权因子')
    match_amt = Column(DECIMAL(26, 4), comment='成交额')
    match_amt_last3m_avg = Column(DECIMAL(26, 4), comment='最近6个月日均成交额（字段名错，历史原因）')
    close_price = Column(DECIMAL(26, 4), comment='当日收盘价')
    yest_close_price = Column(DECIMAL(26, 4), comment='昨日收盘价')
    sec_abbr = Column(VARCHAR(100), comment='股票简称')
    susp_date = Column(DECIMAL(26, 4), comment='最新停牌起始时间')
    continus_susp_date = Column(DECIMAL(26, 4), comment='连续停牌最早起始时间')
    continus_days = Column(DECIMAL(26, 4), comment='连续停牌天数')
    is_continus5dsusp = Column(DECIMAL(26, 4), comment='是否连续停牌5天')
    resume_trading_date = Column(DECIMAL(26, 4), comment='最新停牌截止时间')
    ashare_gl_cptl = Column(DECIMAL(26, 4), comment='A股总股本')
    pledge_ratio = Column(DECIMAL(26, 4), comment='质押比例')
    ful_mkt_pledge_tot = Column(DECIMAL(26, 4), comment='全市场质押股数')
    pledge_glaxy_tot = Column(DECIMAL(26, 4), comment='质押于银河总股数')
    pledge_glaxy_prop = Column(DECIMAL(26, 4), comment='质押于银河比例')
    fst_hold_pledge_tot = Column(DECIMAL(26, 4), comment='第一大股东质押股数')
    hold_pledge_tot = Column(DECIMAL(26, 4), comment='控股股东持股总数')
    fhpt_hpt_prop = Column(DECIMAL(26, 4), comment='控股股东质押总数/持股总数')
    fhpt_agc_prop = Column(DECIMAL(26, 4), comment='控股股东质押总数/总股本')
    fhpt_sum_hpt_prop = Column(DECIMAL(26, 4), comment='持股5%以上控股质押总数/持股总数')
    fhpt_sum_agc_prop = Column(DECIMAL(26, 4), comment='持股5%以上控股质押总数/总股本')
    com_value_mul = Column(DECIMAL(26, 4), comment='企业价值倍数')
    ann_volatility = Column(DECIMAL(26, 4), comment='收盘价年化波动率')
    data_time = Column(DateTime, comment='数据时间')
    is_st = Column(VARCHAR(2), comment='是否ST')
    pledge_mkt_value = Column(DECIMAL(26, 4), comment='质押股份市值')
    trust_ast_mang_hold_artio = Column(DECIMAL(26, 4), comment='信托资管持股比例')
    div_fin_ratio = Column(DECIMAL(26, 4), comment='分红融资比')
    cumu_cash_div_tot = Column(DECIMAL(26, 4), comment='累计现金分红总额')
    div_fin_ratio_qunt = Column(DECIMAL(26, 4), comment='累计现金分红总额百分比')
    cumu_cash_div_tot_qunt = Column(DECIMAL(26, 4), comment='分红融资比百分位')
    turnover_last6m_avg_qunt = Column(DECIMAL(26, 4), comment='换手率百分位')
    totl_mkt_val_last6m_avg_qunt = Column(DECIMAL(26, 4), comment='市值百分位')
    dednlos_netpft_qunt = Column(DECIMAL(26, 4), comment='扣除非经常性损益百分位')
    biz_income_3inc_qunt = Column(DECIMAL(26, 4), comment='营业收入复合增长率百分位')
    sync_pof_gros_prt_3yinc_qunt = Column(DECIMAL(26, 4), comment='归母净利润复合增长率百分位')
    tot_assets_3yinc_qunt = Column(DECIMAL(26, 4), comment='总资产复合增长率百分位')
    net_cash_flows_oper_act_qunt = Column(DECIMAL(26, 4), comment='现金流净额百分位')
    ann_volatility_qunt = Column(DECIMAL(26, 4), comment='波动率年化百分位')
    match_amt_last6m_avg_qunt = Column(DECIMAL(26, 4), comment='成交额百分位')
    ntcs_flows_opat_last_y1 = Column(DECIMAL(26, 4), comment='最近年度经营活动现金流量净额')
    ntcs_flows_opat_last_y2 = Column(DECIMAL(26, 4), comment='最近1年度经营活动现金流量净额')
    ntcs_flows_opat_last_y3 = Column(DECIMAL(26, 4), comment='最近2年度经营活动现金流量净额')
    cash_recp_sg_and_rs_last_y1 = Column(DECIMAL(26, 4), comment='最近年度销售商品提供劳务收到的现金')
    cash_recp_sg_and_rs_last_y2 = Column(DECIMAL(26, 4), comment='最近1年度销售商品提供劳务收到的现金')
    cash_recp_sg_and_rs_last_y3 = Column(DECIMAL(26, 4), comment='最近2年度销售商品提供劳务收到的现金')
    sync_pof_gros_prt_last_y2 = Column(DECIMAL(26, 4), comment='最近1年度归属于母公司所有者的净利润')
    sync_pof_gros_prt_last_y3 = Column(DECIMAL(26, 4), comment='最近2年度归属于母公司所有者的净利润')
    pledge_date = Column(DECIMAL(26, 4), comment='最近质押日期')
    match_qty_tot_90d = Column(DECIMAL(26, 4), comment='近90个交易日累计成交量')
    par_val = Column(DECIMAL(26, 4), comment='股票面值')
    ashare_stkhld_hz_hold = Column(DECIMAL(26, 4), comment='A股股东户数')
    pe_ratio = Column(DECIMAL(26, 4), comment='静态市盈率')
    curd_guar_securities_mkt = Column(DECIMAL(26, 4), comment='当日日末担保证券市值')
    curd_securities_mkt = Column(DECIMAL(26, 4), comment='当日日末证券总市值')
    guar_sec_prop = Column(DECIMAL(26, 4), comment='当日日末担保证券市值占该证券总市值比重')
    biz_date = Column(Integer, primary_key=True, nullable=False, comment='业务日期')
    tdy_liq_mkt_val = Column(DECIMAL(26, 4), comment='当日流通市值')
    asset_liab_ratio_perc = Column(DECIMAL(26, 4), comment='最近2年1期资产负债率均值百分位')
    net_profit_gr_perc = Column(DECIMAL(26, 4), comment='近三年扣除非经常性损益后的净利润复合增长率百分位')
    roe_perc = Column(DECIMAL(26, 4), comment='最近2年1期净资产收益率均值百分位')
    pe_ttm_perc = Column(DECIMAL(26, 4), comment='市盈率(PE,TTM)百分位')
    pb_perc = Column(DECIMAL(26, 4), comment='市净率(PB,MRQ)百分位')
    liq_mar_val_perc = Column(DECIMAL(26, 4), comment='流通市值百分位')
    avg_vol_3m_perc = Column(DECIMAL(26, 4), comment='近三个月日均成交额百分位')
    volatility_3m_perc = Column(DECIMAL(26, 4), comment='近三个月波动率周化百分位')
    volatility_6m = Column(DECIMAL(26, 4), comment='近半年股价振幅')
    ps_ttm = Column(DECIMAL(26, 4), comment='市销率(PS,TTM)')
    dednlos_netpft_netpft_prop = Column(DECIMAL(26, 4), comment='扣非后归母净利润/归母净利润')
    gw_ta_prop = Column(DECIMAL(26, 4), comment='商誉/总资产')
    op_period = Column(DECIMAL(26, 4), comment='营业周期')
    income_growth_rate = Column(DECIMAL(26, 4), comment='营业收入同比增长率')
    sync_pof_gros_prt_perc = Column(DECIMAL(26, 4), comment='归母净利润全市场百分位')
    income_growth_rate_perc = Column(DECIMAL(26, 4), comment='营业收入同比增长率全市场百分位')
    dednlos_netpft_netpft_prop_perc = Column(DECIMAL(26, 4), comment='扣非后归母净利润/归母净利润全市场百分位')
    gw_ta_prop_perc = Column(DECIMAL(26, 4), comment='商誉/总资产全市场百分位')
    asset_liab_rate_std_perc = Column(DECIMAL(26, 4), comment='资产负债率(行业标准化后)全市场百分位')
    already_get_intr_mul_std_perc = Column(DECIMAL(26, 4), comment='已获利息倍数(行业标准化后)全市场百分位')
    op_period_std_perc = Column(DECIMAL(26, 4), comment='营业周期(行业标准化后)全市场百分位')
    last3m_avg_vol_perc = Column(DECIMAL(26, 4), comment='近半年日均成交额全市场百分位')
    totl_mkt_val_last6m_avg_perc = Column(DECIMAL(26, 4), comment='近半年日均市值全市场百分位')
    ann_volatility_perc = Column(DECIMAL(26, 4), comment='收盘价年化波动率全市场百分位')
    beta_perc = Column(DECIMAL(26, 4), comment='Beta全市场百分位')
    volatility_6m_perc = Column(DECIMAL(26, 4), comment='近半年股价振幅全市场百分位')
    pe_ttm_std_perc = Column(DECIMAL(26, 4), comment='市盈率(PE,TTM,行业标准化后)全市场百分位')
    pb_std_perc = Column(DECIMAL(26, 4), comment='市净率(PB,MRQ,行业标准化后)全市场百分位')
    ps_ttm_std_perc = Column(DECIMAL(26, 4), comment='市销率(PE,TTM,行业标准化后)全市场百分位')
    com_value_mul_std_perc = Column(DECIMAL(26, 4), comment='企业价值倍数(行业标准化后)全市场百分位')
    listed_days = Column(DECIMAL(26, 4), comment='上市天数')
    outstand_mkt_val_avg_m6 = Column(DECIMAL(26, 4), comment='区间(近六个月)日均流通市值')
    outstand_mkt_val_avg_qunt_m6 = Column(DECIMAL(26, 4), comment='区间(近六个月)日均流通市值百分位')
    pb_ratio_qunt = Column(DECIMAL(26, 4), comment='市净率百分位')
    pe_ratio_qunt = Column(DECIMAL(26, 4), comment='市盈率百分位')
    ps = Column(DECIMAL(26, 4), comment='市销率')
    ps_qunt = Column(DECIMAL(26, 4), comment='市销率百分位')
    sale_net_intr_rate_qunt = Column(DECIMAL(26, 4), comment='销售净利率百分位')
    tdy_outstand_mkt_val = Column(DECIMAL(26, 4), comment='当日流通市值')
    match_qty = Column(DECIMAL(26, 4), comment='成交量')
    net_asset_payoff_rate_qunt = Column(DECIMAL(26, 4), comment='扣非加权净资产收益率ROE百分位')
    net_profit_inc_qunt_y3 = Column(DECIMAL(26, 4), comment='近三年净利润复合年增长率百分位')
    net_op_cf_or_prop_ttm = Column(DECIMAL(26, 4), comment='经营活动现金流量净额/营业收入（TTM）')
    net_op_cf_or_prop_ttm_perc = Column(DECIMAL(26, 4), comment='经营活动现金流量净额/营业收入（TTM）_全市场百分位')
    roe_exdlt = Column(DECIMAL(26, 4), comment='净资产收益率（扣除摊薄）')
    roe_exdlt_avg_3y = Column(DECIMAL(26, 4), comment='净资产收益率（扣除摊薄）_最近三年均值')
    roe_exdlt_avg_3y_perc = Column(DECIMAL(26, 4), comment='净资产收益率（扣除摊薄）_最近三年均值_全市场百分位')
    inv_turnover_3yinc_media = Column(DECIMAL(26, 4), comment='最近三年存货周转率复合增长率_行业中位数')
    receive_turnover_3yinc_media = Column(DECIMAL(26, 4), comment='最近三年应收账款周转率复合增长率_行业中位数')


class SuspendedTableUpchina(Base):
    __tablename__ = 'suspended_table_upchina'
    __table_args__ = {'comment': '中国A股停复牌历史（优品）'}

    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, index=True, comment='股票代码')
    susp_date = Column(Date, primary_key=True, nullable=False, comment='停牌起始日期')
    resume_trading_date = Column(Date, comment='复牌日期')
    susp_reason = Column(TEXT, comment='停牌原因')
    data_time = Column(DateTime, comment='数据时间')
    biz_date = Column(Date, server_default=text("'2020-12-12'"), comment='业务日期')
    num_susp_days = Column(Integer, comment='停牌天数')


class SwConversionRateAdjHistory(Base):
    __tablename__ = 'sw_conversion_rate_adj_history'
    __table_args__ = {'comment': '折算率定调记录'}

    biz_date = Column(Date, primary_key=True, nullable=False, comment='业务日期')
    stk_code = Column(VARCHAR(10), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    grt_in = Column(VARCHAR(10), comment='保证金调入')
    grt_out = Column(VARCHAR(10), comment='保证金调出')
    grt_before = Column(VARCHAR(10), comment='保证金调整前')
    grt_after = Column(VARCHAR(10), comment='保证金调整后')
    fb_in = Column(VARCHAR(10), comment='融资标的券变化调入')
    fb_out = Column(VARCHAR(10), comment='融资标的券变化调入')
    fb_before = Column(VARCHAR(10), comment='融资标的券变化调整前')
    fb_after = Column(VARCHAR(10), comment='融资标的券变化调整后')
    ss_in = Column(VARCHAR(10), comment='融券标的券变化调入')
    ss_out = Column(VARCHAR(10), comment='融券标的券变化调出')
    ss_before = Column(VARCHAR(10), comment='融券标的券变化调整前')
    ss_after = Column(VARCHAR(10), comment='融券标的券变化调整后')
    flag = Column(Integer, primary_key=True, nullable=False, comment='标记：1，日初定调；2，科创板融券；3，周五盘后调整 ')
    sec_code = Column(VARCHAR(10), comment='证券代码（带后缀）')
    created_at = Column(DateTime, nullable=False, comment='创建时间')


class SwGuaranteeAdj(Base):
    __tablename__ = 'sw_guarantee_adj'
    __table_args__ = {'comment': '担保券调整表'}

    stk_code = Column(CHAR(18), primary_key=True, nullable=False, comment='证券代码')
    cr = Column(VARCHAR(100), comment='参考变化原因')
    stk_name = Column(VARCHAR(100), comment='证券简称')
    cfl = Column(Integer, comment='上期折算率(%)')
    ri = Column(VARCHAR(100), comment='所属指数')
    vt = Column(VARCHAR(100), comment='变动类型')
    vd = Column(Date, primary_key=True, nullable=False, comment='变动日期')
    st = Column(VARCHAR(20), comment='证券品种')
    market = Column(VARCHAR(20), comment='交易市场')
    re = Column(VARCHAR(10), comment='是否注册制上市')
    cf = Column(Integer, comment='最新折算率(%)')
    pel = Column(VARCHAR(10), comment='上周最后一个交易日静态市盈率')
    sec_code = Column(VARCHAR(100), comment='证券代码（带后缀）')
    datatime = Column(DateTime, comment='数据日期')


class SwGuaranteeList(Base):
    __tablename__ = 'sw_guarantee_list'
    __table_args__ = {'comment': '担保券名单'}

    stk_code = Column(VARCHAR(20), primary_key=True, comment='证券代码')
    stk_name = Column(VARCHAR(10), comment='证券简称')
    rate = Column(VARCHAR(10), comment='折算率')
    state = Column(Integer)
    market = Column(VARCHAR(10), comment='市场')
    createUser = Column(Integer)
    createDate = Column(Date)
    updateUser = Column(Integer)
    updateDate = Column(Date, comment='更新日期')
    trimDate = Column(Date)
    lrate = Column(VARCHAR(10), comment='上一次使用的折算率（非0）')
    datatime = Column(DateTime, comment='数据日期')


class SwSecuritiesStatu(Base):
    __tablename__ = 'sw_securities_status'
    __table_args__ = {'comment': '证券状态（从深圳证券信息网站上爬取）'}

    stk_name = Column(VARCHAR(20), comment='证券简称')
    status = Column(Integer, comment='状态：0，正常；1，首日上市；2，上市满5个交易日；3，上市满3个月；')
    updated_at = Column(Date, comment='更新时间')
    created_at = Column(Date, comment='创建时间')
    stk_code = Column(VARCHAR(6), primary_key=True, comment='证券代码')
    sec_code = Column(VARCHAR(10))
    datatime = Column(DateTime, comment='数据日期')


class SwStaticPe(Base):
    __tablename__ = 'sw_static_pe'
    __table_args__ = {'comment': '静态市盈率表'}

    sec_code = Column(VARCHAR(10), comment='证券代码（带后缀）')
    pe = Column(Float(asdecimal=True), comment='本周静态市盈率')
    tradeDate = Column(Date, primary_key=True, nullable=False, comment='变动日期')
    market = Column(VARCHAR(10), comment='交易市场')
    lastweekPe = Column(Float(asdecimal=True), comment='上周静态市盈率')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    pe3 = Column(Float(asdecimal=True), comment='静态市盈率（含追溯调整）')
    pe2 = Column(Float(asdecimal=True), comment='静态市盈率（交易所）')
    changeDirection = Column(VARCHAR(20), comment='变化方向')
    stk_code = Column(CHAR(6), primary_key=True, nullable=False, comment='证券代码')
    datatime = Column(DateTime, comment='数据日期')


class SwUnderlyingAdj(Base):
    __tablename__ = 'sw_underlying_adj'
    __table_args__ = {'comment': '标的券调整表'}

    stk_code = Column(CHAR(6), primary_key=True, nullable=False, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    market = Column(VARCHAR(10), comment='交易市场')
    ss = Column(VARCHAR(10), comment='融券标的券变化')
    td = Column(Date, primary_key=True, nullable=False, comment='变动日期')
    st = Column(VARCHAR(10), comment='证券品种')
    fb = Column(VARCHAR(10), comment='融资标的券变化')
    memo = Column(VARCHAR(100), comment='涨跌幅限制')
    sec_code = Column(VARCHAR(10), comment='证券代码（带后缀）')
    datatime = Column(DateTime, comment='数据日期')


class SwUnderlyingList(Base):
    __tablename__ = 'sw_underlying_list'
    __table_args__ = {'comment': '标的券名单'}

    stk_code = Column(CHAR(6), primary_key=True, comment='证券代码')
    stk_name = Column(VARCHAR(20), comment='证券简称')
    rzRatio = Column(VARCHAR(10), comment='融资保证金比例')
    rqRatio = Column(VARCHAR(10), comment='融券保证金比例')
    market = Column(VARCHAR(10), comment='市场')
    createUser = Column(Integer)
    createDate = Column(Date)
    updateUser = Column(Integer)
    updateDate = Column(Date, comment='更新日期')
    state = Column(Integer)
    trimDate = Column(Date)
    datatime = Column(DateTime, comment='数据日期')


class UploadFileInfo(Base):
    __tablename__ = 'upload_file_info'
    __table_args__ = {'comment': '上传文件信息表'}

    url = Column(String(200, 'utf8mb4_general_ci'), comment='上传路径')
    file_name = Column(String(100, 'utf8mb4_general_ci'), primary_key=True, nullable=False, comment='文件名称')
    location = Column(String(100, 'utf8mb4_general_ci'), comment='文件位置')
    file_size = Column(Float(10), comment='大小，单位M')
    upload_at = Column(DateTime, comment='上传时间')
    module_tag = Column(String(200, 'utf8mb4_general_ci'), primary_key=True, nullable=False, comment='所属模块')


t_v_fin_afordpnifee = Table(
    'v_fin_afordpnifee', metadata,
    Column('fund_id', String(100)),
    Column('pni_fee_tot', DECIMAL(56, 4)),
    Column('avl_amt', DECIMAL(19, 2))
)


t_v_net_short_position = Table(
    'v_net_short_position', metadata,
    Column('fund_id', String(100)),
    Column('stk_code', CHAR(8)),
    Column('biz_date', Date),
    Column('belong_org_id', String(12)),
    Column('ref_mrkt_val', DECIMAL(48, 4)),
    Column('unrepaid_mkt', DECIMAL(48, 4)),
    Column('share_bal', DECIMAL(48, 4)),
    Column('unrepaid_qtty', DECIMAL(48, 0)),
    Column('net_long_value', DECIMAL(49, 4)),
    Column('net_short_value', DECIMAL(49, 4)),
    Column('net_long_qty', DECIMAL(53, 4)),
    Column('net_short_qty', DECIMAL(53, 4))
)


t_v_sec_afordpnifee = Table(
    'v_sec_afordpnifee', metadata,
    Column('fund_id', String(100)),
    Column('pni_fee_tot', DECIMAL(54, 4)),
    Column('avl_amt', DECIMAL(19, 2))
)


class AttentionPool(Base):
    __tablename__ = 'attention_pool'
    __table_args__ = {'comment': '关注池'}

    id = Column(Integer, primary_key=True, comment='ID')
    stk_code = Column(ForeignKey('securities.code', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True, comment='证券代码')
    user_id = Column(Integer, nullable=False, comment='用户id')
    created_at = Column(DateTime, nullable=False, comment='创建时间')

    security = relationship('Security')


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = (
        Index('idx_department_type_name', 'department_id', 'type', 'name', unique=True),
        {'comment': '指标类别'}
    )

    id = Column(Integer, primary_key=True, comment='ID')
    department_id = Column(ForeignKey('department.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, comment='部门ID，1：质押；2：两融;10:客户风险等级')
    type = Column(Integer, nullable=False, comment='类别类型（0：评分项；1：指标；）')
    order_num = Column(Integer, nullable=False, comment='序号')
    name = Column(VARCHAR(32), nullable=False, comment='类别名称')
    created_by = Column(Integer, nullable=False, comment='创建人')
    updated_at = Column(DateTime, nullable=False, comment='更新时间')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by_name = Column(VARCHAR(120), comment='创建人姓名')

    department = relationship('Department')


class RiskGrade(Base):
    __tablename__ = 'risk_grade'
    __table_args__ = {'comment': '风险等级配置'}

    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, nullable=False)
    department_id = Column(ForeignKey('department.id'), nullable=False, index=True)
    height_risk_tv = Column(CHAR(32), nullable=False)
    middle_risk_tv = Column(CHAR(32), nullable=False)
    lower_risk_tv = Column(CHAR(32), nullable=False)
    user_id = Column(Integer, nullable=False)
    user_department_id = Column(Integer, nullable=False)
    updated_at = Column(Date, nullable=False)

    department = relationship('Department')


class TotalScore(Base):
    __tablename__ = 'total_score'
    __table_args__ = {'comment': '汇总分表'}

    id = Column(Integer, primary_key=True, comment='ID')
    plan_id = Column(ForeignKey('securities_score_plan.id', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False, index=True, comment='方案ID')
    name = Column(VARCHAR(64), nullable=False, comment='汇总分名称')
    model = Column(Integer, nullable=False, server_default=text("'0'"), comment='模式（0：加权平均值，1：求和）')
    created_by = Column(Integer, nullable=False, comment='创建人')
    updated_at = Column(DateTime, nullable=False, comment='更新时间')
    created_at = Column(DateTime, nullable=False, comment='创建时间')
    created_by_name = Column(String(120), comment='创建人姓名')

    plan = relationship('SecuritiesScorePlan')


class TotalScoreProcessRule(Base):
    __tablename__ = 'total_score_process_rule'
    __table_args__ = {'comment': '汇总分计算过程规则'}

    id = Column(Integer, primary_key=True, comment='ID')
    plan_id = Column(ForeignKey('securities_score_plan.id', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False, index=True, comment='评分项id')
    industry = Column(JSON, nullable=False, comment='行业')
    listed_sector = Column(JSON, comment='上市板块')
    public_offering_type = Column(JSON, comment='证券发行制度')

    plan = relationship('SecuritiesScorePlan')


class TotalScoreProcessRuleResult(Base):
    __tablename__ = 'total_score_process_rule_results'
    __table_args__ = {'comment': '汇总分计算过程规则结果'}

    id = Column(Integer, primary_key=True, comment='ID')
    total_score_process_rule_id = Column(ForeignKey('total_score_process_rule.id', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False, index=True, comment='后处理规则id')
    name = Column(VARCHAR(64), nullable=False)
    form = Column(VARCHAR(64))
    text = Column(VARCHAR(64))
    type = Column(VARCHAR(64), nullable=False)

    total_score_process_rule = relationship('TotalScoreProcessRule')


class TotalScoreProcessRuleTerm(Base):
    __tablename__ = 'total_score_process_rule_terms'
    __table_args__ = {'comment': '汇总分计算过程规则项'}

    id = Column(Integer, primary_key=True, comment='ID')
    total_score_process_rule_id = Column(ForeignKey('total_score_process_rule.id', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False, index=True, comment='后处理规则id')
    name = Column(VARCHAR(64), nullable=False)
    form = Column(VARCHAR(64))
    text = Column(VARCHAR(64))
    type = Column(VARCHAR(64), nullable=False)

    total_score_process_rule = relationship('TotalScoreProcessRule')


class TotalScoreWeight(Base):
    __tablename__ = 'total_score_weight'
    __table_args__ = {'comment': '汇总分权重'}

    id = Column(Integer, primary_key=True, comment='ID')
    total_score_id = Column(ForeignKey('total_score.id', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False, index=True, comment='汇总分ID')
    rating_item_id = Column(ForeignKey('rating_item.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True, comment='评分项ID')
    weight = Column(Integer, nullable=False, comment='权重')

    rating_item = relationship('RatingItem')
    total_score = relationship('TotalScore')
