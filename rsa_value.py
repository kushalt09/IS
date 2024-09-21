import rsa

def generate_keys():
    # Generate public and private keys
    (public_key, private_key) = rsa.newkeys(512)
    return public_key, private_key

def encrypt_message(message, public_key):
    # Encrypt the message using the public key
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    # Decrypt the message using the private key
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return decrypted_message

def main():
    # Generate RSA keys
    public_key, private_key = generate_keys()
    
    # Choose a message to encrypt
    message = "This is a test message."
    print(f"Original message: {message}")
    
    # Encrypt the message
    encrypted_message = encrypt_message(message, public_key)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, private_key)
    print(f"Decrypted message: {decrypted_message}")
    
    # Verify that the original and decrypted messages are the same
    if message == decrypted_message:
        print("RSA encryption and decryption test passed!")
    else:
        print("RSA encryption and decryption test failed.")

if __name__ == "__main__":
    main()
