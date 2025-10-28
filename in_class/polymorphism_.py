# 10/28/25 class, starting to discuss polymorphism

# def add(a:int, b:int) -> int:
#     return a + b
# print(add(2, 3))
# print(add("hello", "world"))

def add(a:int, b:int) -> int:
    return a + b
def add(a:int, b:int, c:int, d:int) -> int:
    return a + b + c + d
# This does not work the same as in other languages due to Python's re-definition of names
# The one defined last is the one that will be used

print(add(2, 3, 4, 5))