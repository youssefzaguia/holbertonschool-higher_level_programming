#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list.insert(i, replace)
            new_list.remove(search)
    return new_list