import random
import string

def generate_captcha(length=6):
    """Generate a random CAPTCHA string of given length."""
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

def verify_captcha(user_input, captcha):
    """Check if the user's input matches the CAPTCHA."""
    return user_input == captcha

def main():

    captcha = generate_captcha()
    

    print(f"CAPTCHA: {captcha}")
    

    user_input = input("Please enter the CAPTCHA: ")

    if verify_captcha(user_input, captcha):
        print("Verification successful. You are a verified user.")
    else:
        print("Verification failed. CAPTCHA did not match.")

if __name__ == "__main__":
    main()
