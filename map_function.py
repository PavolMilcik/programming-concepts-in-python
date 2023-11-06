print("\n\n------------ COMPLEX EXAMPLES - MAP FUNCTION AND LAMBDA FUNCTION ------------\n\n")


print("The map() function in Python is used to apply a given function to all items\nin an input list (or another iterable) and return an iterable map object.\nYou can convert the map object to a list to get a list of the results.")
print("\nLambda is used as a one-line function in Python.")


print("\n\n------------------- 1. Example - Map function -------------------")
print("\na.) normal def function - exponentiation of number or numbers from the list:")
numbers_list_01 = list(range(1, 11))
print(numbers_list_01)

def return_power_01(number, power=2):
    list_to_return = []
    if type(number) == list:
        for x in number:
            list_to_return.append(x**power)
        return list_to_return
    else:
        return number**power

print(return_power_01(5))
print(return_power_01(5,3))
print(return_power_01(numbers_list_01))
print(return_power_01(numbers_list_01, 3))


print("\n\nb.) map function - exponentiation of numbers from the list:")
def return_power_02(number, power=2):
    return number**power

map_list_01 = list(map(return_power_02, numbers_list_01))
print(map_list_01)


print("\n\nc.) for loop in map function - exponentiation of numbers from the list:")
for nmb in map(return_power_02, numbers_list_01):
    print(nmb, end=" ")



print("\n\n\n\n------------------- 2. Example - Lambda function -------------------")
print("\na.) lambda is used as a one-line function in Python:")
math_lambda_def = lambda x, y, z: x**y + z
print(math_lambda_def(5, 2, 10))


print("\n\nb.) map + lambda - exponentiation of numbers from the list:")
map_lambda_list_01 = list(map(lambda number: number**2, numbers_list_01))
print(map_lambda_list_01)



print("\n\n\n------------------- 3. Example - Map function -------------------")
print("\na.) normal def function - return a tuple containing the negative and positive values of the same number:")
numbers_list_02 = list(range(1,11))
def return_tuple(number):
    list_to_return = []
    if type(number) == list:
        for x in number:
            list_to_return.append((x, -x))
        return list_to_return
    else:
        return (number, -number)
print(return_tuple(numbers_list_02))


print("\n\nb.) map function - return a tuple containing the negative and positive values of the same number:")
map_list_02 = list(map(return_tuple, numbers_list_02))
print(map_list_02)


print("\n\nc.) map + lambda - return a tuple containing the negative and positive values of the same number:")
map_lambda_list_02 = list(map(lambda number: (number,-number), numbers_list_02))
print(map_lambda_list_02)



print("\n\n\n------------------- 4. Example - Map function + Lambda function -------------------")
print("\na.) map + lambda - return a list of chars from a string:")
map_lambda_string_to_list_01 = list(map(lambda char: char*2, "Hello"))
print(map_lambda_string_to_list_01)


print("\n\nb.) map + lambda - return a list of chars from a string, with an implemented print function:")
map_lambda_string_to_list_02 = list(map(lambda char: print(char*2, end=" "), "Hello"))



print("\n\n\n\n------------------- 5. Example - Map function -------------------")
print("\na.) map function - factorial using a while loop:")
def return_factorial_01(number):
    result_fact = 1
    while number > 0:
        result_fact *= number
        number -= 1
    return result_fact
print(return_factorial_01(5))

map_list_03 = list(map(return_factorial_01, numbers_list_01))
print(map_list_03)


print("\n\nb.) map function - factorial using a recursion:")
def return_factorial_02(number):
    if number == 0:
        return 1
    else:
        return number * return_factorial_02(number-1)
print(return_factorial_02(5))

map_list_04 = list(map(return_factorial_02, numbers_list_01))
print(map_list_04)



print("\n\n\n------------------- 6. Example - Map function -------------------")
print("\na.) normal def function using for loop and for loop:")
list_of_everything = ["Hi", 3, "Python", "World", 4]
# [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], [1, 2, 3, 4]]

def return_range_01(param_list):
    result_list = []
    for i in param_list:
        temp_list = []
        if type(i) == int or type(i) == float:
            for number in range(1, i+1):
                temp_list.append(number)
            result_list.append(temp_list)
        else:
            for j in range(1, len(i)+1):
                temp_list.append(j)
            result_list.append(temp_list)
    return result_list
print(return_range_01(list_of_everything))
    
    
print("\n\nb.) map function using for loop:")
list_of_everything = ["Hi", 3, "Python", "World", 4]
# [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], [1, 2, 3, 4]]

def return_range_02(param_list):
    result_list = []
    if type(param_list) == int or type(param_list) == float:
        for number in range(1, param_list+1):
            result_list.append(number)
    else:
        for i in range(1, len(param_list)+1):
            result_list.append(i)
    return result_list

map_list_05 = list(map(return_range_02, list_of_everything))
print(map_list_05) 


print("\n\nc.) map function using a lambda function:")
list_of_everything = ["Hi", 3, "Python", "World", 4]
# [[1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], [1, 2, 3, 4]]
map_list_06 = list(map(lambda x: list(range(1, x+1)) if type(x)==int else list(range(1, len(x)+1)), list_of_everything))
print(map_list_06) 



print("\n\n\n------------------- 7. Example - compare Map function vs Filter function -------------------")
numbers_list_01 = list(range(1, 11))
def is_even_number_01(number):
    return number % 2 == 0

print("\na.) map function - returns even numbers:")
map_list_07 = list(map(is_even_number_01, numbers_list_01))
print(map_list_07)


print("\n\nb.) filter function - returns even numbers:")
filter_list_01 = list(filter(is_even_number_01, numbers_list_01))
print(filter_list_01)


print("\n\nc.) map function - returns even numbers using a lambda function:")
map_lambda_list_03 = list(map(lambda number: number%2==0, numbers_list_01))
print(map_lambda_list_03)


print("\n\nd.) filter function - returns even numbers using a lambda function:")
filter_lambda_list_01 = list(filter(lambda number: number%2==0, numbers_list_01))
print(filter_lambda_list_01)



print("\n\n")
