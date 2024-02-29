from .base import execute


def select(package_id: str = '') -> tuple:
    sql = """select * from `pic_package_info` where `id`='{}'""".format(package_id)
    return execute(sql)


def insert(package_id: str, count: int):
    sql = """insert into pic_package_info (id, count)
    values ('{}', {});""".format(package_id, count)
    execute(sql)


def update(package_id: str, count: int):
    sql = """update pic_package_info set count = {} where id = '{}'""".format(count, package_id)
    execute(sql)
