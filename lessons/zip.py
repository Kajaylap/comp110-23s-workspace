
def zip(list_str: list[str],list_int: list[int]) -> str:
    dict :  list()
    if len(list_str) == len(list_int): 
        new_dict = {list_str[i]: list_int[i] for i in range(len(list_str))}
        return new_dict
    if len(list_str) != len(list_int):
        return []
    if len(list_str) == 0 and len(list_int) == 0:
        return []


