import hashlib

# Define the input string
input_string = "come home tomorrow"

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the bytes of the input string
hash_object.update(input_string.encode())

# Get the hexadecimal representation of the hash
hash_hex = hash_object.hexdigest()

# Print the original string and its hash
print(f"Original String: {input_string}")
print(f"SHA-256 Hash: {hash_hex}")
