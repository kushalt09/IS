def encrypt_columnar_transposition(plaintext, key):
    n_cols = len(key)
    plaintext = plaintext.replace(" ", "").upper()
    
    # Pad the plaintext to fit the matrix if necessary
    n_rows = (len(plaintext) + n_cols - 1) // n_cols
    padded_length = n_rows * n_cols
    plaintext = plaintext.ljust(padded_length, 'X')
    
    # Create the matrix
    matrix = [plaintext[i:i + n_cols] for i in range(0, len(plaintext), n_cols)]
    
    # Read columns in the order specified by the key
    ciphertext = ""
    for col in key:
        for row in matrix:
            ciphertext += row[col - 1]
    
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    n_cols = len(key)
    n_rows = len(ciphertext) // n_cols
    
    # Create an empty matrix to fill in the characters
    matrix = ['' for _ in range(n_cols)]
    
    col_lengths = [n_rows] * n_cols
    
    # Read columns in the order specified by the key
    idx = 0
    for col in key:
        for row in range(n_rows):
            matrix[col - 1] += ciphertext[idx]
            idx += 1
    
    # Read the matrix row-wise to get the plaintext
    plaintext = ""
    for row in range(n_rows):
        for col in range(n_cols):
            plaintext += matrix[col][row]
    
    return plaintext

# Message and key
message = "I WILL PASS EXAM"
key = [1, 3, 5, 2, 4]
encrypted_message = encrypt_columnar_transposition(message, key)
decrypted_message = decrypt_columnar_transposition(encrypted_message, key)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
