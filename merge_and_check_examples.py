print("\n")


# --- 1. Merging two lists into a new list and then sorting the new list.
# --- 2. Checking the brackets or characters to see if they are in pairs.



print("\n----------- 1. Merging two lists into a new list and then sorting the new list ------------")

print("\na.) by using Python's built-in functions:")
list_nmbs_01 = [1, 2, 4, 3]
list_nmbs_02 = [2, 3, 6, 5]

new_list_01 = list_nmbs_01 + list_nmbs_02
new_list_01.sort()
print(new_list_01)


print("\n\nb.) by using the Bubble Sort algorithm:")
list_nmbs_03 = [1, 2, 4, 1, 6, 5]
list_nmbs_04 = [2, 3, 6, 6, 1, 2, 10, -5, 20, -6]

def merge_and_sort_list(param_list_1, param_list_2):
    new_list_02 = param_list_1 + param_list_2

    for i in new_list_02:
        for j in range(len(new_list_02)-1):
            current_number = new_list_02[j]
            next_number = new_list_02[j+1]
            if current_number >= next_number:
                new_list_02[j+1] = current_number
                new_list_02[j] = next_number
                
    return new_list_02
            
print(merge_and_sort_list(list_nmbs_03, list_nmbs_04))



print("\n\n\n----------- 2. Checking the brackets or characters to see if they are in pairs ------------")

print("\na.):")
def is_valid(param_string):
    stack_lst = []
    
    for c in param_string:
        if c == "(":
            stack_lst.append(")")
        elif c == "{":
            stack_lst.append("}")
        elif c == "[":
            stack_lst.append("]")
            
        elif c in stack_lst:
            stack_lst.remove(c)
        elif c not in stack_lst:
            stack_lst.append(c)
    
    if len(stack_lst) == 0:
        return True
    else:
        return False

print(  is_valid("")    )                       # True
print(  is_valid("()")  )                       # True
print(  is_valid("[")   )                       # False
print(  is_valid("[)")  )                       # False
print(  is_valid("([][]{()})")  )               # True
print(  is_valid("({([()()])}))")   )           # False
print(  is_valid("({([()()])})")    )           # True
print(  is_valid("({([()()])})()[][{]}")    )   # True
print(  is_valid("({([(s)a(s)])})")    )        # False
print(  is_valid("({([(s)a(s)a])})")    )       # True


print("\n\nb.) by using a dictionary:")
pairs_dict = {
    "(": ")",
    "{": "}",
    "[": "]"
}

def is_valid(param_string):
    stack_list = []
    
    for char in param_string:
        if char in pairs_dict.keys():
            stack_list.append(pairs_dict[char])
            
        elif char in stack_list:
            stack_list.remove(char)
        elif char not in stack_list:
            stack_list.append(char)
    
    if len(stack_list) == 0:
        return True
    else:
        return False

print(  is_valid("")    )                       # True
print(  is_valid("()")  )                       # True
print(  is_valid("[")   )                       # False
print(  is_valid("[)")  )                       # False
print(  is_valid("([][]{()})")  )               # True
print(  is_valid("({([()()])}))")   )           # False
print(  is_valid("({([()()])})")    )           # True
print(  is_valid("({([()()])})()[][{]}")    )   # True
print(  is_valid("({([(s)a(s)])})")    )        # False
print(  is_valid("({([(s)a(s)a])})")    )       # True




print("\n")
