#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    if my_list:
        for i in my_list:
            if i not in new_list:
                new_list.insert(0, i)
    return sum(new_list)
