# Class 11/11/25
# The professor lectured beforehand about pure functions, then lambda functions

# def add(x, y):
#     return x + y
# The function above is done more simply below
# add_ = lambda x, y: x + y

# def function_param(f,g,x):
# 	return f(g(x))

def int_con(f,x):
    return f(x)

def main():
    # function_param(print,len,"Hello")  # this will return 5 because it will print the length of string Hello
    
    a = "23"
    b = int_con(int, a)  # converts string "23" to integer 23
    print(type(b))  # shows that b is of type int

    # print(add_(2, 3))
    # square = lambda x: x**2  # square function handled simply with a lambda function
    # print(square(4))

if __name__ == "__main__":
    main()