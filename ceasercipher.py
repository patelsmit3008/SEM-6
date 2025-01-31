def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                cipher_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher_text += char  # Non-alphabetic characters remain unchanged
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                plain_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                plain_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            plain_text += char  # Non-alphabetic characters remain unchanged
    return plain_text

# Get user input for the word and operation
word = input("Enter the word: ")
key = int(input("Enter the key (integer): "))
encrypted = encrypt(word, key)
print(f"Encrypted word: {encrypted}")
decrypted = decrypt(word, key)
print(f"Decrypted word: {decrypted}")
