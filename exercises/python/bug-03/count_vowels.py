def count_vowels(text):
    vowels = "aeio"
    count = 0
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count
