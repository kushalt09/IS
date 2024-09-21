import getpass

# Predefined user credentials (in a real-world application, these would be stored securely in a database)
credentials = {
    1: {
        'username': 'Kushal',
        'password': 'kushal@123'
    },
    # You can add more users here if needed
}

def authenticate(user_id, password):
    """Check if the provided user ID and password match the stored credentials."""
    if user_id in credentials and credentials[user_id]['password'] == password:
        return True
    else:
        return False

def main():
    # Prompt the user for their ID and password
    user_id = int(input("Enter your user ID: "))  # User ID as an integer
    password = getpass.getpass("Enter your password: ")  # Using getpass to hide the password input
    
    # Authenticate the user
    if authenticate(user_id, password):
        username = credentials[user_id]['username']
        print(f"Authentication successful. Welcome, {username}!")
    else:
        print("Authentication failed. Invalid user ID or password.")

if __name__ == "__main__":
    main()
