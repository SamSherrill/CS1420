# 9/18/25 Class Session

for i in range(5):
    print(i)

str_1 = "Hello World"

for i in range(0,len(str_1)):
    print(str_1[i])

### Write a function that takes a string input from user and prints the number of vowels in the string

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

def main():
    user_input = input("Enter a string: ")
    vowel_count = count_vowels(user_input)
    print(f"Number of vowels in the string: {vowel_count}") 

if __name__ == "__main__":
    main()