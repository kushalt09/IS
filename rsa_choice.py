def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

def rsa_keygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = next(i for i in range(2, phi) if gcd(i, phi) == 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_encrypt(public_key, plaintext):
    e, n = public_key
    return [(ord(char) ** e) % n for char in plaintext]

def rsa_decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr((char ** d) % n) for char in ciphertext])

# Example usage
p, q = 61, 53
public_key, private_key = rsa_keygen(p, q)

message = "HI"
encrypted_message = rsa_encrypt(public_key, message)
decrypted_message = rsa_decrypt(private_key, encrypted_message)

print(f"Public Key: {public_key}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
