from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HOST = "127.0.0.1"
PORT = "3306"
USERNAME = 'root'
PASSWORD = "123456"
DB = "oa"
localhost_oa_url = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}?charset=utf8mb4'
localhost_oa_engine = create_engine(localhost_oa_url, echo=True)
localhost_oa_session = sessionmaker(bind=localhost_oa_engine)()

test_db = "test"
localhost_test_url = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{test_db}?charset=utf8mb4'
localhost_test_engine = create_engine(localhost_test_url, echo=True)
localhost_test_session = sessionmaker(bind=localhost_test_engine)()
