print("\n\n------------------ COMPLEX EXAMPLES - TRY-EXCEPT -----------------")


print("\n\n------------------- 1. Example - Try-Except -------------------")
def choose_index():
    while True:
        numbers_list = [5, 8, 7, 1]
        print("choose any index from list:", numbers_list)
        user_input_index = input("index number: ") 
        try:
            result = numbers_list[int(user_input_index)]
        except IndexError as e:
            print("\nerror:", e, "\n")
            continue
        except ValueError as e:
            print("\nerror:", e, "\n")
            continue
        except Exception as e:
            print(e)
            continue
        print(result)   
        break
        # or instead of 'print(result)' and then 'break,' we simply use 'return result' but without break!
choose_index()
# or instead 'choose_index()', we use 'print(choose_index())'



print("\n\n------------------- 2. Example - Try-Except -------------------")
print("a.) Tuples as the return value from a function:")
def return_user_name_age():
    while True:
        try:
            user_input_name = input("Write your name: ")
        except Exception as e:
            print(e)
            continue
        if len(user_input_name) == 0:
            print("\nWrite any name, but no number, only string!\n")
            continue
        elif user_input_name.isalpha():
            break
        else:
            print("\nInvalid input. Please enter a valid string.\n")
            continue
    while True:
        try:
            user_input_age = int(input("Write your age: "))
        except Exception as e:
            print("\nwrite only int number!\n")
            continue
        if user_input_age > 0:
            break
        else:
            print("\nInvalid input. Please enter age bigger than 0.\n")
    return user_input_name, user_input_age

user_name, user_age = return_user_name_age()
print("\nUser name:", user_name)
print("User age:", user_age)



print("\n")
