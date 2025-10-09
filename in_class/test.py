#  Class on 10/7/2025
#  Testing 2nd_file.py

def multiple_elem(item):
    return len(item[2]), item[0]
lst = [(5,"a","grape"), (9,"d","pear"), (13,"b","apple")]
result = sorted(lst, key=multiple_elem)
print(result)

# She mentioned that if we return multiple things, these will be returned as a tuple