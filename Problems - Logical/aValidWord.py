def validWord(word):
    if len(word) < 3:
        return False
    word = word.lower()
    vowels = "aeiou"
    has_vowel = False
    has_consonant = False
    
    for char in word:
        if char.isalnum():
            continue
        if char in vowels:
            has_vowel = True
        elif char.isalpha():
            has_consonant = True
    
    if has_vowel and has_consonant:
        return True
    return False
    
if __name__ == "__main__":
    word = input("Enter a Word:")
    if validWord(word):
        print("This is a valid word.")
    else:
        print("This is not a valid word.")
        