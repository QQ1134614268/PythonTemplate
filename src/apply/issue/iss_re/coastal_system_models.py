# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, Date, DateTime, Float, ForeignKeyConstraint, Index, JSON, LargeBinary, String, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, CHAR, INTEGER, SMALLINT, TEXT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class QRTZCALENDAR(Base):
    __tablename__ = 'QRTZ_CALENDARS'
    __table_args__ = {'comment': '日历信息表'}

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    calendar_name = Column(String(200), primary_key=True, nullable=False, comment='日历名称')
    calendar = Column(LargeBinary, nullable=False, comment='存放持久化calendar对象')


class QRTZFIREDTRIGGER(Base):
    __tablename__ = 'QRTZ_FIRED_TRIGGERS'
    __table_args__ = {'comment': '已触发的触发器表'}

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    entry_id = Column(String(95), primary_key=True, nullable=False, comment='调度器实例id')
    trigger_name = Column(String(200), nullable=False, comment='qrtz_triggers表trigger_name的外键')
    trigger_group = Column(String(200), nullable=False, comment='qrtz_triggers表trigger_group的外键')
    instance_name = Column(String(200), nullable=False, comment='调度器实例名')
    fired_time = Column(BIGINT(13), nullable=False, comment='触发的时间')
    sched_time = Column(BIGINT(13), nullable=False, comment='定时器制定的时间')
    priority = Column(INTEGER(11), nullable=False, comment='优先级')
    state = Column(String(16), nullable=False, comment='状态')
    job_name = Column(String(200), comment='任务名称')
    job_group = Column(String(200), comment='任务组名')
    is_nonconcurrent = Column(String(1), comment='是否并发')
    requests_recovery = Column(String(1), comment='是否接受恢复执行')


class QRTZJOBDETAIL(Base):
    __tablename__ = 'QRTZ_JOB_DETAILS'
    __table_args__ = {'comment': '任务详细信息表'}

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    job_name = Column(String(200), primary_key=True, nullable=False, comment='任务名称')
    job_group = Column(String(200), primary_key=True, nullable=False, comment='任务组名')
    description = Column(String(250), comment='相关介绍')
    job_class_name = Column(String(250), nullable=False, comment='执行任务类名称')
    is_durable = Column(String(1), nullable=False, comment='是否持久化')
    is_nonconcurrent = Column(String(1), nullable=False, comment='是否并发')
    is_update_data = Column(String(1), nullable=False, comment='是否更新数据')
    requests_recovery = Column(String(1), nullable=False, comment='是否接受恢复执行')
    job_data = Column(LargeBinary, comment='存放持久化job对象')


class QRTZLOCK(Base):
    __tablename__ = 'QRTZ_LOCKS'
    __table_args__ = {'comment': '存储的悲观锁信息表'}

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    lock_name = Column(String(40), primary_key=True, nullable=False, comment='悲观锁名称')


class QRTZPAUSEDTRIGGERGRP(Base):
    __tablename__ = 'QRTZ_PAUSED_TRIGGER_GRPS'
    __table_args__ = {'comment': '暂停的触发器表'}

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    trigger_group = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_group的外键')


class QRTZSCHEDULERSTATE(Base):
    __tablename__ = 'QRTZ_SCHEDULER_STATE'
    __table_args__ = {'comment': '调度器状态表'}

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    instance_name = Column(String(200), primary_key=True, nullable=False, comment='实例名称')
    last_checkin_time = Column(BIGINT(13), nullable=False, comment='上次检查时间')
    checkin_interval = Column(BIGINT(13), nullable=False, comment='检查间隔时间')


class GenTable(Base):
    __tablename__ = 'gen_table'
    __table_args__ = {'comment': '代码生成业务表'}

    table_id = Column(BIGINT(20), primary_key=True, comment='编号')
    table_name = Column(String(200), server_default=text("''"), comment='表名称')
    table_comment = Column(String(500), server_default=text("''"), comment='表描述')
    sub_table_name = Column(String(64), comment='关联子表的表名')
    sub_table_fk_name = Column(String(64), comment='子表关联的外键名')
    class_name = Column(String(100), server_default=text("''"), comment='实体类名称')
    tpl_category = Column(String(200), server_default=text("'crud'"), comment='使用的模板（crud单表操作 tree树表操作）')
    package_name = Column(String(100), comment='生成包路径')
    module_name = Column(String(30), comment='生成模块名')
    business_name = Column(String(30), comment='生成业务名')
    function_name = Column(String(50), comment='生成功能名')
    function_author = Column(String(50), comment='生成功能作者')
    gen_type = Column(CHAR(1), server_default=text("'0'"), comment='生成代码方式（0zip压缩包 1自定义路径）')
    gen_path = Column(String(200), server_default=text("'/'"), comment='生成路径（不填默认项目路径）')
    options = Column(String(1000), comment='其它生成选项')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), comment='备注')


