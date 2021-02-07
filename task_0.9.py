import re

def print_vowels(words):
    pattern = r"[aeiouAEIOU]"
    
    vowels = re.findall(pattern, words)
    print(vowels)