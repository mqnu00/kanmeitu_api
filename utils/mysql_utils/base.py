import pymysql


def execute(sql: str) -> tuple:
    connection = pymysql.connect(
        host='127.0.0.1',  # 数据库主机名
        port=3306,  # 数据库端口号，默认为3306
        user='root',  # 数据库用户名
        passwd='123456',  # 数据库密码
        db='kanmeitu',  # 数据库名称
        charset='utf8'  # 字符编码
    )
    # 创建游标对象
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    res = cursor.fetchall()
    cursor.close()
    return res