class GenTableColumn(Base):
    __tablename__ = 'gen_table_column'
    __table_args__ = {'comment': '代码生成业务表字段'}

    column_id = Column(BIGINT(20), primary_key=True, comment='编号')
    table_id = Column(String(64), comment='归属表编号')
    column_name = Column(String(200), comment='列名称')
    column_comment = Column(String(500), comment='列描述')
    column_type = Column(String(100), comment='列类型')
    java_type = Column(String(500), comment='JAVA类型')
    java_field = Column(String(200), comment='JAVA字段名')
    is_pk = Column(CHAR(1), comment='是否主键（1是）')
    is_increment = Column(CHAR(1), comment='是否自增（1是）')
    is_required = Column(CHAR(1), comment='是否必填（1是）')
    is_insert = Column(CHAR(1), comment='是否为插入字段（1是）')
    is_edit = Column(CHAR(1), comment='是否编辑字段（1是）')
    is_list = Column(CHAR(1), comment='是否列表字段（1是）')
    is_query = Column(CHAR(1), comment='是否查询字段（1是）')
    query_type = Column(String(200), server_default=text("'EQ'"), comment='查询方式（等于、不等于、大于、小于、范围）')
    html_type = Column(String(200), comment='显示类型（文本框、文本域、下拉框、复选框、单选框、日期控件）')
    dict_type = Column(String(200), server_default=text("''"), comment='字典类型')
    sort = Column(INTEGER(11), comment='排序')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')


