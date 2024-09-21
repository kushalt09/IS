def load_password_list(file_path: str) -> set:
    """
    Load a list of common passwords from a file and return as a set.
    """
    try:
        with open(file_path, 'r') as file:
            # Read each line and strip newlines
            passwords = {line.strip() for line in file}
        return passwords
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return set()
    except Exception as e:
        print(f"An error occurred: {e}")
        return set()

def check_password(password: str, password_list: set) -> bool:
    """
    Check if the given password is in the list of common passwords.
    """
    return password in password_list

def main():
    # Path to the password list file
    password_list_file = 'wordlist.txt'
    
    # Load the list of common passwords
    password_list = load_password_list(password_list_file)
    
    if not password_list:
        print("Password list is empty or could not be loaded.")
        return
    
    # Input password to check
    password = input("Enter your password to check: ")
    
    # Check if the password is in the list
    if check_password(password, password_list):
        print("Warning: Your password is too common and may be easily guessed.")
    else:
        print("Your password is not in the list of common passwords.")

if __name__ == "__main__":
    main()
