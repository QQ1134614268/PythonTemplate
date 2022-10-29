import datetime


class Id:
    id: int


class Path(Id):
    parent_id: int
    children: list


class Human(Path):
    create_time: datetime.datetime
    update_time: datetime.datetime
    create_by: int
    update_by: int
    position: str
    version: str
    desc: str
    data: object
