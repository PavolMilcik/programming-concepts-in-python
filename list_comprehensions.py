print("\n\n------------------ 4 COMPLEX EXAMPLES - LIST COMPREHENSION ----------")


print("\n\n------------------ 1. Example - List comprehension ------------------")
print("a.)")
# [2, 4, 6, 8, 10]
even_number_list_01 = [x for x in range(1, 11) if x % 2 == 0]
print(even_number_list_01)

# compare list comprehension - up, vs for loop - down
even_numbers_01 = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers_01.append(i)
print(even_numbers_01)


print("\nb.)")
# [1, 20, 3, 40, 5, 60, 7, 80, 9, 100]
number_list_02 = [x*10 if x % 2 == 0 else x for x in range(1, 11)]
print(number_list_02)


print("\nc.)")
# [(1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd'), (6, 'even'), (7, 'odd'), (8, 'even'), (9, 'odd'), (10, 'even')]
comprehensions_list_01 = [(x, "even") if x % 2 == 0 else (x, "odd") for x in range(1, 11)]
print(comprehensions_list_01)



print("\n\n------------------ 2. Example - List comprehension ------------------")
# ['Learning', 'programming', 'is', 'great']
# [8, 11, 2, 5]
print("a.)")
message_01 = "Learning programming is great"
list_from_string_01 = message_01.split()
print(list_from_string_01)

len_list_01 = [len(x) for x in list_from_string_01]
print(len_list_01)


# compare list comprehension - up, vs for loop - down
print("\nb.)")
list_from_string_02 = []
temp_str = ""
counter = 0
for char in message_01:
    counter += 1
    if char != " ":
        temp_str += char
    elif char == " ":
        if len(temp_str) > 0:
            list_from_string_02.append(temp_str)
        temp_str = ""
    if counter == len(message_01) and message_01[-1] != " ":
        list_from_string_02.append(temp_str)
print(list_from_string_02)

len_list_02 = []
for x in list_from_string_02:
    len_list_02.append(len(x))
print(len_list_02)



print("\n\n------------------ 3. Example - List comprehension ------------------")
print("a.)")
# [0, 1, 2, 3, 4, 5, 6]
# [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]
def list_of_lists(param_last_number_in_list):
    user_list = list(range(0, param_last_number_in_list+1))
    print(user_list)
    
    list_of_lists_var = [list(range(0, x+1)) for x in user_list]
    return list_of_lists_var
print(list_of_lists(6))



print("\n\n------------------ 4. Example - List comprehension ------------------")
# *
# **
# ***
# ****
# *****
# ******
print("a.)")
star_list_01 = [print("*", end="") if star < row else print() for row in range(0, 6) for star in range(-1, row+1)]


# compare list comprehension - up, vs for loop - down
print("\nb.)")
def print_stars_01(param_rows):
    for row in range(0, param_rows):
        for star in range(0, row+1):
            print("*", end="")
        print()
print_stars_01(6)



print("\n")
