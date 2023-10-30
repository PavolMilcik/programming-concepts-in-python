print("\n\n-------------------- COMPLEX EXAMPLES - FILE HANDLING --------------------")


print("\n\n------------------- 1. Example - file handling - write -------------------")
print("a.) Create a new file and write to it.")
# create a new file and write to it
file_writer_01 = open("file_handler_folder/data_file.txt", "w")
my_number_list_01 = list(range(0, 10+1))
for number_a in my_number_list_01:
    if number_a == my_number_list_01[-1]:
        file_writer_01.write(str(number_a))
    else:
        file_writer_01.write(str(number_a) + "\n")
file_writer_01.close()

# read from an existing file
file_reader_01 = open("file_handler_folder/data_file.txt", "r")
for line_e in file_reader_01:
    print(line_e.strip(), end=" ")
file_reader_01.close()



print("\n\n\n------------------- 2. Example - file handling - read -------------------")
print("a.) Read from an existing file.")
# create a list from an existing file
file_reader_02 = open("file_handler_folder/data_file.txt", "r")
my_number_list_02 = []
for number in file_reader_02:
    number = number.strip()
    number_int = int(number)
    my_number_list_02.append(number_int)
print(my_number_list_02)

# read a list from an existing file
for number_b in my_number_list_02:
    if number_b == my_number_list_02[-1]:
        print(str(number_b))
    else:
        print(str(number_b), end=", ")
file_reader_02.close()



print("\n\n------------------- 3. Example - file handling - append -------------------")
print("a.) Append to an existing file.")
# append to an existing file
file_appender_01 = open("file_handler_folder/data_file.txt", "a")
my_number_list_03 = [11, 12, 13, 14, 15]
for number_c in my_number_list_03:
    file_appender_01.write("\n" + str(number_c))
file_appender_01.close()

# read from an existing file with new appended numbers
file_reader_03 = open("file_handler_folder/data_file.txt", "r")
for line_e in file_reader_03:
    print(line_e.strip(), end=" ")
file_reader_03.close()



print("\n\n\n------------------- 4. Example - file handling - write -------------------")
print("a.) Read an existing file, create new files, and write either even or odd numbers to them.")
# create new files with even numbers and odd numbers
file_reader_04 = open("file_handler_folder/data_file.txt", "r")
file_writer_02 = open("file_handler_folder/data_file_even_numbers.txt", "w")
file_writer_03 = open("file_handler_folder/data_file_odd_numbers.txt", "w")
for number_d in file_reader_04:
    number_d = number_d.strip()
    int_number_d = int(number_d)
    if int_number_d % 2 == 0 and int_number_d != 0:
        file_writer_02.write(str(int_number_d) + "\n")
    elif int_number_d % 2 != 0 and int_number_d != 0:
        file_writer_03.write(str(int_number_d) + "\n")
file_reader_04.close()
file_writer_02.close()
file_writer_03.close()

# read from an even numbers file
file_reader_05 = open("file_handler_folder/data_file_even_numbers.txt", "r")
for line_e in file_reader_05:
    print(line_e.strip(), end=" ")
file_reader_05.close()

print()
# read from an odd numbers file
file_reader_06 = open("file_handler_folder/data_file_odd_numbers.txt", "r")
for line_e in file_reader_06:
    print(line_e.strip(), end=" ")
file_reader_06.close()



print("\n\n\n------------------- 5. Example - file handling - write -------------------")
print("a.) Read an existing file, create a new file, and write the numbers from the end to the beginning.")
# create new file - the numbers from the end to the beginning
file_reader_07 = open("file_handler_folder/data_file.txt", "r")
file_writer_04 = open("file_handler_folder/data_file_end_to_beginning.txt", "w")
my_number_list_04 = []
for number_e in file_reader_07:
    number_e = number_e.strip()
    int_number_e = int(number_e)
    my_number_list_04.append(int_number_e)
print(my_number_list_04)

for i in range(len(my_number_list_04)-1, 0-1, -1):
    if i == 0:
        file_writer_04.write(str(my_number_list_04[i]))
    else:
        file_writer_04.write(str(my_number_list_04[i]) + "\n")
file_reader_07.close()
file_writer_04.close()

# read from - the numbers from the end to the beginning
file_reader_08 = open("file_handler_folder/data_file_end_to_beginning.txt", "r")
for line_e in file_reader_08:
    print(line_e.strip(), end=" ")
file_reader_08.close()



print("\n")
