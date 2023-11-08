print("\n\n-------------------- COMPLEX EXAMPLES - FIRST CLASS FUNCTIONS -------------------\n")



print("\n\n------------------- 1. Example - First class functions -------------------")

print("\na.) assigning a function's body to a new variable,\nand this variable will now have the properties of that function:")
def old_name_function(a):
    return "Hi! " + str(a)

new_name_function = old_name_function
print(new_name_function(5))


print("\nb.) assigning a lambda function's body to a new variable:")
lambda_var_function = lambda x,y: x**y
print(lambda_var_function(5,2))


print("\nc.) calling the function within a new variable and storing its return value in this variable:")
def function_hi(param_number):
    return "Hi! " + str(param_number)

what_return_function = function_hi(8)
print(what_return_function)



print("\n\n\n------------------- 2. Example - First class functions -------------------")

print("\na.) calling a function that takes a parameter, which is another function from the outside:")
def hello_world_def_01():
    return "Hello world."

def function_wrapper_01(func):
    print("This is wrapper.")
    print(func)

function_wrapper_01(hello_world_def_01())


print("\nb.) calling a function that takes a parameter, which is another function from the outside:")
def hello_world_def_01():
    return "Hello world."

def function_wrapper_01(func):
    print("This is wrapper.")
    print(func())

function_wrapper_01(hello_world_def_01)


print("\nc.) calling a function from the outside, inside another function:")
def hello_world_def_02():
    return "Hello world."

def function_wrapper_02():
    print("This is wrapper.")
    print(hello_world_def_02())

function_wrapper_02()



print("\n\n\n------------------- 3. Example - First class functions -------------------")

print("\na.) function within a function:")
def function_wrapper_03():
    print("This is wrapper.")
    def hello_w_01():
        return "Hello world."
    print(hello_w_01())

function_wrapper_03()


print("\nb.) function within a function:")
def function_wrapper_04():
    print("This is wrapper.")
    def hello_w_02():
        print("Hello world.")
    return hello_w_02()

function_wrapper_04()


print("\nc.) function within a function:")
def function_wrapper_05():
    print("This is wrapper.")
    def hello_w_03():
        print("Hello world.")
    return hello_w_03

function_wrapper_05()()



print("\n\n\n------------------- 4. Example - First class functions -------------------")

def adder(x, y):
    return x + y

def substractor(x, y):
    return x - y

def multiplier(x, y):
    return x * y

list_of_functions = [adder, substractor, multiplier]


print("\na.) save three functions into a list and then call them with a for loop:")
for function in list_of_functions:
    print(function(6, 3))


print("\nb.) save three functions into a list and then call them with a map function by using lambda function:")
map_list = list(map(lambda x: x(4, 2), list_of_functions))
print(map_list)


print("\nc.) lambda function with three parameters stored in a variable,\nwhere one of the parameters is a function from the outside:")
lambda_var = lambda func, a, b: func(a, b)
print(lambda_var(adder, 3, 6))


print("\nd.) lambda function with three parameters stored in a variable,\nwhere one of the parameters are functions from the outside,")
print("we iterate through a list of saved three functions in a for loop with using a lambda function:")
lambda_var = lambda func, a, b: func(a, b)
for function in list_of_functions:
    print(lambda_var(function, 9, 4))


print("\ne.) a function that will have a lambda function as one of its parameters:")
def function_wrapper_06(func, k, l):
    return func(k,l)

print(function_wrapper_06(lambda y,z: y + z, 1, 2))



print("\n")
