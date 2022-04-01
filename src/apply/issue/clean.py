from conf.sw_config import shenwan_session
from util.cache_util import to_file


@to_file("out.json")
def getlist():
    results = shenwan_session.execute("show processlist")
    data = [dict(zip(result.keys(), result)) for result in results]
    return data


@to_file("out.json")
def kill(pid):
    sql = f"kill {pid}"
    results = shenwan_session.execute(sql)
    return sql


def main():
    while True:
        lis = getlist()
        for item in lis:
            if item["Info"] == "UPDATE rzrq_market_data s LEFT JOIN sec_stkprice b ON s.stk_code = b.stk_code AND s.biz_date = b.biz":
                kill(item["Id"])


if __name__ == '__main__':
    main()
