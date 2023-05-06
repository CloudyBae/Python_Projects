"""Convert a phrase to its acronym.

Techies love their TLA (Three Letter Acronyms)!

Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).

Punctuation is handled as follows: hyphens are word separators (like whitespace); all other punctuation can be removed from the input."""

def abbreviate(words):
    new_word = words
    for letters in words:
        if not letters.isalpha() and letters != "'":
            new_word = new_word.replace(letters, " ")
    
    new_word = new_word.split()
    
    result = ""
    for value in new_word:
        result += value[0]
    return result.upper()
    

