# String Analysis Tool
# - Write a program to analyze a string:
# - Count vowels, consonants, digits, and special characters.
# - Reverse the string and display the result.
def analyze_string(s):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0
    special_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char in digits:
            digit_count += 1
        else:
            special_count += 1
    reversed_string = s[::-1]
    return {
        "vowels": vowel_count,
        "consonants": consonant_count,
        "digits": digit_count,
        "special_characters": special_count,
        "reversed_string": reversed_string
    }
input_string = input("Enter a string: ")
result = analyze_string(input_string)
print("Vowels:", result["vowels"])
print("Consonants:", result["consonants"])
print("Digits:", result["digits"])
print("Special Characters:", result["special_characters"])
print("Reversed String:", result["reversed_string"])