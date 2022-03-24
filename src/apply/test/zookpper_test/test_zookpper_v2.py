from kazoo.client import KazooClient
from conf.config import GGOK_ZOOKEEPER_HOST

# 连接zookeeper
zk = KazooClient(hosts=GGOK_ZOOKEEPER_HOST)  # hosts="127.0.0.1:2181,192.168.0.162:2182,192.168.0.162:2183"

# 启动连接
zk.start()

# 创建
# # 创建节点
if zk.exists("/my/favorite"):
    zk.delete("/my/favorite", recursive=True)

zk.ensure_path("/my/favorite")

# # 节点添加数据,必须是byte
zk.create("/my/favorite/node", b"a value")
zk.create("/my/favorite/name1", b"111111")
zk.create("/my/favorite/name2", b"222222")

# 获取节点数据
data, stat = zk.get("/my/favorite/node")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
# Version: 0, data: a value

# 列出节点数据
children = zk.get_children("/my/favorite")
print("There are %s children with names %s" % (len(children), children))
# There are 3 children with names ['node', 'name2', 'name1']

# 修改节点数据
zk.set("/my/favorite/node", b"some data")

# 删除节点数据
zk.delete("/my/favorite/name2", recursive=True)

# 关闭连接
zk.stop()
