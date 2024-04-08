#!/usr/bin/python3
# adds all unique integers in a list
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return []
    uniq_list = list(set(my_list))
    result = 0
    for num in uniq_list:
        if isinstance(num, int):
            result += num
    return result
