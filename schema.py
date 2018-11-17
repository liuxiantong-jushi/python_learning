class Column:
    def __init__(self, col_name, col_type):
        self.name = col_name
        self.type = col_type


class Table:
    def __init__(self, table_name,  col_list):
        self.name = table_name
        self.col_list = col_list

