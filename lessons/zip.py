

def zip(list_str: list[str],list_int: list[int]) -> str:
    if len(list_str) == len(list_int): 
        dict = {list_str[i]: list_int[i] for i in range(len(list_str))}
        return dict
    else: 
        return{}

