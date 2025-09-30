# Sep 30, 2025 session

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
grades_dict = {"Alice":[99,95,97,92], "Bob":[88,90,85,87], "Charlie":[70,75,80,72]}

# print(grades_dict.get("Alice"))

for student, grades in grades_dict.items():
    average = sum(grades) / len(grades)
    print(f"The average grade for {student} is {average:.2f}")