class SysArea(Base):
    __tablename__ = 'sys_area'
    __table_args__ = {'comment': '城市区域'}

    id = Column(BIGINT(20), primary_key=True)
    code = Column(VARCHAR(12), nullable=False, unique=True, comment='区域编号')
    name = Column(VARCHAR(20), nullable=False, comment='区域名称')
    level = Column(INTEGER(11), index=True, server_default=text("'2'"), comment='查询基本,1 市 2 , 区/县 3,街道 默认新建都为 2(区/县)级别')
    parent_code = Column(VARCHAR(255), index=True)
    parent_id = Column(BIGINT(20), index=True, comment='父类Id')
    del_flag = Column(CHAR(1), nullable=False, server_default=text("'0'"), comment='状态  0 未删除 1 删除')
    create_by = Column(VARCHAR(64), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(VARCHAR(64), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(VARCHAR(200), server_default=text("''"), comment='备注')


class SysConfig(Base):
    __tablename__ = 'sys_config'
    __table_args__ = {'comment': '参数配置表'}

    config_id = Column(INTEGER(5), primary_key=True, comment='参数主键')
    config_name = Column(String(100), server_default=text("''"), comment='参数名称')
    config_key = Column(String(100), server_default=text("''"), comment='参数键名')
    config_value = Column(String(500), server_default=text("''"), comment='参数键值')
    config_type = Column(CHAR(1), server_default=text("'N'"), comment='系统内置（Y是 N否）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), comment='备注')


class SysDept(Base):
    __tablename__ = 'sys_dept'
    __table_args__ = {'comment': '部门表'}

    dept_id = Column(BIGINT(20), primary_key=True, comment='部门id')
    parent_id = Column(BIGINT(20), server_default=text("'0'"), comment='父部门id')
    ancestors = Column(String(50), server_default=text("''"), comment='祖级列表')
    dept_name = Column(String(30), server_default=text("''"), comment='部门名称')
    dept_code = Column(VARCHAR(50), comment='部门编号')
    order_num = Column(INTEGER(4), server_default=text("'0'"), comment='显示顺序')
    leader = Column(String(20), comment='负责人')
    phone = Column(String(11), comment='联系电话')
    email = Column(String(50), comment='邮箱')
    status = Column(CHAR(1), server_default=text("'0'"), comment='部门状态（0正常 1停用）')
    del_flag = Column(CHAR(1), server_default=text("'0'"), comment='删除标志（0代表存在 2代表删除）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')


class SysDictDatum(Base):
    __tablename__ = 'sys_dict_data'
    __table_args__ = {'comment': '字典数据表'}

    dict_code = Column(BIGINT(20), primary_key=True, comment='字典编码')
    dict_sort = Column(INTEGER(4), server_default=text("'0'"), comment='字典排序')
    dict_label = Column(String(100), server_default=text("''"), comment='字典标签')
    dict_value = Column(String(100), server_default=text("''"), comment='字典键值')
    dict_type = Column(String(100), server_default=text("''"), comment='字典类型')
    css_class = Column(String(100), comment='样式属性（其他样式扩展）')
    list_class = Column(String(100), comment='表格回显样式')
    is_default = Column(CHAR(1), server_default=text("'N'"), comment='是否默认（Y是 N否）')
    status = Column(CHAR(1), server_default=text("'0'"), comment='状态（0正常 1停用）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), comment='备注')


class SysDictType(Base):
    __tablename__ = 'sys_dict_type'
    __table_args__ = {'comment': '字典类型表'}

    dict_id = Column(BIGINT(20), primary_key=True, comment='字典主键')
    dict_name = Column(String(100), server_default=text("''"), comment='字典名称')
    dict_type = Column(String(100), unique=True, server_default=text("''"), comment='字典类型')
    status = Column(CHAR(1), server_default=text("'0'"), comment='状态（0正常 1停用）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), comment='备注')


class SysJob(Base):
    __tablename__ = 'sys_job'
    __table_args__ = {'comment': '定时任务调度表'}

    job_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='任务ID')
    job_name = Column(String(64), primary_key=True, nullable=False, server_default=text("''"), comment='任务名称')
    job_group = Column(String(64), primary_key=True, nullable=False, server_default=text("'DEFAULT'"), comment='任务组名')
    invoke_target = Column(String(500), nullable=False, comment='调用目标字符串')
    cron_expression = Column(String(255), server_default=text("''"), comment='cron执行表达式')
    misfire_policy = Column(String(20), server_default=text("'3'"), comment='计划执行错误策略（1立即执行 2执行一次 3放弃执行）')
    concurrent = Column(CHAR(1), server_default=text("'1'"), comment='是否并发执行（0允许 1禁止）')
    status = Column(CHAR(1), server_default=text("'0'"), comment='状态（0正常 1暂停）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), server_default=text("''"), comment='备注信息')


class SysJobLog(Base):
    __tablename__ = 'sys_job_log'
    __table_args__ = {'comment': '定时任务调度日志表'}

    job_log_id = Column(BIGINT(20), primary_key=True, comment='任务日志ID')
    job_name = Column(String(64), nullable=False, comment='任务名称')
    job_group = Column(String(64), nullable=False, comment='任务组名')
    invoke_target = Column(String(500), nullable=False, comment='调用目标字符串')
    job_message = Column(String(500), comment='日志信息')
    status = Column(CHAR(1), server_default=text("'0'"), comment='执行状态（0正常 1失败）')
    exception_info = Column(String(2000), server_default=text("''"), comment='异常信息')
    create_time = Column(DateTime, comment='创建时间')


class SysMenu(Base):
    __tablename__ = 'sys_menu'
    __table_args__ = {'comment': '菜单权限表'}

    menu_id = Column(BIGINT(20), primary_key=True, comment='菜单ID')
    menu_name = Column(String(50), nullable=False, comment='菜单名称')
    parent_id = Column(BIGINT(20), server_default=text("'0'"), comment='父菜单ID')
    order_num = Column(INTEGER(4), server_default=text("'0'"), comment='显示顺序')
    path = Column(String(200), server_default=text("''"), comment='路由地址')
    component = Column(String(255), comment='组件路径')
    query = Column(String(255), comment='路由参数')
    is_frame = Column(INTEGER(1), server_default=text("'1'"), comment='是否为外链（0是 1否）')
    is_cache = Column(INTEGER(1), server_default=text("'0'"), comment='是否缓存（0缓存 1不缓存）')
    menu_type = Column(CHAR(1), server_default=text("''"), comment='菜单类型（M目录 C菜单 F按钮）')
    visible = Column(CHAR(1), server_default=text("'0'"), comment='菜单状态（0显示 1隐藏）')
    status = Column(CHAR(1), server_default=text("'0'"), comment='菜单状态（0正常 1停用）')
    perms = Column(String(100), comment='权限标识')
    icon = Column(String(100), server_default=text("'#'"), comment='菜单图标')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), server_default=text("''"), comment='备注')


class SysNotice(Base):
    __tablename__ = 'sys_notice'
    __table_args__ = {'comment': '通知公告表'}

    notice_id = Column(BIGINT(4), primary_key=True, comment='公告ID')
    notice_title = Column(String(50), nullable=False, comment='公告标题')
    notice_type = Column(CHAR(1), nullable=False, server_default=text("'2'"), comment='公告类型（1通知 2公告）')
    notice_content = Column(String(500), comment='公告内容')
    status = Column(CHAR(1), server_default=text("'0'"), comment='公告状态（0正常 1关闭）')
    time_limit = Column(DateTime, comment='过期时间')
    create_id = Column(BIGINT(20), comment='发布者id')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(255), comment='备注')


class SysNoticeRead(Base):
    __tablename__ = 'sys_notice_read'

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20))
    notice_id = Column(INTEGER(11))
    is_read = Column(TINYINT(1), comment='1已读 0未读')
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class SysPost(Base):
    __tablename__ = 'sys_post'
    __table_args__ = {'comment': '岗位信息表'}

    post_id = Column(BIGINT(20), primary_key=True, comment='岗位ID')
    post_code = Column(String(64), nullable=False, comment='岗位编码')
    post_name = Column(String(50), nullable=False, comment='岗位名称')
    post_sort = Column(INTEGER(4), nullable=False, comment='显示顺序')
    status = Column(CHAR(1), nullable=False, comment='状态（0正常 1停用）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), comment='备注')


class SysRole(Base):
    __tablename__ = 'sys_role'
    __table_args__ = {'comment': '角色信息表'}

    role_id = Column(BIGINT(20), primary_key=True, comment='角色ID')
    role_name = Column(String(30), nullable=False, comment='角色名称')
    role_key = Column(String(100), nullable=False, comment='角色权限字符串')
    role_sort = Column(INTEGER(4), nullable=False, comment='显示顺序')
    data_scope = Column(CHAR(1), server_default=text("'1'"), comment='数据范围（1：全部数据权限 2：自定数据权限 3：本部门数据权限 4：本部门及以下数据权限）')
    menu_check_strictly = Column(TINYINT(1), server_default=text("'1'"), comment='菜单树选择项是否关联显示')
    dept_check_strictly = Column(TINYINT(1), server_default=text("'1'"), comment='部门树选择项是否关联显示')
    status = Column(CHAR(1), nullable=False, comment='角色状态（0正常 1停用）')
    del_flag = Column(CHAR(1), server_default=text("'0'"), comment='删除标志（0代表存在 2代表删除）')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(VARCHAR(500), comment='角色概述')


class SysRoleDept(Base):
    __tablename__ = 'sys_role_dept'
    __table_args__ = {'comment': '角色和部门关联表'}

    role_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='角色ID')
    dept_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='部门ID')


