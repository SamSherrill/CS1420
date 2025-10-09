# Oct 2 class session
# Learning about files in Python

fin = open("input.txt", "r")

# Read one line
# print(fin.readline(), end = " ")

# Read all lines; if we have already read some lines, it continues from there
# print(fin.readlines())

for line in fin:
    print(line)

