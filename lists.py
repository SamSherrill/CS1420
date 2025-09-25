# Tue 9/23/25 Class Session, continued on Thu 9/25/25

# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# nested_list.append([10, 11, 12])
# print(nested_list)

# mixed_list.append("$1M")
# print(mixed_list)

# Write a function that takes a list parameter with interger values,
# in your function iterate the list elements and extract the even numbers,
# put them in a new list and return it

def extract_even_numbers(input_list):
    even_numbers = []
    for number in input_list:
        if isinstance(number, int) and number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def main():
    mixed_list = [1, 2, 3, 3.1416, "Hello", True]
    my_list = [65, 99, 23, 44, 12, 78, 90, 33, 22]

    even_numbers = extract_even_numbers(my_list)
    print(even_numbers)  # Output: [44, 12, 78, 90, 22]

    print(sorted(my_list))

if __name__ == "__main__":
    main()