class SysRoleMenu(Base):
    __tablename__ = 'sys_role_menu'
    __table_args__ = {'comment': '角色和菜单关联表'}

    role_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='角色ID')
    menu_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='菜单ID')


class SysUser(Base):
    __tablename__ = 'sys_user'
    __table_args__ = {'comment': '用户信息表'}

    user_id = Column(BIGINT(20), primary_key=True, comment='用户ID')
    dept_id = Column(BIGINT(20), comment='部门ID')
    name = Column(VARCHAR(30), comment='姓名')
    user_name = Column(String(30), nullable=False, comment='用户账号')
    nick_name = Column(VARCHAR(30), comment='用户昵称')
    user_type = Column(String(2), server_default=text("'00'"), comment='用户类型（00系统用户）')
    email = Column(String(50), server_default=text("''"), comment='用户邮箱')
    phonenumber = Column(String(11), server_default=text("''"), comment='手机号码')
    sex = Column(CHAR(1), server_default=text("'0'"), comment='用户性别（0未知  1男  2女）')
    avatar = Column(String(100), server_default=text("''"), comment='头像地址')
    id_card = Column(VARCHAR(18), comment='身份证号')
    password = Column(String(100), server_default=text("''"), comment='密码')
    effective_time = Column(Date, comment='有效日期')
    status = Column(CHAR(1), server_default=text("'0'"), comment='帐号状态（0正常 1停用）')
    level = Column(TINYINT(1), comment='权限等级  1高 2中 3低 ')
    del_flag = Column(CHAR(1), server_default=text("'0'"), comment='删除标志（0代表存在 1代表删除）')
    login_ip = Column(String(128), server_default=text("''"), comment='最后登录IP')
    login_date = Column(DateTime, comment='最后登录时间')
    create_by = Column(String(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(500), comment='备注')
    is_online = Column(TINYINT(1), comment='1在线 0不在线')


class SysUserPost(Base):
    __tablename__ = 'sys_user_post'
    __table_args__ = {'comment': '用户与岗位关联表'}

    user_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='用户ID')
    post_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='岗位ID')


class SysUserRole(Base):
    __tablename__ = 'sys_user_role'
    __table_args__ = {'comment': '用户和角色关联表'}

    user_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='用户ID')
    role_id = Column(BIGINT(20), primary_key=True, nullable=False, comment='角色ID')


class VedioTurningConfig(Base):
    __tablename__ = 'vedio_turning_config'
    __table_args__ = {'comment': '摄像头轮巡设置'}

    id = Column(BIGINT(20), primary_key=True, comment='编号')
    group_name = Column(String(50, 'utf8mb4_general_ci'), comment='组名')
    ttl = Column(INTEGER(10), comment='切换时间，单位：秒')
    split_type = Column(VARCHAR(50), server_default=text("'9'"), comment='分屏模式 1、2、3、4、6、9、16分屏，默认 9')
    device_codes = Column(TEXT, comment='关联设备编码集合，格式：[{"deviceCode":"123"}, {"deviceCode":"124"}]')
    create_by = Column(String(64, 'utf8mb4_general_ci'), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64, 'utf8mb4_general_ci'), comment='更新人')
    update_time = Column(DateTime, comment='更细时间')
    remark = Column(String(200, 'utf8mb4_general_ci'), comment='备注')


class XcBlacklist(Base):
    __tablename__ = 'xc_blacklist'
    __table_args__ = {'comment': '黑名单表-使用'}

    id = Column(INTEGER(11), primary_key=True)
    data_type = Column(INTEGER(10), comment='数据类型   1 车牌 2 imsi 3 imei 4 mac ')
    content = Column(VARCHAR(50), comment='数据类型对应的内容')
    is_enable_create_archive = Column(INTEGER(11), comment='是否允许建档,默认允许建档；0不允许 1允许')
    record_reason = Column(VARCHAR(500), comment='登记原因')
    create_time = Column(DateTime, comment='登记时间')
    create_by = Column(VARCHAR(64), comment='创建人')
    update_time = Column(DateTime, comment='修改时间')
    update_by = Column(VARCHAR(64), comment='修改人')
    remark = Column(String(200, 'utf8mb4_general_ci'), comment='备注')


