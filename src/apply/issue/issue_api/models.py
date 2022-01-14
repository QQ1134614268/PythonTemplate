# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, text
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class AuthItem(Base):
    __tablename__ = 'auth_item'

    en_name = Column(VARCHAR(255), primary_key=True, comment='权限英文名称')
    name = Column(VARCHAR(255), nullable=False, comment='权限名称')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')


class AuthLoginLog(Base):
    __tablename__ = 'auth_login_log'

    id = Column(Integer, primary_key=True, comment='ID')
    user_id = Column(Integer, nullable=False, unique=True, comment='用户ID')
    failure_count = Column(Integer, comment='登录失败次数')
    created_at = Column(DateTime, comment='更新时间')


class AuthOrg(Base):
    __tablename__ = 'auth_org'

    id = Column(Integer, primary_key=True, comment='ID')
    name = Column(VARCHAR(255), nullable=False, comment='组织名称')
    parent_id = Column(Integer, comment='父级ID')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')
    code = Column(VARCHAR(255), comment='组织代码')
    type = Column(VARCHAR(1), comment='组织类型：0-总部，1-分公司，2-营业部')
    data_source = Column(VARCHAR(1), comment='数据来源：0-同步，1-自定义')
    status = Column(VARCHAR(1), nullable=False, server_default=text("'1'"), comment='状态（0-禁用，1-启用）')


class AuthRandomCode(Base):
    __tablename__ = 'auth_random_code'

    code = Column(VARCHAR(255), primary_key=True)
    key = Column(VARCHAR(255), server_default=text("''"))
    expiredDate = Column(DateTime, comment='过期时间')


class AuthRole(Base):
    __tablename__ = 'auth_role'

    id = Column(Integer, primary_key=True, comment='ID')
    name = Column(VARCHAR(255), nullable=False, comment='角色名称')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')
    type = Column(VARCHAR(1), comment='角色分类：0-总部，1-分公司，2-营业部')


class AuthService(Base):
    __tablename__ = 'auth_services'

    name = Column(VARCHAR(255), primary_key=True, comment='服务名称')
    ip_port = Column(VARCHAR(255), nullable=False, comment='服务地址')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')
    header = Column(JSON, comment='请求头设置')


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True, comment='ID')
    name = Column(VARCHAR(255), nullable=False, unique=True, comment='用户名')
    nick_name = Column(VARCHAR(255), nullable=False, comment='昵称')
    access_token = Column(VARCHAR(255), unique=True, comment='令牌')
    password_hash = Column(VARCHAR(255), nullable=False, comment='密码（哈希）')
    email = Column(VARCHAR(255), comment='邮箱')
    mobile_phone = Column(VARCHAR(255), comment='手机号码')
    status = Column(VARCHAR(1), nullable=False, server_default=text("'1'"), comment='状态（0-禁用，1-启用）')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')


class AuthApiLog(Base):
    __tablename__ = 'auth_api_log'

    id = Column(Integer, primary_key=True, comment='ID')
    api = Column(VARCHAR(255), comment='API地址')
    method = Column(VARCHAR(255), comment='请求方式')
    created_by = Column(ForeignKey('auth_user.id'), index=True, comment='用户ID')
    created_at = Column(DateTime, comment='创建时间')

    auth_user = relationship('AuthUser')


class AuthMenu(Base):
    __tablename__ = 'auth_menu'

    id = Column(Integer, primary_key=True, comment='ID')
    name = Column(VARCHAR(255), nullable=False, comment='菜单名称')
    parent_id = Column(Integer, comment='父级ID')
    item_en_name = Column(ForeignKey('auth_item.en_name'), index=True, comment='权限英文名')
    # serial_no = Column(Integer, comment='序号')
    updated_at = Column(DateTime, comment='更新时间')
    created_at = Column(DateTime, comment='创建时间')

    auth_item = relationship('AuthItem')


class AuthOrgUser(Base):
    __tablename__ = 'auth_org_user'

    org_id = Column(ForeignKey('auth_org.id'), primary_key=True, nullable=False, comment='组织ID')
    user_id = Column(ForeignKey('auth_user.id'), primary_key=True, nullable=False, index=True, comment='用户ID')
    created_at = Column(DateTime, comment='创建时间')

    org = relationship('AuthOrg')
    user = relationship('AuthUser')


class AuthRoleItem(Base):
    __tablename__ = 'auth_role_item'

    item_en_name = Column(ForeignKey('auth_item.en_name'), primary_key=True, nullable=False, comment='权限英文名')
    role_id = Column(ForeignKey('auth_role.id'), primary_key=True, nullable=False, index=True, comment='角色ID')
    created_at = Column(DateTime, comment='创建时间')

    auth_item = relationship('AuthItem')
    role = relationship('AuthRole')


class AuthUserPwdChangeLog(Base):
    __tablename__ = 'auth_user_pwd_change_log'

    id = Column(Integer, primary_key=True, nullable=False, comment='ID')
    user_id = Column(ForeignKey('auth_user.id'), primary_key=True, nullable=False, index=True, comment='用户ID')
    created_at = Column(DateTime, comment='创建时间')

    user = relationship('AuthUser')


class AuthUserRole(Base):
    __tablename__ = 'auth_user_role'

    user_id = Column(ForeignKey('auth_user.id'), primary_key=True, nullable=False, comment='用户ID')
    role_id = Column(ForeignKey('auth_role.id'), primary_key=True, nullable=False, index=True, comment='角色ID')
    created_at = Column(DateTime, comment='创建时间')

    role = relationship('AuthRole')
    user = relationship('AuthUser')
