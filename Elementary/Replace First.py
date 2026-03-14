from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    
    if items:
        first_element = items[0]
        del items[0]
        items.append(first_element)
        return items
    else:
        return items