class XcDeviceBase(Base):
    __tablename__ = 'xc_device_base'
    __table_args__ = {'comment': '设备的基础类表'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(50), server_default=text("''"), comment='设备名称')
    device_code = Column(VARCHAR(20), nullable=False, server_default=text("''"), comment='设备编号')
    device_model = Column(VARCHAR(50), server_default=text("''"), comment='设备型号')
    provider = Column(VARCHAR(50), server_default=text("''"), comment='设备供应商')
    type = Column(INTEGER(2), nullable=False, comment='设备类型 对应类型见数据字典')
    camera_type = Column(INTEGER(2), comment='摄像头类型 0非摄像机 1远距离光电 2高清激光球机 3全景网络摄像机 4热成像网络摄像机 5高清球机 6高清枪机 7人脸识别 8微卡口单元 9卡口')
    business_function = Column(VARCHAR(200), comment='业务功能项 1-视频 2-视频联动 3-人脸识别 4-车辆识别 5-船舶结构化 6-视频告警 以半角逗号隔开')
    ip = Column(VARCHAR(30), server_default=text("''"), comment='设备ip')
    port = Column(INTEGER(5), comment='端口')
    user_name = Column(VARCHAR(30), comment='摄像头登录用户名')
    password = Column(VARCHAR(64), comment='摄像头登录密码')
    power = Column(INTEGER(11), comment='功率  1微功率  2小功率 3大功率')
    longitude = Column(Float(asdecimal=True), comment='经度')
    latitude = Column(Float(asdecimal=True), comment='纬度')
    addr = Column(VARCHAR(200), server_default=text("''"), comment='设备地址')
    area_code = Column(VARCHAR(12), server_default=text("''"), comment='区域编码')
    site_id = Column(BIGINT(20), comment='站点id')
    shaft_code = Column(VARCHAR(20), server_default=text("''"), comment='杆体编号')
    status = Column(INTEGER(1), server_default=text("'0'"), comment='设备状态 在线为1 故障为0')
    install_high = Column(INTEGER(10), comment='安装高度')
    horizontal1 = Column(Float(5), comment='水平视角1')
    horizontal2 = Column(Float(5), comment='水平视角2')
    cover_raduis = Column(INTEGER(11), comment='覆盖半径')
    threshold = Column(INTEGER(1), comment='设备阈值 -1表示自动设置阈值')
    threshold_type = Column(INTEGER(1), comment='异常阈值 1自动2手动')
    vadio_together_id = Column(BIGINT(20), comment='视频联动设备id')
    gps_code = Column(VARCHAR(50), comment='GPS编号')
    del_flag = Column(INTEGER(1), server_default=text("'0'"), comment='是否删除 0未删除  1删除')
    comment = Column(VARCHAR(200), server_default=text("''"), comment='设备描述')
    create_by = Column(VARCHAR(64), server_default=text("''"), comment='创建者')
    create_time = Column(DateTime)
    update_by = Column(VARCHAR(64), server_default=text("''"), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(100, 'utf8mb4_bin'), server_default=text("''"), comment='备注')


class XcDeviceBusinessFunction(Base):
    __tablename__ = 'xc_device_business_function'

    id = Column(BIGINT(20), primary_key=True)
    device_id = Column(BIGINT(20))
    business_function = Column(INTEGER(2), comment='业务功能 business_function 1 视频 2 视频联动 3 人脸识别 4 车辆识别 5 船舶结构化')
    create_time = Column(DateTime)


class XcDeviceChannel(Base):
    __tablename__ = 'xc_device_channel'

    id = Column(BIGINT(20), primary_key=True)
    device_id = Column(BIGINT(20), comment='设备id')
    channel_no = Column(VARCHAR(50), comment='通道编号')
    ip = Column(String(30, 'utf8mb4_general_ci'), comment='ip')
    port = Column(INTEGER(5), comment='port')
    account = Column(String(50, 'utf8mb4_general_ci'), comment='账号')
    password = Column(String(255, 'utf8mb4_general_ci'), comment='密码')
    vadio_type = Column(TINYINT(1), comment='视频类型 1可见光  2红外线   3全景  4细节')
    sort = Column(INTEGER(2), comment='排序号')
    del_flag = Column(TINYINT(1), server_default=text("'0'"), comment='是否删除 1-是  0-非')
    create_time = Column(DateTime)
    create_by = Column(String(50, 'utf8mb4_general_ci'))
    update_time = Column(DateTime)
    update_by = Column(String(50, 'utf8mb4_general_ci'))
    remark = Column(VARCHAR(255), comment='备注')


class XcDeviceCollect(Base):
    __tablename__ = 'xc_device_collect'

    id = Column(BIGINT(20), primary_key=True)
    device_id = Column(BIGINT(20), comment='设备id')
    today_collect_num = Column(INTEGER(11), comment='今日采集数量')
    prev_month_rate = Column(Float, comment='同比上月')
    yesterday_rate = Column(Float, comment='昨天')
    month_argv = Column(Float, comment='月均值')
    exception_value = Column(INTEGER(11), comment='异常阀值')
    collect_date = Column(CHAR(10), comment='统计日期')
    create_time = Column(DateTime, comment='创建时间')
    update_time = Column(DateTime, comment='更新时间')


