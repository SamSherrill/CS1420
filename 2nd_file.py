# Class on 10/7/2025

# fin = open("input.txt", "r")
# print(fin)
# print(fin.readlines())
# fin.close()

with open("input.txt", "r") as fin:
    for line in fin:
        # print(line, end = " ")
        line = line.strip()  # Using strip() to remove extra newlines
        line = line.split("|")  # Splitting into words (not used further here)
        print(line)

    # fin.close()  # Not needed when using 'with' statement

