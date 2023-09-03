import hashlib

# Create an empty dictionary to store user credentials (username: password_hash)
user_credentials = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Hash the password before storing it
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_credentials[username] = password_hash
    print("Registration successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Check if the username exists
    if username in user_credentials:
        # Hash the entered password and compare it with the stored hash
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if password_hash == user_credentials[username]:
            print("Login successful!")
            access_secured_page()
        else:
            print("Invalid password. Login failed.")
    else:
        print("Username not found. Login failed.")

def access_secured_page():
    print("Welcome to the secured page!")

# Main loop
while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