class XcDeviceCollectException(Base):
    __tablename__ = 'xc_device_collect_exception'

    id = Column(INTEGER(10), primary_key=True)
    device_name = Column(VARCHAR(255), comment='设备名')
    device_code = Column(VARCHAR(50), comment='设备编码')
    device_type = Column(INTEGER(11), comment='设备类型')
    exception_type = Column(INTEGER(11), comment='异常类型 1无采集数据上报 2设备故障 3数据接收服务故障 4:1400无数据推送 51400数据推送延迟 6阿里人脸识别故障 7阿里人脸识别延迟 8设备位置发生变化')
    begin_time = Column(DateTime)
    end_time = Column(DateTime)
    exception_content = Column(VARCHAR(200), comment='异常内容')
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class XcDeviceDeptRelation(Base):
    __tablename__ = 'xc_device_dept_relation'
    __table_args__ = {'comment': '设备分配表，xc_device_base与sys_dept关联表'}

    id = Column(INTEGER(10), primary_key=True)
    device_bases_id = Column(BIGINT(20), index=True, comment='对应device_base表的id')
    dept_id = Column(VARCHAR(32), index=True, comment='部门id')
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class XcDeviceSite(Base):
    __tablename__ = 'xc_device_site'
    __table_args__ = {'comment': '设备站点信息表'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(50), nullable=False, server_default=text("''"), comment='站点名称')
    site_code = Column(VARCHAR(10), nullable=False, server_default=text("''"), comment='站点编码')
    type = Column(TINYINT(3), server_default=text("'1'"), comment='站点类型 1固定站点 2移动站点')
    del_flag = Column(INTEGER(1), comment='删除状态 0未删除 1删除')
    addr = Column(VARCHAR(255), server_default=text("''"), comment='站点地址')
    area = Column(VARCHAR(255), server_default=text("''"), comment='站点区域')
    latitude = Column(Float(9, True), server_default=text("'0.000000'"), comment='站点 纬度')
    longitude = Column(Float(9, True), server_default=text("'0.000000'"), comment='站点 经度')
    radius = Column(INTEGER(11))
    shaft_code = Column(VARCHAR(255), server_default=text("''"), comment='杆体号')
    graph = Column(TEXT, comment='范围')
    create_time = Column(DateTime, comment='创建时间')
    create_by = Column(VARCHAR(64), comment='创建者')
    update_time = Column(DateTime, comment='更新时间')
    update_by = Column(VARCHAR(64), comment='更新者')
    remark = Column(String(200, 'utf8mb4_bin'), comment='备注')
    delet_status = Column(TINYINT(3), comment='删除状态 0未删除 1删除')


class XcLabel(Base):
    __tablename__ = 'xc_label'
    __table_args__ = {'comment': '标签信息表'}

    id = Column(BIGINT(20), primary_key=True, comment='标签编号')
    label_name = Column(VARCHAR(50), comment='标签名称')
    type = Column(TINYINT(2), nullable=False, comment='标签类型（1人员档案 2车辆档案 3手机档案 4船舶档案 5雷达目标 6船舶布控 7建模风险类别 8案件类别 9场所类型 10人员布控 11便签类别 12预案类别）')
    is_auto = Column(CHAR(1), nullable=False, server_default=text("'0'"), comment='自动打标签 0 手动(默认) 1 自动')
    del_flag = Column(TINYINT(2), server_default=text("'0'"), comment='删除标志（0代表存在 1代表删除）')
    mark = Column(String(30, 'utf8mb4_general_ci'), comment='记号，标签来源')
    create_by = Column(VARCHAR(64), comment='创建者')
    create_time = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    update_by = Column(VARCHAR(64), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(200, 'utf8mb4_general_ci'), comment='备注')


class XcMark(Base):
    __tablename__ = 'xc_mark'
    __table_args__ = {'comment': '标记点信息'}

    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(30, 'utf8mb4_general_ci'), comment='标记名称')
    longitude = Column(Float(asdecimal=True), comment='经度')
    latitude = Column(Float(asdecimal=True), comment='纬度')
    del_flag = Column(CHAR(1), server_default=text("'0'"), comment='删除标记 1-删除 0-未删除')
    create_by = Column(String(64, 'utf8mb4_general_ci'), comment='创建者')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64, 'utf8mb4_general_ci'), comment='更新者')
    update_time = Column(DateTime, comment='更新时间')
    remark = Column(String(200, 'utf8mb4_general_ci'), comment='备注')


class XcMmsiCountry(Base):
    __tablename__ = 'xc_mmsi_country'
    __table_args__ = {'comment': 'mmsi的前三位，对应的国籍'}

    id = Column(BIGINT(20), primary_key=True, comment='编号')
    country_code = Column(VARCHAR(50), comment='国籍代码')
    country_name = Column(VARCHAR(80), comment='国籍名称')
    mmsi = Column(VARCHAR(3), comment='mmsi前3位')


class XcMonitorArea(Base):
    __tablename__ = 'xc_monitor_area'
    __table_args__ = {'comment': '区域记录表'}

    id = Column(BIGINT(20), primary_key=True, comment='主键id')
    name = Column(String(20, 'utf8mb4_general_ci'), nullable=False, comment='区域名称')
    graph = Column(Text(collation='utf8mb4_general_ci'), nullable=False, comment='WKT标记语言图形字符串')
    type = Column(CHAR(1), comment='图形类型 1-线 2-圆形 3-矩形 4-多边形')
    graph_json = Column(JSON, comment='图形json 大数据使用')
    device_codes = Column(Text(collation='utf8mb4_general_ci'), comment='当前区域拥有设备 保存deviceCode')
    device_ids = Column(Text(collation='utf8mb4_general_ci'), comment='当前区域拥有设备 保存id')
    del_flag = Column(CHAR(1), nullable=False, server_default=text("'0'"), comment='删除标记 0-未删除 1-已删除')
    control_type_id = Column(CHAR(1), comment='布控类型(1:船舶布控, 2: 人员布控)')
    create_by = Column(String(64, 'utf8mb4_general_ci'), comment='创建人')
    create_time = Column(DateTime, comment='创建时间')
    update_by = Column(String(64, 'utf8mb4_general_ci'), comment='修改人')
    update_time = Column(DateTime, comment='修改时间')
    remark = Column(String(500, 'utf8mb4_general_ci'), comment='预留字段')


