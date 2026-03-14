def between_markers(text: str, start: str, end: str) -> str:
    output_string = ""
    flag = False
    
    for i in text:
        if i == end:
            flag = False
            break

        if flag:
            output_string += i

        if i == start:
            flag = True
                       
    return output_string
