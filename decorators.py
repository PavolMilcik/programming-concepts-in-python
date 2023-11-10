print("\n\n-------------------- COMPLEX EXAMPLES - DECORATORS -------------------\n")


print("In Python, decorators are a powerful and flexible way to modify or enhance the behavior of functions or methods.")
print("They are essentially functions that take another function as input and return a new function with added functionality. ")


print("\n\n------------------- 1. Example - Decorators -------------------")

import datetime
import time

print("\na.) classical call of functions located outside the body of the function in which we call them:")
def user_name_00(name):
    print(name)

def user_time_00(param_second):
    print(param_second, "seconds pause")
    time.sleep(param_second)

def date_time_name_00():
    print(datetime.datetime.now())
    user_name_00("Pavol")
    user_time_00(2)
    print(datetime.datetime.now())
date_time_name_00()


print("\nb.) the classic way of using functions as parameters in other functions, without using the decorator technique:")
def date_time_name_01(funct_user_name, usr_name, funct_time, second):
    print(datetime.datetime.now())
    funct_user_name(usr_name)
    funct_time(second)
    print(datetime.datetime.now())

def user_name_01(name):
    print(name)

def user_time_01(param_second):
    print(param_second, "seconds pause")
    time.sleep(param_second)

date_time_name_01(user_name_01, "Pavol", user_time_01, 2)


print("\nc.) use functions as parameters in other functions using the decorator technique:")
def date_name_decorator_01(param_function):
    def wrapper(*args):
        print(datetime.datetime.now())
        param_function(*args)
        print(datetime.datetime.now())
    return wrapper

@date_name_decorator_01
def user_name_02(name):
    print(name)
user_name_02("Pavol")


print("\nd.) use functions as parameters in other functions using the decorator technique:")
def user_time_02(param_second):
    print(param_second, "seconds pause")
    time.sleep(param_second)

def date_name_decorator_02(param_function):
    def wrapper(*args):
        print(datetime.datetime.now())
        param_function(*args)
        print(datetime.datetime.now())
    return wrapper

@date_name_decorator_02
def user_name_02(name, surname):
    print(name, surname)
    user_time_02(2)
user_name_02("Pavol", "Mlck")



print("\n\n\n------------------- 2. Example - Decorators -------------------")

import time
import datetime

print("\nDecorator_01: The function we send to the decorator has one parameter.")
def duration_time_01(param_func):
    def wrapper(param):
        print(datetime.datetime.now())
        param_func(param)
        print(datetime.datetime.now())
    return wrapper


print("\na.)")
def sleep_function_01(param_pause):
    print(str(param_pause) + " seconds pause")
    time.sleep(param_pause)

duration_time_01(sleep_function_01)(2)


print("\nb.)")
def sleep_function_02(param_pause):
    print(str(param_pause) + " seconds pause")
    time.sleep(param_pause)

sleep_function_001 = duration_time_01(sleep_function_02)
sleep_function_001(2)


print("\nc.)")
@duration_time_01
def sleep_function_03(param_pause):
    print(str(param_pause) + " seconds pause")
    time.sleep(param_pause)

sleep_function_03(2)



print("\n\n\n------------------- 3. Example - Decorators -------------------")

print("\nDecorator_02: The function we send to the decorator has multiple parameters.")
def duration_time_02(param_func):
    def wrapper(*args):
        print(datetime.datetime.now())
        param_func(*args)
        print(datetime.datetime.now())
    return wrapper


print("\na.)")
@duration_time_02
def print_name(param_name, sur_name):
    print("My name is: " + param_name + " " + sur_name)

print_name("Pavol", "Mlck")


print("\nb.)")
@duration_time_02
def print_name_sleep_funct(param_name, param_surname, param_pause):
    print("My name is: " + param_name + " " + param_surname)
    print(str(param_pause) + " seconds pause")
    time.sleep(param_pause)

print_name_sleep_funct("Pavol", "Mlck", 2)


print("\nc.)")
def log_info_01(func):
    def wrapper(pause, name):
        print(datetime.datetime.now())
        print("The length of the pause is: " + str(pause) + " seconds.")
        func(pause, name)
        print(datetime.datetime.now())
        print()
    return wrapper

@log_info_01
def send_pause_01(prm_ps, nm):
    time.sleep(prm_ps)
    print(nm)
send_pause_01(1, "Pavol")
send_pause_01(2, "Bubu")
send_pause_01(3, "Keko")


print("\nd.) plus return:")
def log_info_02(func):
    def wrapper(pause, name):
        print(datetime.datetime.now())
        print("The length of the pause is: " + str(pause) + " seconds.")
        value_r = func(pause, name)
        print(datetime.datetime.now())
        print()
        return value_r
    return wrapper

@log_info_02
def send_pause_02(prm_ps, nm):
    time.sleep(prm_ps)
    print(nm)
    return prm_ps
return_01 = send_pause_02(1, "Pavol")
return_02 = send_pause_02(2, "Bubu")
return_03 = send_pause_02(3, "Keko")

sum_returns = return_01 + return_02 + return_03
print("The sum of all pauses is: " + str(sum_returns) + ".")



