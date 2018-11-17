#coding:utf-8

"""
学习的记录
--------------------------------------------------------------------------------
Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
"""


"""
--------------------------------------------------------------------------------
data_set
--------------------------------------------------------------------------------
"""


class Record:
    def __init__(self, value_list):
        self.value_list = value_list


class DataSet:
    def __init__(self, headers, records):
        self.headers = headers
        self.records = records


"""
--------------------------------------------------------------------------------
db_service
--------------------------------------------------------------------------------
develop plan:  
- basic data structure
- basic operation -- CURD
- support normal form 1
- SQL interpreter, support create/delete/select/where/update
- SQL interpreter, support condition
- SQL interpreter, support join
- support normal form 2
"""


class DBService:
    def __init__(self):
        self.table_schemas = {}
        self.data_sets = []

    def create_table(self, table):
        self.table_schemas[table.name] = table
        self.data_sets[table.name] = DataSet(table.col_list, [])

    def del_table(self, table_name):
        self.data_sets.pop(table_name)
        self.table_schemas.pop(table_name)

    def get_record_from_table(self, table_name):
        return self.data_sets[table_name].records

    def insert_record(self, table_name, records):
        self.data_sets[table_name].add(records)

    def del_record(self, table_name):
        self.data_sets[table_name].records = []




