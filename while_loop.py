# Password validity using while loop:
# length at least 8 characters
# contains at least one uppercase letter
# contains at least one lowercase letter
# contains at least one special character
# contains at least one number

def is_valid_password():
    print("Password validity checker")
    print("A valid password must contain at least:")
    print("- 8 characters")
    print("- 1 uppercase letter")
    print("- 1 lowercase letter")
    print("- 1 special character")
    print("- 1 number")
    password = input("Enter a password to check its validity: ")
    
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_special = False
    has_number = False

    special_characters = "!@#$%^&*()-+?_=,<>/"

    i = 0
    while i < len(password):
        char = password[i]
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_characters:
            has_special = True
        elif char.isdigit():
            has_number = True
        i += 1

    return has_upper and has_lower and has_special and has_number

def nested_loops_example():
    print("Nested loops example:")
    for i in range(5):
        for j in range(5):
            # print(f"i: {i}, j: {j}")
            # print in a matrix format
            print(f"{i},{j}", end=" ")
        print()  # for new line after inner loop

def main():
        # if is_valid_password():
    #     print("The password is valid.")
    # else:
    #     print("The password is invalid.")

    nested_loops_example()

if __name__ == "__main__":
    main()