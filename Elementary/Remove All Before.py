from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    temp_array = []
    flag = False
    
    for i in range(len(items)):       
        if items[i] == border:
            flag = True
            
        if flag:
            temp_array.append(items[i])
            
    if not (flag):
        return items
        
    return temp_array
