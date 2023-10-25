# ------------------------------ 4 Complex Examples - Recursion ------------------------------


print("\n------------------------------ 1. Recursion ------------------------------")
print("a.) Factorial")
result_fact = 1
def factorial_recursion_01(x):
    global result_fact
    result_fact *= x
    x -= 1
    if x > 0:
        factorial_recursion_01(x)
    else:
        print(result_fact)
factorial_recursion_01(5)    


print("\nb.) Factorial")
def factorial_recursion_02(y):
    if y == 0:
        return 1
    else:
        return y * factorial_recursion_02(y - 1)
print(factorial_recursion_02(5))



print("\n\n------------------------------ 2. Recursion ------------------------------")
print("a.) Division of two numbers")
def division_recursion_01(x):
    print(x)
    x = x / 2
    if x >= 1:
        division_recursion_01(x)
division_recursion_01(100)


print("\nb.) Division of two numbers")
def division_recursion_02(x, y):
    if x < y:
        return 0
    else:
        return 1 + division_recursion_02(x - y, y)
print(division_recursion_02(15, 5))



print("\n\n------------------------------ 3. Recursion ------------------------------")
print("a.) Print Characters from the Front of a String")
x_add = 0
def char_from_front_01(my_string):
    global x_add
    print(my_string[x_add])
    x_add += 1
    if x_add < len(my_string):
        char_from_front_01(my_string)
char_from_front_01("Pavol")


print("\nb.) Print Characters from the Front of a String")
xx_add = 0
result_string_front = ""
def char_from_front_02(my_string):
    global xx_add, result_string_front
    result_string_front += my_string[xx_add]
    xx_add += 1
    if xx_add < len(my_string):
        char_from_front_02(my_string)
    else:
        print(result_string_front)
char_from_front_02("Pavol")


print("\nc.) Print Characters from the Front of a String")
def char_from_front_03(param_string):
    x = len(param_string)
    if x > 0:
        print(param_string[0], end="")
        char_from_front_03(param_string[1:x])
char_from_front_03("John")



print("\n\n\n------------------------------ 4. Recursion ------------------------------")
print("a.) Print Characters from the Back of a String")
y_add = 0
def char_from_back_01(my_string):
    global y_add
    y_add += 1
    index_from_back = len(my_string) - y_add
    
    char_string = my_string[index_from_back]
    print(char_string)

    if index_from_back > 0:
        char_from_back_01(my_string)
char_from_back_01("Pavol")


print("\nb.) Print Characters from the Back of a String")
yy_add = 0
result_string_back = ""
def char_from_back_02(my_string):
    global yy_add, result_string_back
    
    yy_add += 1
    index_from_back = len(my_string) - yy_add
    
    char_string = my_string[index_from_back]
    result_string_back += char_string
    
    if index_from_back > 0:
        char_from_back_02(my_string)
    else:
        print(result_string_back)
char_from_back_02("Pavol")


print("\nc.) Print Characters from the Back of a String")
def char_from_back_03(word):
    x = len(word)
    if x > 1:
       char_from_back_03(word[1:x]) 
    print(word[0], end="")
char_from_back_03("Pavol")
# Pavol x=5 Pavol[1:5]=avol,  avol x=4 avol[1:4],  vol x=3 vol[1:3],  ol x=2 ol[1:2],  l x=1 
# lovaP   


print("\n\nd.) Print Characters from the Back of a String")
def char_from_back_03(param_string):
    x = len(param_string)
    if x > 0:
        print(param_string[-1], end="")
        char_from_back_03(param_string[0:-1])
char_from_back_03("John")
# John[-1]=n, Joh[-1]=h, Jo[-1]=o, J[-1]=J 
# nhoJ 



print("\n")
