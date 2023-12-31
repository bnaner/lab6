# Layth
# Takes each digit, adds 3, and returns new password
def encode(password):
    new_pass = ""
    for char in password:
        new_value = int(char) + 3
        new_pass += str(new_value % 10)  # Ensures value isn't over 10
    return new_pass


# Takes each digit, subtracts 3, and returns new password
def decode(password):
    new_pass = ""
    for char in password:
        new_value = int(char) - 3
        new_pass += str((new_value + 10) % 10)
    return new_pass


running = True
saved_pass = ""

# displays menu options
while running:
    # Menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    # Branches based on user input
    choice = input("\nPlease enter an option: ")
    if choice == "1":
        pass_str = input("Please enter your password to encode: ")
        saved_pass = encode(pass_str)
        print("Your password has been encoded and stored!\n")
    elif choice == "2":
        print(f"The encoded password is {saved_pass}, and the original password is {decode(saved_pass)}.\n")
    elif choice == "3":
        running = False
        break
