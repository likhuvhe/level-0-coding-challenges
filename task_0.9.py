import re

def print_vowels(words):
    pattern = r"[aeiouAEIOU]"
    
    vowels = list(re.findall(pattern, words))
    str_vowels = ""
    for vowel in vowels:
        str_vowels += f"{vowel}, "
    
    print(str_vowels[:-2])