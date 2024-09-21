import itertools

def prepare_text(text, key=False):
    text = text.upper().replace('J', 'I').replace(' ', '')
    if key:
        text = ''.join(sorted(set(text), key=text.index))  # Remove duplicates
    return text

def generate_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is typically omitted in Playfair cipher
    key = prepare_text(key, key=True)
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def process_digraphs(text, matrix, encrypt=True):
    prepared_text = prepare_text(text)
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'

    digraphs = []
    i = 0
    while i < len(prepared_text):
        a = prepared_text[i]
        b = prepared_text[i + 1] if i + 1 < len(prepared_text) else 'X'
        if a == b:
            digraphs.append(a + 'X')
            i += 1
        else:
            digraphs.append(a + b)
            i += 2

    result = []
    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        if row1 == row2:
            if encrypt:
                result.append(matrix[row1][(col1 + 1) % 5])
                result.append(matrix[row2][(col2 + 1) % 5])
            else:
                result.append(matrix[row1][(col1 - 1) % 5])
                result.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            if encrypt:
                result.append(matrix[(row1 + 1) % 5][col1])
                result.append(matrix[(row2 + 1) % 5][col2])
            else:
                result.append(matrix[(row1 - 1) % 5][col1])
                result.append(matrix[(row2 - 1) % 5][col2])
        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return ''.join(result)

def encrypt(plaintext, key):
    key_matrix = generate_key_matrix(key)
    return process_digraphs(plaintext, key_matrix, encrypt=True)

def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    return process_digraphs(ciphertext, key_matrix, encrypt=False)

message = "INFORMATION SYSTEM"
key = "SECURE"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