t_xc_monitor_area_relation = Table(
    'xc_monitor_area_relation', metadata,
    Column('business_id', String(64, 'utf8mb4_general_ci'), comment='业务ID'),
    Column('business_type', CHAR(2), comment='业务类型 01:布控预警 03:智慧建模 09:研判分析 10:智慧建模事件 11:研判分析事件'),
    Column('area_id', BIGINT(20), comment='区域id'),
    Index('business_id_business_type_area_id', 'business_id', 'business_type', 'area_id'),
    comment='布控区域关联表'
)


class XcMynote(Base):
    __tablename__ = 'xc_mynote'
    __table_args__ = {'comment': '便签表'}

    id = Column(INTEGER(11), primary_key=True, comment='主键')
    note_title = Column(VARCHAR(32), comment='标题、模块名称、或新增便签')
    note_type = Column(INTEGER(11), nullable=False, comment='类型  0自建便签 1技战法 2研判 3智搜')
    note_type_id = Column(BIGINT(11), comment='类型id 对应xc_label表的id')
    task_name = Column(VARCHAR(32), comment='战法，研判--任务名字 ， 智搜--侦码数据/车牌数据/人脸数据')
    result_num = Column(INTEGER(11), comment='结果条数（默认0条，技战法，研判，智搜任务实际结果数）')
    note_content = Column(TEXT, comment='便签内容自建任务写入')
    create_time = Column(DateTime, nullable=False, comment='创建时间')
    create_uid = Column(VARCHAR(32), nullable=False, comment='创建人id（便签所属者）')
    note_desc = Column(VARCHAR(128), comment='便签备注')
    business_table_id = Column(BIGINT(20), comment='业务表关联id 布控审批对应布控表id')


class XcTaskApproval(Base):
    __tablename__ = 'xc_task_approval'
    __table_args__ = {'comment': '布控审批表'}

    id = Column(INTEGER(10), primary_key=True, comment='主键')
    type = Column(INTEGER(11), nullable=False, comment='类型 0布控审批 1续控  2撤控 号码翻译')
    business_table_id = Column(BIGINT(20), comment='业务表关联id 布控审批对应布控表id')
    monitor_type = Column(TINYINT(4), comment='布控类型 针对布控的审批 0表示非布控业务 1: 船舶布控, 2:人员布控 ')
    task_no = Column(VARCHAR(30), nullable=False, comment='任务编号 如果是布控审批 对应布控id')
    task_name = Column(VARCHAR(255), nullable=False, comment='任务名称')
    task_desc = Column(VARCHAR(255), comment='任务内容描述, 申请理由')
    apply_uid = Column(VARCHAR(32), comment='申请人id')
    apply_name = Column(VARCHAR(50), comment='申请人昵称')
    status = Column(INTEGER(11), nullable=False, comment='状态0初始待审批 1审批通过 2审批不通过 3转审批')
    approval_uid = Column(VARCHAR(32), nullable=False, comment='审批人id（指定审批人时产生）')
    approval_dept_id = Column(BIGINT(20), comment='审批部门id')
    approval_name = Column(VARCHAR(50), comment='审批人昵称')
    approval_desc = Column(VARCHAR(255), comment='审批内容说明')
    approval_time = Column(DateTime, comment='审批时间')
    parent_id = Column(INTEGER(11), server_default=text("'0'"), comment='被转审批父级id')
    is_del = Column(TINYINT(1), server_default=text("'0'"), comment='是否删除 0未删除  1删除')
    create_by = Column(VARCHAR(32), comment='创建人账号')
    create_time = Column(DateTime, nullable=False, comment='创建时间')


class XcTaskApprovalRecord(Base):
    __tablename__ = 'xc_task_approval_record'
    __table_args__ = {'comment': '个人工作台审批操作记录表'}

    id = Column(BIGINT(20), primary_key=True, comment='编号')
    task_id = Column(BIGINT(20), nullable=False, comment='审批任务id')
    operate_type = Column(TINYINT(4), comment='操作事项 1.提交申请  2.处理申请')
    status = Column(TINYINT(1), comment='处理意见 1同意 2不同意 3转审')
    operate_id = Column(VARCHAR(32), comment='操作人id')
    operate_name = Column(VARCHAR(50), comment='操作人昵称')
    operate_desc = Column(VARCHAR(100), comment='备注')
    create_time = Column(DateTime, comment='操作时间')


class XcWhitelist(Base):
    __tablename__ = 'xc_whitelist'
    __table_args__ = {'comment': '白名单表-使用'}

    id = Column(INTEGER(11), primary_key=True)
    data_type = Column(String(20, 'utf8mb4_general_ci'), comment='数据类型')
    content = Column(VARCHAR(50), comment='数据类型对应的内容')
    is_enable_create_archive = Column(INTEGER(11), comment='是否允许建档,默认允许建档；0不允许 1允许')
    record_reason = Column(VARCHAR(500), comment='登记原因')
    create_time = Column(DateTime, comment='登记时间')
    create_by = Column(VARCHAR(64), comment='创建人')
    update_time = Column(DateTime, comment='修改时间')
    update_by = Column(VARCHAR(64), comment='修改人')
    remark = Column(String(200, 'utf8mb4_general_ci'), comment='备注')


