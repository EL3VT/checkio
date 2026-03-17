from datetime import date

def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    date_1 = date(a[0], a[1], a[2])
    date_2 = date(b[0], b[1], b[2])

    differense = date_2 - date_1
    
    return abs(differense.days)


print("Example:")
print(days_diff((2014, 1, 1), (2014, 8, 27)))

assert days_diff((1970, 1, 1), (2000, 1, 1)) == 10957
print("The mission is done! Click 'Check Solution' to earn rewards!")
