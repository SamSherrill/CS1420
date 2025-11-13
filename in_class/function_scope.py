# Class 11/13/25 discussing helper and inner functions

def area_triangle(base: float, height: float) -> float:
    return 0.5 * base * height
def area_multiple_triangle(n, base: float, height: float) -> float:
    one_triangle = area_triangle(base, height)
    return one_triangle * n

def func1(name):
    def func2():
        return f"Hello, {name}!"
    return func2()

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

def main():
    # base = float(input("Enter the base of the triangle: "))
    # height = float(input("Enter the height of the triangle: "))
    # n = int(input("Enter the number of triangles: "))
    # total_area = area_multiple_triangle(n, base, height)
    # print(f"The total area of {n} triangles is: {total_area}")

    print(func1("Alice"))

    outer = make_multiplier(3)
    result = outer(10)
    print(f"Result of multiplying 10 by 3: {result}")

if __name__ == "__main__":
    main()