class QRTZTRIGGER(Base):
    __tablename__ = 'QRTZ_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'job_name', 'job_group'], ['QRTZ_JOB_DETAILS.sched_name', 'QRTZ_JOB_DETAILS.job_name', 'QRTZ_JOB_DETAILS.job_group']),
        Index('sched_name', 'sched_name', 'job_name', 'job_group'),
        {'comment': '触发器详细信息表'}
    )

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    trigger_name = Column(String(200), primary_key=True, nullable=False, comment='触发器的名字')
    trigger_group = Column(String(200), primary_key=True, nullable=False, comment='触发器所属组的名字')
    job_name = Column(String(200), nullable=False, comment='qrtz_job_details表job_name的外键')
    job_group = Column(String(200), nullable=False, comment='qrtz_job_details表job_group的外键')
    description = Column(String(250), comment='相关介绍')
    next_fire_time = Column(BIGINT(13), comment='上一次触发时间（毫秒）')
    prev_fire_time = Column(BIGINT(13), comment='下一次触发时间（默认为-1表示不触发）')
    priority = Column(INTEGER(11), comment='优先级')
    trigger_state = Column(String(16), nullable=False, comment='触发器状态')
    trigger_type = Column(String(8), nullable=False, comment='触发器的类型')
    start_time = Column(BIGINT(13), nullable=False, comment='开始时间')
    end_time = Column(BIGINT(13), comment='结束时间')
    calendar_name = Column(String(200), comment='日程表名称')
    misfire_instr = Column(SMALLINT(2), comment='补偿执行的策略')
    job_data = Column(LargeBinary, comment='存放持久化job对象')

    QRTZ_JOB_DETAIL = relationship('QRTZJOBDETAIL')


class QRTZBLOBTRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_BLOB_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['QRTZ_TRIGGERS.sched_name', 'QRTZ_TRIGGERS.trigger_name', 'QRTZ_TRIGGERS.trigger_group']),
        {'comment': 'Blob类型的触发器表'}
    )

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    trigger_name = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_name的外键')
    trigger_group = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_group的外键')
    blob_data = Column(LargeBinary, comment='存放持久化Trigger对象')


class QRTZCRONTRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_CRON_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['QRTZ_TRIGGERS.sched_name', 'QRTZ_TRIGGERS.trigger_name', 'QRTZ_TRIGGERS.trigger_group']),
        {'comment': 'Cron类型的触发器表'}
    )

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    trigger_name = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_name的外键')
    trigger_group = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_group的外键')
    cron_expression = Column(String(200), nullable=False, comment='cron表达式')
    time_zone_id = Column(String(80), comment='时区')


class QRTZSIMPLETRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_SIMPLE_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['QRTZ_TRIGGERS.sched_name', 'QRTZ_TRIGGERS.trigger_name', 'QRTZ_TRIGGERS.trigger_group']),
        {'comment': '简单触发器的信息表'}
    )

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    trigger_name = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_name的外键')
    trigger_group = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_group的外键')
    repeat_count = Column(BIGINT(7), nullable=False, comment='重复的次数统计')
    repeat_interval = Column(BIGINT(12), nullable=False, comment='重复的间隔时间')
    times_triggered = Column(BIGINT(10), nullable=False, comment='已经触发的次数')


class QRTZSIMPROPTRIGGER(QRTZTRIGGER):
    __tablename__ = 'QRTZ_SIMPROP_TRIGGERS'
    __table_args__ = (
        ForeignKeyConstraint(['sched_name', 'trigger_name', 'trigger_group'], ['QRTZ_TRIGGERS.sched_name', 'QRTZ_TRIGGERS.trigger_name', 'QRTZ_TRIGGERS.trigger_group']),
        {'comment': '同步机制的行锁表'}
    )

    sched_name = Column(String(120), primary_key=True, nullable=False, comment='调度名称')
    trigger_name = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_name的外键')
    trigger_group = Column(String(200), primary_key=True, nullable=False, comment='qrtz_triggers表trigger_group的外键')
    str_prop_1 = Column(String(512), comment='String类型的trigger的第一个参数')
    str_prop_2 = Column(String(512), comment='String类型的trigger的第二个参数')
    str_prop_3 = Column(String(512), comment='String类型的trigger的第三个参数')
    int_prop_1 = Column(INTEGER(11), comment='int类型的trigger的第一个参数')
    int_prop_2 = Column(INTEGER(11), comment='int类型的trigger的第二个参数')
    long_prop_1 = Column(BIGINT(20), comment='long类型的trigger的第一个参数')
    long_prop_2 = Column(BIGINT(20), comment='long类型的trigger的第二个参数')
    dec_prop_1 = Column(DECIMAL(13, 4), comment='decimal类型的trigger的第一个参数')
    dec_prop_2 = Column(DECIMAL(13, 4), comment='decimal类型的trigger的第二个参数')
    bool_prop_1 = Column(String(1), comment='Boolean类型的trigger的第一个参数')
    bool_prop_2 = Column(String(1), comment='Boolean类型的trigger的第二个参数')
