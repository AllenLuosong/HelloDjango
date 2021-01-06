import pymysql
# 使用pymysql模块链接数据库并指定数据库版本
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
