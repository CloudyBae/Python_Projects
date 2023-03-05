alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(which_direction, message, shift_amount):
  if which_direction == "encode":
    encryption = ""
    for letter in message:
      position = alphabet.index(letter)
      encryption += alphabet[position + shift_amount]
    print(f"The decoded text is {encryption}")
  elif which_direction == "decode":
    decryption = ""
    for letter in message:
      position = alphabet.index(letter)
      decryption += alphabet[position - shift_amount]
    print(f"The decoded text is {decryption}")

caesar(which_direction=direction, message=text, shift_amount=shift)