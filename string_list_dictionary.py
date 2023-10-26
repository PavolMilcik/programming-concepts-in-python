print("\n\n----------- WORKING WITH - STRINGS, LISTS AND DICTIONARIES ---------------")


print("\n\n------------------- 1. Example - Dictionary ----------------------")
print("a.) Find the most frequently occurring number in the list:")
# key: 2 value: 7
list_numbers_01 = [1, 2, 3, 1, 2, 5, 6, 1, 2, 8, 9, 5, 6, 1, 2, 3, 1, 5, 9, 2, 2, 2, 9]
my_dict_01 = {}
for i in list_numbers_01:
    if i not in my_dict_01:
        my_dict_01[i] = 1
    else:
        my_dict_01[i] += 1
print(my_dict_01)

max_key_01 = 0
max_value_01 = 0
for k, v in my_dict_01.items():
    if v > max_value_01:
        max_value_01 = v
        max_key_01 = k
print("key:", max_key_01, "value:", max_value_01)


print("\nb.) Find the most frequently occurring number in the list:")
# use 'get' function
# key: 2 value: 7
my_dict_02 = {}
for number in list_numbers_01:
    my_dict_02[number] = my_dict_02.get(number, 0) + 1
print(my_dict_02)

max_key_02 = 0
max_value_02 = 0
for k, v in my_dict_02.items():
    if v > max_value_02:
        max_value_02 = v
        max_key_02 = k
print("key:", max_key_02, "value:", max_value_02)



print("\n\n------------------- 2. Example - Working with Strings -------------------")
print("a.) fix new line:")
# C:\python
# otes
# C:\python\notes
string_path_error="C:\python\notes"
print(string_path_error)
string_path_fixed=r"C:\python\notes"
print(string_path_fixed)



print("\n\n------------------- 3. Example - List to String -------------------")
print("a.)")
# this is Python
list_of_strings_01 = ["this", "is", "Python"]
new_string_01 = " ".join(list_of_strings_01)
print(new_string_01)


# compare python function 'join' - up, vs for loop - down
print("\nb.)")
# this is string
new_string_02 = ""
for i in list_of_strings_01:
    for j in i:
        new_string_02 += j
    if list_of_strings_01[-1] != i:
        new_string_02 += " "
print(new_string_02)



print("\n\n------------------- 4. Example - String to List -------------------")
print("a.)")
# ['Learning', 'programming', 'is', 'great']
message_01 = "Learning programming is great"
list_from_string_01 = message_01.split()
print(list_from_string_01)



print("\n\n------------------- 5. Example - Working with Lists -------------------")
print("a.)")
# ['P', 'a', 'v', 'o', 'l', 1, 2, [3, 4]]
name_string_01 = "Pavol"
new_list_01 = []

# Iterating over the characters in the string_01 and appending them to the list.
for char in name_string_01:
    new_list_01.append(char)

# Extending the list with numbers.      
new_list_01.extend([1, 2])               

# Appending a nested list [3, 4] to new_list_01.
new_list_01.append([3, 4])               
print(new_list_01)


print("\nb.) Slice / Slicing:")
# 3
# ['P', 'v', 'l', 2]
# [[3, 4], 1, 'o', 'a']
print(new_list_01[-1][0])
print(new_list_01[0::2])
print(new_list_01[-1::-2])


print("\nc.) count char 'a' in list:")
# 3
print(message_01.count('a'))


print("\nd.) insert, reverse and sort:")
list_of_numbers_01 = [2, 5, 8, 11]
print(list_of_numbers_01)
list_of_numbers_01.insert(1, 3)
print(list_of_numbers_01)
list_of_numbers_01.reverse()
print(list_of_numbers_01)
list_of_numbers_01.sort()
print(list_of_numbers_01)



print("\n")
