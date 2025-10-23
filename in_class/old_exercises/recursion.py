# 10/9/25 class session

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def hanoi(n, source, intermediate, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, target, intermediate)
    hanoi(1, source, intermediate, target)
    hanoi(n - 1, intermediate, source, target)
    
def main():
    input_number = int(input("Enter a non-negative integer: "))
    if input_number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {input_number} is {factorial(input_number)}.")
    print(f"The {input_number}th Fibonacci number is {fibonacci(input_number)}.")

if __name__ == "__main__":
    main()