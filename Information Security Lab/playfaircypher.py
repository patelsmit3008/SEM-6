def create_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates while maintaining order
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' is merged with 'I'
    matrix = key + ''.join([char for char in alphabet if char not in key])
    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace('J', 'I')  # Merge J with I
    # Remove non-alphabetic characters and split into pairs
    prepared_text = ''.join([char for char in text if char.isalpha()])
    i = 0
    final_text = ''
    while i < len(prepared_text):
        final_text += prepared_text[i]
        if i + 1 < len(prepared_text) and prepared_text[i] == prepared_text[i + 1]:
            final_text += 'X'  # Add X to avoid duplicate pairs
            i += 1
        i += 1
    if len(final_text) % 2 != 0:
        final_text += 'X'  # If odd length, append 'X'
    return final_text

def encrypt(plain_text, key):
    matrix = create_matrix(key)
    prepared_text = prepare_text(plain_text)
    cipher_text = ''
    
    for i in range(0, len(prepared_text), 2):
        row1, col1 = find_position(matrix, prepared_text[i])
        row2, col2 = find_position(matrix, prepared_text[i+1])
        
        if row1 == row2:  # Same row
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle
            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]
    
    return cipher_text

def decrypt(cipher_text, key):
    matrix = create_matrix(key)
    plain_text = ''
    
    for i in range(0, len(cipher_text), 2):
        row1, col1 = find_position(matrix, cipher_text[i])
        row2, col2 = find_position(matrix, cipher_text[i+1])
        
        if row1 == row2:  # Same row
            plain_text += matrix[row1][(col1 - 1) % 5]
            plain_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plain_text += matrix[(row1 - 1) % 5][col1]
            plain_text += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle
            plain_text += matrix[row1][col2]
            plain_text += matrix[row2][col1]
    
    return plain_text

# Example usage:
word = input("Enter the word: ")
key = input("Enter the key: ")
encrypted = encrypt(word, key)
print(f"Encrypted word: {encrypted}")
decrypted = decrypt(encrypted, key)
print(f"Decrypted word: {decrypted}")