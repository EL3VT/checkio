from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    parsed_text = text if len(text) % 2 == 0 else text + "_"
    pairs = []
    index = 0
    
    for i in range(len(parsed_text) // 2):
        pairs.append(parsed_text[index:index+2])
        index += 2
    return pairs


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
