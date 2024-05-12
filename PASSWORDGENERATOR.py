import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator App")
    while True:
        try:
            length = int(input("Enter the desired length of the password (enter 0 to quit): "))
            if length == 0:
                print("Thank you for using the Password Generator App. Goodbye!")
                break
            elif length < 0:
                print("Please enter a Positive length.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
