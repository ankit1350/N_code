def calculate_percentage_from_file():
    try:
        file_name = input("Enter the file name: ")
        
        if file_name == "txt.txt":
            print("Processing 'txt.txt' directly...")
        
        with open(file_name, 'r') as file:
            file_content = file.read()
        
        text = file_content.lower()
        
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        total_chars = 0
        vowel_count = 0
        consonant_count = 0

        for char in text:
            if char.isalpha():
                total_chars += 1
                if char in vowels:
                    vowel_count += 1
                elif char in consonants:
                    consonant_count += 1

        if total_chars == 0:
            print("No alphabetic characters found in the input.")
            return

        vowel_percentage = (vowel_count / total_chars) * 100
        consonant_percentage = (consonant_count / total_chars) * 100

        print(f"Vowel Percentage: {vowel_percentage:.2f}%")
        print(f"Consonant Percentage: {consonant_percentage:.2f}%")

    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example call
calculate_percentage_from_file()

