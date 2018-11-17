#coding:utf-8

import schema

"""
学习的记录
--------------------------------------------------------------------------------
Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
"""


class Record:
    def __init__(self, value_list):
        self.value_list = value_list


class Dataset:
    def __init__(self, headers, records):
        self.headers = headers
        self.records = records


class Tableset(Dataset):
    def __init__(self, table,  records):
        super.__init__(table.col_list, records)
        self.table = table


class DBService:
    def __init__(self):
        self.talbe_schemas = []
        self.tables = []
        self.tablesets = []


def create_table():
    pass


def del_table():
    pass


def get_record_from_table():
    pass


def filter_from_dataset():
    pass


def insert_record():
    pass


def del_record():
    pass
