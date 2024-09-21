def caesar_cipher_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message

message = "COME AT HALF PAST SIX"
key = 2
encrypted_message = caesar_cipher_encrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")
