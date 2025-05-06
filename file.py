def is_vowel(char):
    return char.lower() in 'aeiou'

def is_consonant(char):
    return char.isalpha() and not is_vowel(char)

# Read file content
filename = input("Enter filename (with extension): ")

try:
    with open(filename, 'r') as file:
        text = file.read()

    total_letters = 0
    vowels = 0
    consonants = 0

    for char in text:
        if char.isalpha():
            total_letters += 1
            if is_vowel(char):
                vowels += 1
            elif is_consonant(char):
                consonants += 1

    if total_letters == 0:
        print("No alphabetic characters found in the file.")
    else:
        vowel_percent = (vowels / total_letters) * 100
        consonant_percent = (consonants / total_letters) * 100

        print(f"Total letters: {total_letters}")
        print(f"Vowels: {vowels} ({vowel_percent:.2f}%)")
        print(f"Consonants: {consonants} ({consonant_percent:.2f}%)")

except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