print("\n\n\n------------------- 4. Example - Decorators -------------------")

print("\nDecorator_03: The decorator returns the return value of the function we send to the decorator.")
def duration_time_03(param_func):
    def wrapper(*args):
        print(datetime.datetime.now())
        return_value = param_func(*args)
        print(datetime.datetime.now())
        return return_value
    return wrapper


print("\na.)")
@duration_time_03
def print_name(param_name, sur_name):
    print("My name is: " + param_name + " " + sur_name)
    return "this is return: " + param_name

print_name_001 = print_name("Pavol", "Mlck")
print(print_name_001)



print("\n\n\n------------------- 5. Example - Decorators -------------------")

print("\nEnsuring that the function we send to the decorator does not change its name, for example to 'wrapper', but retains its original name.\n")

print("\na.) before handling the error:")
def log_duration(func):
    def wrapper(x):
        print(datetime.datetime.now())
        func(x)
        print(datetime.datetime.now())
    return wrapper

@log_duration
def hello_world_02(param_name):
    print("Hello world " + param_name)
hello_world_02("Pavol")
print("\nthis is the name of the function 'hello_world_02' after applying a decorator to it ---> " + hello_world_02.__name__ + "\n\n")


print("\nb.) after handling the error:")
import functools

def log_date(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(datetime.datetime.now())
        func(*args)
        print(datetime.datetime.now())
    return wrapper

@log_date
def hello_world_03(param_name):
    print("Hello world " + param_name)
hello_world_03("Pavol")
print("\nthis is the name of the function 'hello_world_03' after applying a decorator to it ---> " + hello_world_03.__name__)



print("\n\n\n------------------- 6. Example - Decorators -------------------")

print("\na.) calling a decorator on a function with one parameter:")
def date_name_decorator_03(param_function):
    def wrapper(*args):
        print(datetime.datetime.now())
        param_function(*args)
        print(datetime.datetime.now())
        print("")
    return wrapper

@date_name_decorator_03
def user_name_03(name):
    print(name)
user_name_03("Pavol")
user_name_03("Michal")
user_name_03("Fero")


print("\nb.) calling a decorator on a function with one parameter that is from a dictionary:\n")

visitors={
    "visitor_1":{
       "name": "Pavol",
        "age": 25 
    },
    "visitor_2":{
       "name": "Bubu",
        "age": 18 
    },
    "visitor_3":{
       "name": "Michal",
        "age": 17
    }
}

def is_adult_001(param_funct):
    def wrapper(param):
        if visitors["visitor_"+str(param)]["age"] >= 18:
            print("Visitor " + str(param) + ": " + visitors["visitor_"+str(param)]["name"] + " is adult.")
            param_funct(param)
        else:
            print("Visitor " + str(param) + ": " + visitors["visitor_"+str(param)]["name"] + " is too young.")
        print("")
    return wrapper

@is_adult_001
def play_movie_001(param_visitor):
    print(f"I am playing movie for {visitors['visitor_'+str(param_visitor)]['name']}.")
play_movie_001(1)
play_movie_001(3)
play_movie_001(2)


print("\nc.) calling a decorator on a function with two parameters that are from a dictionary:\n")
def is_adult_002(param_funct):
    def wrapper(param_vstrs, param_vstr):
        if param_vstrs["visitor_"+str(param_vstr)]["age"] >= 18:
            print("Visitor " + str(param_vstr) + ": " + param_vstrs["visitor_"+str(param_vstr)]["name"] + " is adult.")
            param_funct(param_vstrs, param_vstr)
        else:
            print("Visitor " + str(param_vstr) + ": " + param_vstrs["visitor_"+str(param_vstr)]["name"] + " is too young.")
        print("")
    return wrapper

@is_adult_002
def play_movie_002(all_visitors, param_visitor):
    print(f"I am playing movie for {all_visitors['visitor_'+str(param_visitor)]['name']}.")
play_movie_002(visitors, 1)
play_movie_002(visitors, 3)
play_movie_002(visitors, 2)



print("\n\n------------------- 7. Example - Decorators -------------------")

print("\na.) an example of a decorator that repeats the function call three times:")
def log_info_03(func):
    def wrapper(*args):
        for i in range(3):
            print(datetime.datetime.now())
            func(*args)
            print(datetime.datetime.now())
            print()
    return wrapper

@log_info_03
def send_pause_03(pause, name):
    print("The length of the pause is: " + str(pause) + " seconds.")
    time.sleep(pause)
    print(name)
send_pause_03(1, "Pvl")


print("\nb.) an example of a decorator that repeats the function call a specified number of times (n):")
def repeat_decorator_n_times(n_times):
    def log_info_04(func):
        def wrapper(*args):
            for j in range(n_times):
                print(datetime.datetime.now())
                func(*args)
                print(datetime.datetime.now())
                print()
        return wrapper
    return log_info_04

@repeat_decorator_n_times(n_times=5)
def send_pause_04(pause, name):
    print("The length of the pause is: " + str(pause) + " seconds.")
    time.sleep(pause)
    print(name)
send_pause_04(1, "Pvl")



print("\n")
