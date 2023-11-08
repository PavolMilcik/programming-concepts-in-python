print("\n\n------------ COMPLEX EXAMPLES - TERNARY OPERATOR IN PYTHON ------------")


print("\n\n------------------- 1. Example - Ternary operator -------------------\n")
# 1 - number is odd
# 2 - number is even
# 3 - number is odd
# 4 - number is even
# ...

print("a.) by If-Else Statement")
def print_even_odd_numbers_01(numbers_list_param):
    for i in numbers_list_param:
        if i % 2 == 0:
            print(str(i) + " is even")
        else:
            print(str(i) + " is odd")
print_even_odd_numbers_01(range(1, 11))


print("\nb.) by Ternary operator")
def print_even_odd_numbers_02(numbers_list_param):
    for j in numbers_list_param:
        is_even_or_odd_number = str(j) + " is even" if j % 2 == 0 else str(j) + " is odd"
        print(is_even_or_odd_number)
print_even_odd_numbers_02(range(1, 11))



print("\n\n------------------- 2. Example - Ternary operator -------------------")

print("\nI.")
print("a.) Is number 6 even?")
is_even_or_not = True if 6 % 2 == 0 else False
print(is_even_or_not)

print("b.) Is number 7 even?")
is_even_or_not = True if 7 % 2 == 0 else False
print(is_even_or_not)


print("\nII.")
print("a.) Is number 6 even?")
is_even_or_not = 6 % 2 == 0
print(is_even_or_not)

print("b.) Is number 7 even?")
is_even_or_not = 7 % 2 == 0
print(is_even_or_not)


print("\nIII.")
print("a.) Is number 6 even?")
# 6%2 return 0/False
# not 6%2 return 1/True
is_even_or_not = not 6 % 2
print(is_even_or_not)

print("b.) Is number 7 even?")
# 7%2 return 1/True
# not 7%2 return 0/False
is_even_or_not = not 7 % 2
print(is_even_or_not)



print("\n")
