class Column:
    def __init__(self, col_name, col_type, is_primary):
        self.name = col_name
        self.type = col_type
        self.is_primary = is_primary


class Table:
    def __init__(self, table_name,  col_list):
        self.name = table_name
        self.col_list = col_list


