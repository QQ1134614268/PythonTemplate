# engine 参数语法 :id
# session 参数语法 %(id)s
# connection
# cursors
from sqlalchemy import Column, String
from sqlalchemy import Enum, Text, PrimaryKeyConstraint, TIMESTAMP, DateTime
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT, MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MysqlTables(Base):
    __tablename__ = 'tables'
    # __bind_key__ = 'information_schema'
    __table_args__ = {
        'schema': 'information_schema'
    }
    TABLE_CATALOG = Column(String(64))
    TABLE_SCHEMA = Column(String(64))
    TABLE_NAME = Column(String(64))
    TABLE_TYPE = Column(Enum('BASE TABLE', 'VIEW', 'SYSTEM VIEW'))
    ENGINE = Column(String(64))
    VERSION = Column(INTEGER(2))
    ROW_FORMAT = Column(Enum('Fixed', 'Dynamic', 'Compressed', 'Redundant', 'Compact', 'Paged'))
    TABLE_ROWS = Column(BIGINT(21))
    AVG_ROW_LENGTH = Column(BIGINT(21))
    DATA_LENGTH = Column(BIGINT(21))
    MAX_DATA_LENGTH = Column(BIGINT(21))
    INDEX_LENGTH = Column(BIGINT(21))
    DATA_FREE = Column(BIGINT(21))
    AUTO_INCREMENT = Column(BIGINT(21))
    CREATE_TIME = Column(TIMESTAMP)
    UPDATE_TIME = Column(DateTime)
    CHECK_TIME = Column(DateTime)
    TABLE_COLLATION = Column(String(64))
    CHECKSUM = Column(BIGINT(21))
    CREATE_OPTIONS = Column(String(256))
    TABLE_COMMENT = Column(Text)
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME)


class MysqlColumns(Base):
    __tablename__ = 'columns'
    __bind_key__ = 'information_schema'
    __table_args__ = {
        'schema': 'information_schema'
    }
    # __mapper_args__ = {
    #     'primary_key': []
    # }
    TABLE_CATALOG = Column('TABLE_CATALOG', String(64))
    TABLE_SCHEMA = Column('TABLE_SCHEMA', String(64))
    TABLE_NAME = Column('TABLE_NAME', String(64), comment="表名")
    COLUMN_NAME = Column('COLUMN_NAME', String(64), comment="字段名")
    ORDINAL_POSITION = Column('ORDINAL_POSITION', INTEGER(10), comment="顺序?")
    COLUMN_DEFAULT = Column('COLUMN_DEFAULT', Text, comment="默认值")
    IS_NULLABLE = Column('IS_NULLABLE', String(3), comment="是否可以None")
    DATA_TYPE = Column('DATA_TYPE', LONGTEXT, comment="数据类型")
    CHARACTER_MAXIMUM_LENGTH = Column('CHARACTER_MAXIMUM_LENGTH', BIGINT(21), comment="字符串最大长度?")
    CHARACTER_OCTET_LENGTH = Column('CHARACTER_OCTET_LENGTH', BIGINT(21), comment="?")
    NUMERIC_PRECISION = Column('NUMERIC_PRECISION', BIGINT(10), comment="数据精度")
    NUMERIC_SCALE = Column('NUMERIC_SCALE', BIGINT(10), comment="数据规模")
    DATETIME_PRECISION = Column('DATETIME_PRECISION', INTEGER(10), comment="?")
    CHARACTER_SET_NAME = Column('CHARACTER_SET_NAME', String(64), comment="?")
    COLLATION_NAME = Column('COLLATION_NAME', String(64), comment="表名")
    COLUMN_TYPE = Column('COLUMN_TYPE', MEDIUMTEXT, comment="??")
    COLUMN_KEY = Column('COLUMN_KEY', Enum('', 'PRI', 'UNI', 'MUL'), comment="字段类型,PRI UNI MUL")
    EXTRA = Column('EXTRA', String(256), comment="表名")
    PRIVILEGES = Column('PRIVILEGES', String(154), comment="表名")
    COLUMN_COMMENT = Column('COLUMN_COMMENT', Text, comment="字段注释")
    GENERATION_EXPRESSION = Column('GENERATION_EXPRESSION', LONGTEXT, comment="表名")
    SRS_ID = Column('SRS_ID', INTEGER(10), comment="")
    PrimaryKeyConstraint(TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME)
