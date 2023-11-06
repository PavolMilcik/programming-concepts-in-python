print("\n\n-------------------- COMPLEX EXAMPLES - FILTER FUNCTION AND LAMBDA FUNCTION -------------------\n\n")


print("The filter function in Python is used to filter elements from an iterable\n(a list, tuple, ...) based on a specified function or condition.\nIt returns an iterator containing the elements for which the function or condition evaluates to True.")
print("\nLambda is used as a one-line function in Python.")


print("\n\n------------------- 1. Example - compare Filter function vs Map function -------------------")
numbers_list_01 = list(range(1, 11))
def is_even_number_01(number):
    return number % 2 == 0

print("\na.) filter function - returns even numbers:") 
filter_list_01 = list(filter(is_even_number_01, numbers_list_01))
print(filter_list_01)


print("\n\nb.) map function - returns even numbers:")
map_list_01 = list(map(is_even_number_01, numbers_list_01))
print(map_list_01)


print("\n\nc.) filter function - returns even numbers using a lambda function:")
filter_lambda_list_01 = list(filter(lambda number: number%2==0, numbers_list_01))
print(filter_lambda_list_01)


print("\n\nd.) map function - returns even numbers using a lambda function:")
map_lambda_list_01 = list(map(lambda number: number%2==0, numbers_list_01))
print(map_lambda_list_01)



print("\n\n\n------------------- 2. Example - Filter function -------------------")
numbers_list_02 = list(range(1, 101))
def return_boolean_01(number):
    return number % 3 == 0 and number % 7 ==0

print("\na.) returns numbers divisible by both 3 and 7:")
filter_list_02 = list(filter(return_boolean_01, numbers_list_02))
print(filter_list_02)


print("\n\nb.) returns numbers divisible by both 3 and 7 using a lambda function:")
filter_lambda_list_02 = list(filter(lambda x: x%3==0 and x%7==0, numbers_list_02))
print(filter_lambda_list_02)


print("\n\nc.) returns numbers divisible by both 3 and 7 using a lambda function:")
filter_lambda_list_03 = list(filter(lambda x: not x%3 and not x%7, numbers_list_02))
print(filter_lambda_list_03)



print("\n\n\n------------------- 3. Example - Lambda function -------------------")
print("\na.) lambda is used as a one-line function in Python:")
print((lambda s,l,u: s[l:u] if l>0 and l<u and u<len(s) else s)("Python", 1, 3))
print((lambda s,l,u: s[l:u] if l>0 and l<u and u<len(s) else s)("Python", 1, 10))
print((lambda s,l,u: s[l:u] if l>0 and l<u and u<len(s) else s)("Python", -1, 3))


print("\n\nb.) lambda as a variable:")
my_new_lambda = lambda s,l,u: s[l:u] if l>0 and l<u and u<len(s) else s
print(my_new_lambda("Python", 1, 3))
print(my_new_lambda("Python", 1, 10))
print(my_new_lambda("Python", -1, 3))



print("\n\n\n------------------- 4. Example - Filter function -------------------")

print("\na.) returns numbers not divisible by 3 ---> True == any number except 0:")
print(list(map(lambda x: list(range(1, x+1)), filter(lambda x: x%3, range(1,7)))))
#                                                              True represents any number except 0 
#                                                              True == 1, 2, 3, -1, -5, 100
#                                                              True ----> 
#                                                              4%3=1 == True 
#                                                              5%3=2 == True
#                                                              6%3=0 == False
#                                                       1, 2, 4, 5
# [[1], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5]]


print("\n\nb.) returns numbers divisible by 3 ---> not 0/False == True:")
print(list(map(lambda x: list(range(1, x+1)), filter(lambda x: not x%3, range(1,7)))))
#                                                              False represents only number 0
#                                                              False == 0
#                                                              3%3=0 == False,  6%3=0 == False

#                                                              not 0 == 1 == True
#                                                              not False == True

#                                                              not 1 == 0 == False
#                                                              not True == False
#                                                       3, 6
# [[1, 2, 3], [1, 2, 3, 4, 5, 6]]



print("\n\n\n------------------- 5. Example - Filter function -------------------")

# [1, 2, 3, 4, 5, 6]
numbers_list_03 = list(range(1,7))

print("\na.) returns numbers not divisible by 3 ---> True == any number except 0:")
filter_lambda_list_04 = list(filter(lambda x: x%3, numbers_list_03))
# [1, 2, 4, 5]
print(filter_lambda_list_04)

map_lambda_list_02 = list(map(lambda x: list(range(1,x+1)), filter_lambda_list_04))
# [[1], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
print(map_lambda_list_02)


print("\n\nb.) returns numbers divisible by 3 ---> not 0/False == True:")
filter_lambda_list_05 = list(filter(lambda x: not x%3, numbers_list_03))
# [3, 6]
print(filter_lambda_list_05)

map_lambda_list_03 = list(map(lambda x: list(range(1,x+1)), filter_lambda_list_05))
# [[1, 2, 3], [1, 2, 3, 4, 5, 6]]
print(map_lambda_list_03)



print("\n\n\n------------------- 6. Example - Filter function -------------------")
print("\na.) from list return only numbers, not strings:")
arr_01 = ["Pavol", "Bubu", 1, 2, "City", 3.4]

filter_lambda_list_06 = list(filter(lambda x: type(x)==float or type(x)==int, arr_01))
print(filter_lambda_list_06)

print("\nb.) from list return only numbers, not strings and multiply them by 10:")
filter_lambda_list_07 = list( map(lambda y: y*10, filter(lambda x: type(x)==int or type(x)==float, arr_01)) )
print(filter_lambda_list_07)



print("\n\n\n------------------- 7. Example - Filter function - Prime numbers -------------------")

print("\na.) return prime numbers:")
print(list(filter(lambda x: not len(list(filter(lambda num: not x%num, range(2,int(x**(1/2) +1))))), range(2,101))))

# ---- explanation of x as number 31:
mth_vr = int(31**(1/2))
# 5

flr_lmbd_lst = list(filter(lambda num: not 31%num, range(2,int(31**(1/2) +1))))
# []

len_of_lst = len(flr_lmbd_lst)
# 0
# not 0/False == True
# ---- result: 31 is a prime number


# ---- explanation of x as number 45:
mth_vr = int(45**(1/2))
# 6

flr_lmbd_lst = list(filter(lambda num: not 45%num, range(2,int(45**(1/2) +1))))
# [3, 5]

len_of_lst = len(flr_lmbd_lst)
# 2
# not 2/True == False
# ---- result: 45 is not a prime number



print("\n")
