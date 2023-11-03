print("\n\n------------------ COMPLEX EXAMPLES - BOOLEAN EXPRESSION IN PYTHON FUNCTION ----------------\n\n")


print("The function's purpose is to perform a computation and return a result as a boolean value.")


print("\n\n------------------- 1. Example - Python function with a boolean expression -------------------")
print("\na.) returns even numbers using a def function with if else statement:")
numbers_list_01 = list(range(1, 11))

def is_even_number_01(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even_number_01(5))


print("\n\nb.) returns even numbers using a def function with boolean expression:")
def is_even_number_02(number):
    return number % 2 == 0
print(is_even_number_02(6))



print("\n\n------------------- 2. Example - Python function with a boolean expression -------------------")
print("\na.) boolean expression - compare numbers:")
def compare_numbers(x, y, z):
    return x > y > z
print(compare_numbers(8, 6, 4))
print(compare_numbers(8, 6, 7))



print("\n\n------------------- 3. Example - Python function with a boolean expression -------------------")
print("\na.) returns even numbers using map function + def function with boolean expression:")
map_list = list(map(is_even_number_02, numbers_list_01))
print(map_list)


print("\n\nb.) returns even numbers using filter function + def function with boolean expression:")
filter_list_01 = list(filter(is_even_number_02, numbers_list_01))
print(filter_list_01)



print("\n\n------------------- 4. Example - Python function with a boolean expression -------------------")

print("\na.) returns even numbers using a def function with boolean expression")
def bool_express_01(number):
    return number % 2 == 0
print(bool_express_01(6))
print(bool_express_01(3))

print("\nb.) returns even numbers using a def function with boolean expression")
def bool_express_02(number):
    return number % 2
print(bool_express_02(6))
print(bool_express_02(3))

print("\nc.) returns even numbers using a def function with boolean expression")
def bool_express_03(number):
    return not number % 2
print(bool_express_03(6))
print(bool_express_03(3))



print("\n\n-------------- 5. Example - Map, Filter and Lambda function with Boolean Expression --------------")
list_of_numbers = list(range(1, 11))

print("\nA.) returns even numbers")
# [2, 4, 6, 8, 10]
print("\ti.) map function:")
map_list = list(map(bool_express_01, list_of_numbers))
print("\t", map_list)

print("\n\tii.) filter function:")
filter_list = list(filter(bool_express_01, list_of_numbers))
print("\t", filter_list)


print("\n\nB.) returns even numbers using a lambda function")
# [2, 4, 6, 8, 10]
print("\ti.) map function:")
map_lambda_list_01 = list(map(lambda x: x % 2 == 0, list_of_numbers))
print("\t", map_lambda_list_01)

print("\n\tii.) filter function:")
filter_lambda_list_01 = list(filter(lambda x: x % 2 == 0, list_of_numbers))
print("\t", filter_lambda_list_01)


print("\n\nC.) returns even numbers using a lambda function")
# [1, 3, 5, 7, 9]
print("\ti.) map function:")
map_lambda_list_02 = list(map(lambda x: x % 2, list_of_numbers))
print("\t", map_lambda_list_02)

print("\n\tii.) filter function:")
filter_lambda_list_02  = list(filter(lambda x: x % 2, list_of_numbers))
print("\t", filter_lambda_list_02)


print("\n\nD.) returns even numbers using a lambda function")
# [2, 4, 6, 8, 10]
print("\ti.) map function:")
map_lambda_list_03 = list(map(lambda x: not x % 2, list_of_numbers))
print("\t", map_lambda_list_03)

print("\n\tii.) filter function:")
filter_lambda_list_03  = list(filter(lambda x: not x % 2, list_of_numbers))
print("\t", filter_lambda_list_03)



print("\n")
