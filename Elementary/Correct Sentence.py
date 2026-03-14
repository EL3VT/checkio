def correct_sentence(text: str) -> str:
    upper_first_letter = text[0].upper()
    is_pointed = text[-1] == "."
    
    if is_pointed:
        return upper_first_letter + text[1::]
    else:
        return upper_first_letter + text[1::] + "."
print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
