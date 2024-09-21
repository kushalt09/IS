import hashlib

def hash_string(input_string: str) -> str:
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the input string
    sha256.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the digest
    hashed_value = sha256.hexdigest()
    
    return hashed_value

def main():
    # Define the input string
    phrase = "come home tomorrow"
    
    # Compute the hash value of the input string
    hashed_value = hash_string(phrase)
    
    # Print the original string and its hash value
    print("Original String:", phrase)
    print("Hashed Value:", hashed_value)

# Execute the main function
if __name__ == "__main__":
    main()
