from pyDes import des, ECB, PAD_PKCS5
import binascii

def des_encrypt(message, key):
    des_cipher = des(key, ECB, padmode=PAD_PKCS5)
    encrypted_message = des_cipher.encrypt(message)
    return binascii.hexlify(encrypted_message).decode()

def des_decrypt(encrypted_message, key):
    des_cipher = des(key, ECB, padmode=PAD_PKCS5)
    decrypted_message = des_cipher.decrypt(binascii.unhexlify(encrypted_message))
    return decrypted_message.decode()

message = "Hello Student"
key = "12345678"  # DES key must be 8 bytes
encrypted_message = des_encrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")
decrypted_message = des_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
