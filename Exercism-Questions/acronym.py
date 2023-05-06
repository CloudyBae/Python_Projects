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
    

