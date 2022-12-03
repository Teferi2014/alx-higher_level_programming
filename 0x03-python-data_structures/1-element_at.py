#!usr/bin/python3
def element_at(my_list, indx):
    tam = len(my_list)
    if indx < 0 or indx >= tam or tam == 0:
        return None
    else:
        return my_list[indx]
