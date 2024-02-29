from .base import execute


def select(package_id: str = '') -> tuple:
    sql = """select * from pic_url where pic_package_id = '{}'""".format(package_id)
    return execute(sql)


def insert(package_id: str, count_id: int, url: str):
    sql = """insert into pic_url (pic_package_id, count_id, url)
    values ('{}', '{}', '{}')""".format(package_id, count_id, url)
    execute(sql)