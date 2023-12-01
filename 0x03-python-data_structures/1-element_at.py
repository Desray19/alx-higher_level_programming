#!/usr/bin/python3
def element_at(my_list, index):
    if index < 0:
        return None
    if index >= len(my_list):
        return None
    return my_list[index]
