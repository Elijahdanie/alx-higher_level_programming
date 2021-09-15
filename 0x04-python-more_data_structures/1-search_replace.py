#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp_list = my_list.copy()
    for i in range(0, len(temp_list)):
        if temp_list[i] == search:
            temp_list[i] = replace
    return temp_list
