def custom_hash(input_string):
    # Using Python's built-in hash function
    # We'll use modulo to keep the hash within a specific range
    return hash(input_string) % 1000000

def demonstrate_hashing():
    phrases = [
        "come home tomorrow",
        "come home tomorrow.",
        "come home tomorrow"
    ]
    
    for phrase in phrases:
        hashed_value = custom_hash(phrase)
        print(f"Original: '{phrase}'")
        print(f"Hashed: {hashed_value}")
        print("---")

if __name__ == "__main__":
    demonstrate_hashing()