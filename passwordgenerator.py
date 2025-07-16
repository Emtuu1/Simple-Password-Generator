import random
import string

def generate_password(length=12):
    if length < 6:
        length = 6  # minimum length for decent security
    
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = input("Enter password length (minimum 6): ")
    try:
        length = int(length)
    except ValueError:
        length = 12
    
    print("Generated password:", generate_password(length))
