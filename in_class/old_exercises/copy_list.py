# Thu 25 Sep class

def list_copy_attempt_1():
    list_1 = ["apple", "banana", "cherry"]
    list_2 = list_1
    list_2.append("date")
    print("List 1:", list_1)  # Output: ['apple', 'banana', 'cherry', 'date']
    print("List 2:", list_2)  # Output: ['apple', 'banana', 'cherry', 'date']

print("Copy Attempt 1: (demonstrating reference assignment)")
list_copy_attempt_1()

# We then discussed the differences between mutable and immutable types in Python.
# We then discussed the differences between shallow and deep copies of lists.

def list_copy_attempt_2():
    list_1 = ["apple", "banana", "cherry", ["orange", "grapefruit"]]
    list_2 = list_1[:]  # This creates a shallow copy of list_1
    # [:] is the slicing operator that creates a new list with the same elements
    # The colon indicates the start and end of the slice, and leaving them blank means to take the whole list
    list_2.append("date")
    print("List 1:", list_1)  # Output: ['apple', 'banana', 'cherry', ['orange', 'grapefruit']]
    print("List 2:", list_2)  # Output: ['apple', 'banana', 'cherry', 'date']

print("\nCopy Attempt 2: (demonstrating shallow copy)")
list_copy_attempt_2()

def list_copy_attempt_3():
    list_1 = ["apple", "banana", "cherry"]
    import copy
    list_2 = copy.deepcopy(list_1)  # This creates a deep copy of list_1
    list_2.append("date")
    print("List 1:", list_1)  # Output: ['apple', 'banana', 'cherry']
    print("List 2:", list_2)  # Output: ['apple', 'banana', 'cherry', 'date']

print("\nCopy Attempt 3: (demonstrating deep copy)")
list_copy_attempt_3()