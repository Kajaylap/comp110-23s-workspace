from csv import DictReader

def read_csv_rows(filename:str) -> list[dict[str,str]]:
    lines: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        lines.append(row)
    file_handle.close()
    return lines

def column_values(rows: list[dict[str,str]], column_name: str) -> list[str]:
    list_values: list[str] = []
    for row in rows:
        if column_name in row:
            list_values.append(row[column_name])
    return list_values

def columnar(row_list:list[dict[str,str]]) -> dict[str,list[str]]:
    dict_columns: dict[str,list[str]] = {}
    for column_name in row_list[0]:
       name_list = column_values(row_list, column_name)
       dict_columns[column_name] = name_list
    return dict_columns

def head(table: dict[str,list[str]], n: int) -> dict[str,list[str]]:
    n_rows: dict[str,list[str]] = {}
    for row in table:
        column_list: list[str] = []
        if n > len(table[row]):
            n = len(table[row])
        for items in range(0,n):
            column_list.append(table[row][items])
        n_rows[row] = column_list
    return n_rows
    
def select(table: dict[str,list[str]], column_names: list[str]) -> dict[str,list[str]]:
    new_dict: dict[str,list[str]] = {}
    for columns in column_names:
        new_dict[columns] = table[columns]
    return new_dict
    
def concat(table1: dict[str,list[str]], table2: dict[str,list[str]]) -> dict[str,list[str]]:
    concat_dict: dict[str,list[str]] = table1
    for column in table2:
        table2[column]
        if column in concat_dict:
            concat_dict[column] += table2[column]
        else:
            concat_dict[column] = table2[column]
    return concat_dict

def count(value_list: list[str]) -> dict[str,int]:
    count_dict: dict[str,int] = {}
    for item in value_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
           count_dict[item] = 1
    return count_dict

