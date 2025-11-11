# Class 11/11/25
# The professor lectured beforehand about pure functions, then lambda functions

from functools import reduce

# def add(x, y):
#     return x + y
# The function above is done more simply below
# add_ = lambda x, y: x + y

# def function_param(f,g,x):
# 	return f(g(x))

# def int_con(f,x):
#     return f(x)

def main():
    # print(add_(2, 3))
    # square = lambda x: x**2  # square function handled simply with a lambda function
    # print(square(4))

    # function_param(print,len,"Hello")  # this will return 5 because it will print the length of string Hello
    
    # a = "23"
    # b = int_con(int, a)  # converts string "23" to integer 23
    # print(type(b))  # shows that b is of type int

    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: x * 2, numbers))  # doubles each number in the list
    print(result)  # Output: [2, 4, 6, 8, 10]

    even_filter = list(filter(lambda x: x % 2 == 0, numbers))  # filters even numbers from the list
    print(even_filter)  # Output: [2, 4]
    odd_filter = list(filter(lambda x: x % 2 != 0, numbers))  # filters odd numbers from the list
    print(odd_filter)  # Output: [1, 3, 5]

    numbers_addition = [45, 23, 67, 12]
    reduce_result = reduce(lambda x, y: x + y, numbers_addition)  # sums all numbers in the list
    print(reduce_result)  # Output: 147

if __name__ == "__main__":
    main()