def beginning_zeros(a: str) -> int:
    cout = 0
    for i in a:
        if i == "0":
            cout += 1
        
        else:
            break
    return cout
