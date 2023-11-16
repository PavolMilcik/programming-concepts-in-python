print("\n")



print("\n-------------------- Find the largest and the smallest number in the list --------------------")
unsorted_list = [2, 32, 1, 6, 5, 58, 1, -3, 4, 3, 58, 21]
print(unsorted_list)

print("\na.) using Python's built-in functions:")
largest_nmb = max(unsorted_list)
print(largest_nmb)
smallest_nmb = min(unsorted_list)
print(smallest_nmb)


print("\nb.) the largest number in the list, determined by my solution:")
max_number = unsorted_list[0]
for number in unsorted_list:
    if number >= max_number:
        max_number = number
print(max_number)


print("\nc.) the smallest number in the list, determined by my solution:")
min_number = unsorted_list[0]
for number in unsorted_list:
    if number <= min_number:
        min_number = number
print(min_number)



print("\n\n\n--------------------- Sort the numbers in the list using my solution ---------------------")
unsorted_lst = [2, 32, 1, 6, 5, 58, 1, -3, 4, 3, 58, 21]
print(unsorted_lst)

print("\na.) sort the numbers in the list using Python's built-in functions:")
sorted_list_from_front = sorted(unsorted_lst)
print(sorted_list_from_front)
sorted_list_from_back = sorted(unsorted_lst, reverse=1)
print(sorted_list_from_back)


print("\nb.) sort the list from the smallest to the largest numbers, according to my solution:")
sorted_list_smallest_to_largest = []
for i in unsorted_list:
    number = max(unsorted_list)
    for j in unsorted_list:
        if j <= number and j not in sorted_list_smallest_to_largest:
            number = j
        elif j <= number and j in sorted_list_smallest_to_largest:
            if unsorted_list.count(j) != sorted_list_smallest_to_largest.count(j):
                number = j
    sorted_list_smallest_to_largest.append(number)
print(sorted_list_smallest_to_largest)


print("\nc.) sort the list from the largest to the smallest numbers, according to my solution:")
sorted_list_largest_to_smallest = []
for i in unsorted_list:
    number = min(unsorted_list)
    for j in unsorted_list:
        if j >= number and j not in sorted_list_largest_to_smallest:
            number = j
        elif j >= number and j in sorted_list_largest_to_smallest:
            if unsorted_list.count(j) != sorted_list_largest_to_smallest.count(j):
                number = j
    sorted_list_largest_to_smallest.append(number)
print(sorted_list_largest_to_smallest)



print("\n\n\n----------------- Sort the numbers in the list using the Bubble Sort algorithm -------------------")
unsorted_array = [2, 32, 1, 6, 5, 58, 1, -3, 4, 3, 58, 21]
print(unsorted_array)

print("\na.) sort the list from the smallest to the largest numbers:")
for n in unsorted_array:
    for i in range(len(unsorted_array)-1):
        current_number = unsorted_array[i]
        next_number = unsorted_array[i+1]
        if current_number >= next_number:
            unsorted_array[i+1] = current_number
            unsorted_array[i] = next_number
print(unsorted_array)


print("\nb.) sort the list from the largest to the smallest numbers:")
for n in unsorted_array:
    for i in range(len(unsorted_array)-1):
        current_number = unsorted_array[i]
        next_number = unsorted_array[i+1]
        if current_number <= next_number:
            unsorted_array[i+1] = current_number
            unsorted_array[i] = next_number
print(unsorted_array)



print("\n\n\n----------------- Sort the numbers in the list using the Bubble Sort algorithm -------------------")
print("----------------- Additionally, use the 'stop' function when the list is sorted -------------------")

print("\na.) sort the list from the smallest to the largest numbers:")
import random
random_numbers = random.sample(range(-10, 20), 10)
print(random_numbers)


def is_list_sorted_smallest_to_largest(param_list):
    counter = 0
    for i in range(len(param_list)-1):
        if param_list[i] <= param_list[i+1]:
            counter += 1
    if counter >= len(param_list)-1:
        return True
    else:
        return False

# the same function as above, but shorter:
# print(all(random_numbers[i] <= random_numbers[i+1] for i in range(len(random_numbers)-1)))

for n in random_numbers:
    for i in range(len(random_numbers)-1):
        current_number = random_numbers[i]
        next_number = random_numbers[i+1]
        if current_number >= next_number:
            random_numbers[i+1] = current_number
            random_numbers[i] = next_number
            if is_list_sorted_smallest_to_largest(random_numbers):
                break
    if is_list_sorted_smallest_to_largest(random_numbers):
                print("\nThe list is sorted from the smallest to the largest numbers:")
                break 
print(random_numbers)


print("\n\nb.) sort the list from the largest to the smallest numbers:")
import random
random_numbers = random.sample(range(-10, 20), 10)
print(random_numbers)


def is_list_sorted_largest_to_smallest(param_list):
    counter = 0
    for i in range(len(param_list)-1):
        if param_list[i] >= param_list[i+1]:
            counter += 1
    if counter >= len(param_list)-1:
        return True
    else:
        return False

# the same function as above, but shorter:
# print(all(random_numbers[i] >= random_numbers[i+1] for i in range(len(random_numbers)-1)))

for n in random_numbers:
    for i in range(len(random_numbers)-1):
        current_number = random_numbers[i]
        next_number = random_numbers[i+1]
        if current_number <= next_number:
            random_numbers[i+1] = current_number
            random_numbers[i] = next_number
        if is_list_sorted_largest_to_smallest(random_numbers):
                break
    if is_list_sorted_largest_to_smallest(random_numbers):
                print("\nThe list is sorted from the largest to the smallest numbers:")
                break          
print(random_numbers)



print("\n")
