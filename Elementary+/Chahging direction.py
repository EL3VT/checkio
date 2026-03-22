def changing_direction(elements):
    change_count = 0
    directions = []
    previous_direction = 0

    for element_index in range(len(elements) - 1):
        if elements[element_index] > elements[element_index + 1]:
            directions.append(1)
        
        elif elements[element_index] < elements[element_index + 1]:
            directions.append(2)

    if len(directions) > 2:    
        if directions[0] > directions[1]:
            previous_direction = 1
        
        elif directions[0] < directions[1]:
            previous_direction = 2
        
        else: 
            previous_direction = 3
        
        for element_index in range(len(directions) - 1):
            if previous_direction == 3:
                if directions[element_index] > directions[element_index + 1]:
                    previous_direction = 1
                
                elif directions[element_index] < directions[element_index + 1]:
                    previous_direction = 2
                
                else: 
                    previous_direction = 3
            if directions[element_index] > directions[element_index + 1] and previous_direction == 1:
                change_count += 1
                previous_direction = 2
            
            if directions[element_index] < directions[element_index + 1] and previous_direction == 2:
                change_count += 1
                previous_direction = 1
            
    return change_count


print("Example:")
print(changing_direction([1, 2, 3, 5, 4, 2, 5, 7, 8, 3, 2, 1]))


