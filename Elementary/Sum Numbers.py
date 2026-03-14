def sum_numbers(text: str) -> int:
    suma = 0
    
    for i in text.split(" "):
        if i.isdigit():
            suma += int(i)
            
    print(suma)
    return suma
