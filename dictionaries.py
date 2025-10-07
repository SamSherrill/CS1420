# Sep 30 and Oct 2, 2025 class sessions

# d1 = {"name":"Alice", "age":30, "city":"New York", "grade":[95,99,92]}

# print(d1)
# print(d1.items())
# print(d1.keys())
# print(d1.values())

# for key,value in d1.items():
#     print(f"The key is {key} and the value is {value}")

# Suppose we have a dictionary of students and their grades
# We need to calculate the average grade for each student
# and print it out in a nice format
# grades_dict = {"Alice":[99,95,97,92], "Bob":[88,90,85,87], "Charlie":[70,75,80,72]}

# print(grades_dict.get("Alice"))

# for student, grades in grades_dict.items():
#     average = sum(grades) / len(grades)
#     print(f"The average grade for {student} is {average:.2f}")

# Think Like a Computer Scientist boook activity 12.7, exercise 1
# Write a script that does the following:
# Take a string from the user as input
# Create a dictionary to count the instance of  differnt characters in the string
# Print out the number of instances of each character to the terminal in sorted order

input_string = input("Enter a string: ")
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        # If the character is not in the dictionary, add the char as a key with a paired value of 1
        char_count[char] = 1

# Print out the number of instances of each character to the terminal in sorted order
# Sort by value, use a lambda function to do that
for char in sorted(char_count, key=lambda x: char_count[x]):
    print(f"{char}: {char_count[char]}")