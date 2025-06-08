import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
