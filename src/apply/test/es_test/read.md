https://www.ruanyifeng.com/blog/2017/08/elasticsearch.html

Relational DB Elasticsearch 数据库(database)         索引(indices)
表(tables)                 types 行(rows)                   documents 字段(columns)              fields

method url地址 描述 PUT localhost:9200/索引名称/类型名称/文档id 创建文档（指定文档id） POST localhost:9200/索引名称/类型名称 创建文档 （随机文档id） POST
localhost:9200/索引名称/类型名称/文档id/_update 修改文档 DELETE localhost:9200/索引名称/类型名称/文档id 删除文档 GET localhost:9200/索引名称/类型名称/文档id
查询文档通过文档id POST localhost:9200/索引名称/类型名称/_search 查询所有数
