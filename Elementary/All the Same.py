from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    flag = True
    
    for i in range(len(elements) - 1):
        previous_element = elements[i]
        next_element = elements[i + 1]
        
        if previous_element != next_element:
            flag = False
    
    return flag
