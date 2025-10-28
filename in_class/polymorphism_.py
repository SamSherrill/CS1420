# 10/28/25 class, starting to discuss polymorphism

# def add(a:int, b:int) -> int:
#     return a + b
# print(add(2, 3))
# print(add("hello", "world"))

def add(a:int, b:int) -> int:
    return a + b
def add(a:int, b:int, c:int, d:int) -> int:
    return a + b + c + d
# print(add(2, 3, 4, 5))
# This does not work the same as in other languages due to Python's re-definition of names
# The one defined last is the one that will be used

def add(*args, **kwargs):
    if len(args)>0:
        return sum(args)
    else:
        return 0
print(add(5,3,7,9))