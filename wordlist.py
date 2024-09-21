def load_wordlist(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def is_password_secure(password, wordlist):
    return password.lower() not in wordlist

def main():
    wordlist_path = 'wordlist.txt'
    try:
        wordlist = load_wordlist(wordlist_path)
    except FileNotFoundError:
        print(f"Error: Wordlist file not found at {wordlist_path}")
        return

    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        if is_password_secure(password, wordlist):
            print("Password is not found in the wordlist. It's potentially secure.")
        else:
            print("Warning: Password found in the wordlist. Choose a different password.")

if __name__ == "__main__":
    main()