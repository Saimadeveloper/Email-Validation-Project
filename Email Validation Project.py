import re

while True:
    Email = input("Enter your Email (or type 'exit' to quit): ").strip()  # Remove leading/trailing spaces
    if Email.lower() == 'exit':
        print("Exiting...")
        break

    k, j, d = 0, 0, 0  # Flags for spaces, uppercase letters, and invalid characters

    if len(Email) >= 6:
        if Email[0].isalpha():  # First character must be a letter
            if "@" in Email and Email.count("@") == 1:  # Check for exactly one '@'
                if Email[-4:] == ".com" or Email[-3:] == ".in":  # Valid domain check
                    for i in Email:
                        if i.isspace():  # Check for spaces
                            k = 1
                        elif i.isalpha() and i.isupper():  # Check for uppercase letters
                            j = 1
                        elif i.isdigit():  # Allow digits
                            continue
                        elif i in "_@.":  # Allow these special characters
                            continue
                        else:  # Invalid character
                            d = 1

                    if k == 1:
                        print("Invalid Email: Contains spaces.")
                    elif j == 1:
                        print("Invalid Email: Contains uppercase letters.")
                    elif d == 1:
                        print("Invalid Email: Contains invalid characters.")
                    else:
                        print("Valid Email")
                else:
                    print("Invalid Email: Incorrect domain format.")
            else:
                print("Invalid Email: Incorrect '@' usage.")
        else:
            print("Invalid Email: First character must be a letter.")
    else:
        print("Invalid Email: Too short.")
