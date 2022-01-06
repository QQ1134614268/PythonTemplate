# -*- coding:utf-8 -*-
"""
@Time: 2022/1/6
@Description:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conf.config import localhost_world_url


class VideoUserVO:
    pass


class UserVO:
    pass


if __name__ == '__main__':
    engine = create_engine(localhost_world_url, echo=True)
    session = sessionmaker(bind=engine)()
    vos = session.query(VideoUserVO).all()
    dics = [vo.__dict__ for vo in vos]
    for data in dics:
        del data['_sa_instance_state']
    session.query(UserVO).delete()
    vos = [UserVO(**data) for data in dics]

    session.add_all(vos)
    session.commit()
