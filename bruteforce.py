def check_password_in_wordlist(password, wordlist_file):
    with open(wordlist_file, 'r', encoding='latin-1') as file:
        # Reading all lines and stripping whitespace/newlines
        lines = [line.strip() for line in file]
        # Check if the password matches any of the lines
        if password in lines:
            return True
    return False

def main():
    # Get the password from the user (visible input)
    password = input("Enter your password to check: ")

    # Specify the path to your wordlist file
    wordlist_file = 'wordlist.txt'  # Replace with the path to your wordlist

    # Check if the password is in the wordlist
    if check_password_in_wordlist(password, wordlist_file):
        print("Warning: Your password is in the wordlist! It's not secure.")
    else:
        print("Good news: Your password is not in the wordlist.")

if __name__ == "__main__":
    main()
