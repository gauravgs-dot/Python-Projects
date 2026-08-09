import random
import string
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#ENCRYPT
plain_text=input("Enter the text to encrypt: ")
cipher_text=" "
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"Plain text: {plain_text}")
print(f"Encrypted text: {cipher_text}")
#DECRYPT
cipher_text=input("Enter a message to Decrypt:")
plain_text=" "
for letter in cipher_text:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"Encrypted text: {cipher_text}")   
print(f"Original text: {plain_text}")
