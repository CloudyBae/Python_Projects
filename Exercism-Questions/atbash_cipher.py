"""Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that the resulting alphabet is backwards. 
The first letter is replaced with the last letter, the second with the second-last, and so on.
An Atbash cipher for the Latin alphabet would be as follows:
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba
It is a very weak cipher because it only has one possible key, and it is a simple mono-alphabetic substitution cipher. 
However, this may not have been an issue in the cipher's time.
Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, leaving numbers unchanged, and punctuation is excluded. 
This is to make it harder to guess things based on word boundaries. All text will be encoded as lowercase letters."""

plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"   

def encode(plain_text):   
    decode = ""
    for char in plain_text:
        if char.isalnum():
            decode += char.lower()
    
    encoded = ""
    for letter in decode:
        if letter.isalpha():
            position = plain.find(letter)
            encoded += cipher[position]
        else:
            encoded += letter
        
    decode_list = [encoded[i:i+5] for i in range(0, len(encoded), 5)]
    return " ".join(decode_list)

def decode(ciphered_text):
    decoded = ciphered_text.replace(" ", "")
    translation = ""
    for letter in decoded:
        if letter.isalpha():
            position = plain.find(letter)
            translation += cipher[position]
        else:
            translation += letter

    return translation