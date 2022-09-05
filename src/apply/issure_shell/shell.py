from datetime import datetime
from urllib.parse import quote_plus as urlquote

import psutil
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conf.config import DEBUG_MODE
from util.cache_util import to_json_file

env = {
    "arg": {
        "port": 3306,
    },
    "server": {
        "cpu_percent": None,
        "memory_max": None,
        "memory_free": None,
        "memory_percent": None,
        "total_connection": None
    },
    "process": {
        "pid": None,
        "cpu_percent": None
    }
}


def get_pid(port):
    for net_info in psutil.net_connections():
        laddr, raddr = "", ""
        try:
            laddr = f"{net_info.laddr.ip}:{net_info.laddr.port}"
        except Exception as e:
            print(e)
        if laddr.endswith(str(port)):
            return net_info.pid


@to_json_file(indent=2)
def run_3306(port):
    pid = get_pid(port)
    s = psutil.Process(pid)
    info = psutil.virtual_memory()

    env = {
        "arg": {
            "port": port,
        },
        "pid": {
            "pid": pid,
            "cpu_percent": s.cpu_percent(),
            "memory_percent": s.memory_percent(),
            "connections_num": len(s.connections()),
            "num_threads": s.num_threads(),
            # "threads": s.threads(),
        },
        "time": datetime.now(),
        "server": {
            "cpu_percent": psutil.cpu_percent,
            "memory_total": info.total,
            "memory_available": info.available,
            "memory_percent": info.percent,
            "connection_num": len(list(psutil.net_connections())),
        }
    }
    return env


@to_json_file(indent=2)
def exec_profile():
    env = {
        "arg": {
            "username": "root",
            "password": "Szcentral@1357",
            "host": "44.39.19.2",
            "port": "3306",
            "db": "pcd",
        },
        "result": []
    }
    pcdbak5_url = f'mysql+mysqlconnector://root:{urlquote("Szcentral@1357")}@44.39.19.2:3306/pcd?charset=utf8mb4'
    pcdbak5_engine = create_engine(pcdbak5_url, echo=DEBUG_MODE)
    pcdbak5_session = sessionmaker(bind=pcdbak5_engine)()
    # pcdbak5_session = localhost_test_session
    sql = "show processlist"
    response = pcdbak5_session.execute(sql)
    return [dict(zip(item.keys(), item)) for item in response]


if __name__ == '__main__':
    print(exec_profile())
