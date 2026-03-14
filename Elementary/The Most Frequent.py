def most_frequent(data: list[str]) -> str:
    data_dict = {}    
    
    for string in data:
        data_dict[string] = 0
        
    for string in data:
        data_dict[string] += 1
                    
    return max(data_dict, key=data_dict.get)
