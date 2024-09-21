from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(message, key):
    # Convert message and key to bytes
    message_bytes = message.encode()
    key_bytes = key.encode()
    
    # Pad the message to be a multiple of the block size
    padded_message = pad(message_bytes, AES.block_size)
    
    # Create a new AES cipher with the key and a random IV
    cipher = AES.new(key_bytes, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(padded_message)
    
    # Prepend the IV to the encrypted message
    iv = cipher.iv
    combined_message = iv + encrypted_message
    
    # Encode the combined message as base64
    encrypted_message_b64 = base64.b64encode(combined_message).decode()
    return encrypted_message_b64

def aes_decrypt(encrypted_message_b64, key):
    # Decode the base64 encoded message
    combined_message = base64.b64decode(encrypted_message_b64)
    
    # Extract the IV and the encrypted message
    iv = combined_message[:AES.block_size]
    encrypted_message = combined_message[AES.block_size:]
    
    # Convert the key to bytes
    key_bytes = key.encode()
    
    # Create a new AES cipher with the key and the extracted IV
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv=iv)
    
    # Decrypt and unpad the message
    decrypted_message = cipher.decrypt(encrypted_message)
    unpadded_message = unpad(decrypted_message, AES.block_size)
    decrypted_message_str = unpadded_message.decode()
    return decrypted_message_str

message = "Good Morning ALL"
key = "1234567890123456" # 16-byte key for AES

encrypted_message = aes_encrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = aes_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
