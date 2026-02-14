
import random

USERS = {
    "admin": "Password123"  # hardcoded credential (bad practice)
}

def login(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False

def get_user_choice():
    choice = input("Enter a number (1-3): ")
    return choice

def insecure_math():
    expr = input("Type a math expression (example: 2+2): ")
    return eval(expr)  # eval is dangerous if user inputs malicious code

def generate_reset_code():
    # weak random method for something security-related
    return str(random.randint(100000, 999999))

def main():
    username = input("Username: ")
    password = input("Password: ")

    if login(username, password):
        print("Login success!")
        print("Reset code:", generate_reset_code())

        choice = get_user_choice()
        try:
            if choice == "1":
                print("Result:", insecure_math())
            elif choice == "2":
                print("Admin panel opened")
            else:
                print("Goodbye")
        except:
            print("Something went wrong")  # too generic
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
