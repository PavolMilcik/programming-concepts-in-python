# ------------------------- 6 Complex Examples - For and While loops -----------------------


print("\n\n------------------ 1. Example ---------------------")
# **
# **
# **
print("a.) for loop:\n")

rows = 3
columns = 2
for row in range(0, rows):
    for star in range(0, columns):
        print("*", end="")
    print()

print("\nb.) while loop:\n")

rows = 3
while rows > 0:
    columns = 2
    while columns > 0:
        print("*", end="")
        columns -= 1
    print("")
    rows -= 1



print("\n------------------- 2. Example -------------------")
# *
# **
# ***
# **
# *
print("a.) for loop:\n")

rows = 3
for row in range(0, rows):
    for star in range(0, row+1):
        print("*", end="")
    print("")
for row in range(0, rows):
    for star in range(rows-1, row, -1):
        print("*", end="")
    print("")

print("b.) while loop:\n")

rows = 3
while rows > 0:
    stars = 3
    while stars+1 > rows:
        print("*", end="")
        stars -= 1
    print("")
    rows -= 1
    
rows = 2
while rows > 0:
    stars = rows
    while stars > 0:
        print("*", end="")
        stars -= 1
    print("")
    rows -= 1



print("\n------------------ 3. Example --------------------")
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
print("a.) for loop:\n")

rows = 5
for row in range(rows):
    for number in range(0, row+1):
        print(number+1, end=" ")
    print("")
for row in range(rows):
    for number in range(1, rows - row):
        print(number, end=" ")
    print("")    

print("b.) while loop:\n")

rows = 5
columns = 1
while rows > 0:
    number = 1
    while number <= columns:
        print(number, end=" ")
        number += 1
    print()
    rows -= 1
    columns += 1
    
rows = 5
while rows > 0:
    number = 1
    while number < rows:
        print(number, end=" ")
        number += 1
    print()
    rows -= 1



print("------------------- 4. Example -------------------")
# Print the characters of the string from the end to the beginning.
# Pavol ---> lovaP
print("a.) for loop:")

name_01 = "Pavol"
print(name_01)
for i in range(len(name_01)-1, 0-1, -1):
    print(name_01[i], end="")

print("\n\nb.) while loop:")

name_02 = "Pavol"
print(name_02)
i = len(name_02) - 1
while i >= 0:
    print(name_02[i], end="")
    i -= 1



print("\n\n------------------- 5. Example -------------------")
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
print("a.) for loop:\n")

rows = 6
for row in range(rows):
    for space in range(rows, row, -1):
        print(" ", end="")
    for star in range(0, row+1):
        print("* ", end="")
    print("")

print("\nb.) while loop:\n")

rows = 6
columns = rows
while rows > 0:
    space = rows
    while space > 0:
        print(" ", end="")
        space -= 1
    star = (columns - rows) + 1
    while star > 0:
        print("* ", end="")
        star -= 1
    print("")
    rows -=1



print("\n------------------- 6. Example -------------------")
#     *
#    * *
#   * * *
#  * * * *
#   * * *
#    * *
#     *
print("a.) for loop:\n")

rows = 4
for row in range(rows):
    for space in range(rows, row, -1):
        print(" ", end="")
    for star in range(0, row+1):
        print("* ", end="")
    print("")
rows = 3                   
for row in range(rows):
    for space in range(0, row+2):
        print(" ", end="")
    for star in range(rows, row, -1):
        print("* ", end="")
    print("")


print("\nb.) while loop:\n")

rows = 4
columns = rows
while rows > 0:
    space = rows
    while space > 0:
        print(" ", end="")
        space -= 1
    star = (columns - rows) + 1
    while star > 0:
        print("* ", end="")
        star -= 1
    print("")
    rows -=1

rows = 3
columns = rows
while rows > 0:
    space = (columns - rows) + 2
    while space > 0:
        print(" ", end="")
        space -= 1
    star = rows
    while star > 0:
        print("* ", end="")
        star -= 1
    print("")
    rows -=1


print("\n")
