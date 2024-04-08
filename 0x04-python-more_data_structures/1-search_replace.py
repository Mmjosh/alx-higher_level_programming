#!/usr/bin/python3
# replaces all occurences of an element by another in a new list
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return []
    new_list = my_list.copy()
    for i, x in enumerate(new_list):
        if x == search:
            new_list[i] = replace
    return new_list
