# Sep 30, 2025 session

# tuple_1 = (1, 2, 3, "Cat", 3.1415)
# tuple_2 = tuple_1[0:4]+("apple", "orange")

# print(tuple_1)
# print(tuple_2)
# for item in tuple_2:
#     print(item)

# unsorted_tuple = (3,6,8,10,1,2,1,44,23,12,78,90,33,22)
# sorted_tuple = sorted(unsorted_tuple)
# print(type(sorted_tuple))
# print(sorted_tuple)

# def test(a,b):
#     a+=5
#     b+=10
#     return a,b

# result = test(3,7)
# print(type(result))

tuple_3 = (1,4,5)
a,b,c = tuple_3
print(a,b,c)

tuple_4 = (1,2,3,4,5,6,7,8,9)
tuple_5 = ("a","b","c","d","e","f","g","h","i")

print(list(zip(tuple_5, tuple_4)))