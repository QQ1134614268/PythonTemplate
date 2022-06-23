from sqlalchemy import Column, Enum, MetaData, String, Text, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, MEDIUMTEXT
from sqlalchemy.orm import declarative_base

metadata = MetaData()

Base = declarative_base()


class MysqlColumns(Base):
    __bind_key__ = 'information_schema'
    __tablename__ = 'columns'
    metadata = MetaData()
    __table_args__ = {
        'schema': 'information_schema'
    }
    # __mapper_args__ = {
    #     'primary_key': []
    # }
    TABLE_CATALOG = Column('TABLE_CATALOG', String(64))
    TABLE_SCHEMA = Column('TABLE_SCHEMA', String(64))
    TABLE_NAME = Column('TABLE_NAME', String(64))
    COLUMN_NAME = Column('COLUMN_NAME', String(64))
    ORDINAL_POSITION = Column('ORDINAL_POSITION', INTEGER(10))
    COLUMN_DEFAULT = Column('COLUMN_DEFAULT', Text)
    IS_NULLABLE = Column('IS_NULLABLE', String(3))
    DATA_TYPE = Column('DATA_TYPE', LONGTEXT)
    CHARACTER_MAXIMUM_LENGTH = Column('CHARACTER_MAXIMUM_LENGTH', BIGINT(21))
    CHARACTER_OCTET_LENGTH = Column('CHARACTER_OCTET_LENGTH', BIGINT(21))
    NUMERIC_PRECISION = Column('NUMERIC_PRECISION', BIGINT(10))
    NUMERIC_SCALE = Column('NUMERIC_SCALE', BIGINT(10))
    DATETIME_PRECISION = Column('DATETIME_PRECISION', INTEGER(10))
    CHARACTER_SET_NAME = Column('CHARACTER_SET_NAME', String(64))
    COLLATION_NAME = Column('COLLATION_NAME', String(64))
    COLUMN_TYPE = Column('COLUMN_TYPE', MEDIUMTEXT)
    COLUMN_KEY = Column('COLUMN_KEY', Enum('', 'PRI', 'UNI', 'MUL'))
    EXTRA = Column('EXTRA', String(256))
    PRIVILEGES = Column('PRIVILEGES', String(154))
    COLUMN_COMMENT = Column('COLUMN_COMMENT', Text)
    GENERATION_EXPRESSION = Column('GENERATION_EXPRESSION', LONGTEXT)
    SRS_ID = Column('SRS_ID', INTEGER(10))
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, COLUMN_NAME)


class JsForm(Base):
    __bind_key__ = 'oa'
    __tablename__ = 'js_form'
    metadata = MetaData()
    __table_args__ = {
        'mysql_engine': "InnoDB",
        'mysql_collate': 'utf8mb4_general_ci',
        'mysql_charset': 'utf8mb4',
        'comment': 'js_form',
    }
    TABLE_CATALOG = Column(String(64))
    TABLE_SCHEMA = Column(String(64))
    TABLE_NAME = Column(String(64))
    COLUMN_NAME = Column(String(64))
    ORDINAL_POSITION = Column(String(64))
    COLUMN_DEFAULT = Column(String(64))
    IS_NULLABLE = Column(String(64))
    DATA_TYPE = Column(String(64))
    CHARACTER_MAXIMUM_LENGTH = Column(String(64))
    CHARACTER_OCTET_LENGTH = Column(String(64))
    NUMERIC_PRECISION = Column(String(64))
    NUMERIC_SCALE = Column(String(64))
    DATETIME_PRECISION = Column(String(64))
    CHARACTER_SET_NAME = Column(String(64))
    COLLATION_NAME = Column(String(64))
    COLUMN_TYPE = Column(String(64))
    COLUMN_KEY = Column(String(64))
    EXTRA = Column(String(64))
    PRIVILEGES = Column(String(64))
    COLUMN_COMMENT = Column(String(64))
    GENERATION_EXPRESSION = Column(String(64))
    SRS_ID = Column(String(64))
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, COLUMN_NAME)

    name_cn = Column(String(64))
    data_type = Column(String(64))
    num_max = Column(String(64))
    num_min = Column(String(64))
    valid_regx = Column(String(64))

