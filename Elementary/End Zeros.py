def end_zeros(a: int) -> int:
    count = 0
    
    while int(a) == a:
        if a % 10 == 0:
            count += 1
        if a == 0:
            return 1
        
        a /= 10
    
    return count
