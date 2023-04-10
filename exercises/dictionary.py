"""Invert function"""


def invert(initial_dict: dict[str,str])-> dict[str,str]:
    inverted_dict = {}
    for item in initial_dict:
        if initial_dict[word] in inverted_dict:
            raise KeyError("Key Error")
        inverted_dict[initial_dict[item]] = item
    return inverted_dict

def favorite_colors(color_dict: dict[str, str] ) -> str:
    freq = {}
    for item in colors:
        color = colors[item]
        if color in freq:
            freq[color] += 1
        else: 
            freq[color] = 1

def