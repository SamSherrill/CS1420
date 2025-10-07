# Class on 10/7/2025

# fin = open("input.txt", "r")
# print(fin)
# print(fin.readlines())
# fin.close()

dict_text = {}
with open("input.txt", "r") as fin:
    for line in fin:
        # print(line, end = " ")
        line = line.strip()  # Using strip() to remove extra newlines
        line = line.split("|")  # Splitting into words (not used further here)
        dict_text[int(line[0])] = line[1]
        # print(line)
    # fin.close()  # Not needed when using 'with' statement

print(dict_text)

with open("output.txt", "w") as fout:
    fout.write("This is a test output file\n")