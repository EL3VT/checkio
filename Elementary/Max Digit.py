def max_digit(value: int) -> int:
    array = sorted([int(i) for i in str(value)])
    return array[-1]
