print("\n\n------------ COMPLEX EXAMPLES - FIBONACCI SEQUENCE AND PRIME NUMBERS ------------")


print("\n\n------------------- 1. Example - Fibonacci Sequence -------------------\n")
# a = 0
# b = 1
# c = a + b ---> 1

# a = b ---> a = 1
# b = c ---> b = 1
# c = a + b ---> 2

# a = b ---> a = 1
# b = c ---> b = 2
# c = a + b ---> 3

# a = b ---> a = 2
# b = c ---> b = 3
# c = a + b ---> 5

# a = b ---> a = 3
# b = c ---> b = 5
# c = a + b ---> 8

print("a.) Fibonacci Sequence")
def fibonacci_sequence_01():
    while True:
        try:
            user_limit_number = int(input("Write the number up to which the Fibonacci sequence will be generated: "))
        except ValueError:
            print("\nWrite only integer number!\n")
            continue
        if user_limit_number > 2:
            print("")
            break
        else:
            print("\nWrite integer number bigger than 2!\n")
            
    a = 0
    b = 1
    print(a)
    print(b)
    c = a + b
    while c <= user_limit_number:
        print(c)
        a = b
        b = c
        c = a + b
        
fibonacci_sequence_01()


print("\nb.) Fibonacci Sequence")
def fibonacci_sequence_02():
    while True:
        try:
            user_number_of_fibbos = int(input("How much Fibonacci numbers will be generated: "))
        except ValueError:
            print("\nWrite only integer number!\n")
            continue
        if user_number_of_fibbos > 0:
            print("")
            break
        else:
            print("\nWrite integer number bigger than 0!\n")
            
    fibo_seq_list = [0, 1]
    while len(fibo_seq_list) < user_number_of_fibbos:
        next_number = fibo_seq_list[-2] + fibo_seq_list[-1]
        fibo_seq_list.append(next_number)
    return fibo_seq_list

print(fibonacci_sequence_02())



print("\n\n------------------- 2. Example - Prime Numbers -------------------")
# Prime numbers are natural numbers greater than 1,
# that have only two distinct positive divisors: 1 and themselves.

def prime_numbers_01():
    while True:
        try:
            user_limit_number = int(input("Write the number up to which the prime numbers sequence will be generated: "))
        except ValueError:
            print("\nWrite only integer number!\n")
            continue
        if user_limit_number > 9:
            print("")
            break
        else:
            print("\nWrite integer number bigger than 9!\n")
            
    count_prime_numbers = 0
    prime_numbers_list = []
    for number in range(2, user_limit_number+1):
        count_modulos = 0 
        for i in range(1, number+1):
            if number % i == 0:
                count_modulos += 1
            if count_modulos > 2:
                break
        if count_modulos <= 2:
            count_prime_numbers += 1
            prime_numbers_list.append(number)
                  
    return count_prime_numbers, prime_numbers_list

number_of_prime_numbers, all_prime_numbers = prime_numbers_01()
print("This is the number of all prime numbers in your sequence:", number_of_prime_numbers, "\n")
print("These are all the prime numbers in your sequence:\n" + str(all_prime_numbers))



print("\n")
