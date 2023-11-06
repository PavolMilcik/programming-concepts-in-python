print("\n\n-------------------- COMPLEX EXAMPLES - REDUCE FUNCTION AND LAMBDA FUNCTION -------------------\n\n")


print("The reduce function in Python is a built-in function provided by the functools module.\nIt's used for performing a cumulative operation on the items of an iterable, such as a list,\nby successively applying a given function.")
print("\nLambda is used as a one-line function in Python.")


print("\n\n------------------- 1. Example - Reduce function -------------------")

from functools import reduce

list_of_numbers = list(range(1, 6+1))


print("\na.) python 'sum' function -  summing up a list of numbers:")
print(sum(list_of_numbers))
# 1 + 2 + 3 + 4 + 5 + 6


print("\n\nb.) reduce function -  summing up a list of numbers:")
def reduce_sum(a, b):
    return a + b

reduce_result_01 = reduce(reduce_sum, list_of_numbers)
print(reduce_result_01)


print("\n\nc.) reduce function using a lambda function -  summing up a list of numbers:")
reduce_result_02 = reduce(lambda x,y: x+y, list_of_numbers)
print(reduce_result_02)



print("\n\n\n------------------- 2. Example - Reduce function -------------------")

from functools import reduce
list_of_numbers = list(range(1, 6))

print("\na.) return a factorial using a reduce function:")
# 120
def reduce_multiplication(a,b):
    return a*b
reduce_fatorial_01 = reduce(reduce_multiplication, list_of_numbers)
print(reduce_fatorial_01)


print("\n\nb.) return a factorial using a reduce and lambda function:")
# 120
reduce_fatorial_02 = reduce(lambda a,b: a*b, list_of_numbers)
print(reduce_fatorial_02)


print("\n\nc.) return a factorial:")
# 120
reduce_fatorial_03 = list(map(lambda x: reduce(lambda y,z: y*z, range(1,x+1)), list_of_numbers))
print(reduce_fatorial_03)



print("\n")
