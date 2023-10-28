print("\n\n------------------------- COMPLEX EXAMPLES - MODULES ---------------------")
import time


print("\n\n------------------- 1. Example - Python built-in module - OS -------------------\n")
print("a.) Working with a directory:\n")
import os

not_directory = "NOT DIRECTORY"
empty_directory = "EMPTY DIRECTORY"

def load_game():
    list_of_files_in_directory = []
    dict_of_load_games = {}
    
    # check if directory 'saved_games' is EXIST, if not
    if os.path.isdir("saved_games/") is False:
        print("There are no Saved Games! Start the New Game!")
        return not_directory
    
    # check if directory 'saved_games' is EXIST, if yes
    elif os.path.isdir("saved_games/") is True: 
          
        # check if directory 'saved_games' is EMPTY, so if there aren't any files
        if not os.listdir("saved_games/"):
            print("There are no Saved Games! Start the New Game!")
            return empty_directory 
         
        # if directory 'saved_games' is NOT EMPTY, so if there are some files
        elif os.listdir("saved_games/"):
            # create list of saved games from all saved files
            saved_games_files = os.listdir("saved_games/")
            for i in saved_games_files:
                find_py = i.find(".py")
                find_txt = i.find(".txt")
                if "py" in i:
                    list_of_files_in_directory.append(i[:find_py])
                elif "txt" in i:
                    list_of_files_in_directory.append(i[:find_txt])
                else:
                    list_of_files_in_directory.append(i)
                            
            # create dictionary of saved games from all saved files
            for j in range(len(list_of_files_in_directory)):
                dict_of_load_games[j] = list_of_files_in_directory[j]  
            return dict_of_load_games

def which_saved_game_choose(param_dict_of_load_games):
    selected_load_game = ""
    while True:
        
        print("FILES IN DIRECTORY saved_games --->")
        # print saved games to choose
        for k, v in param_dict_of_load_games.items():
            print(k+1, "-", v)
            
        user_load_game_input = input("\nWhich saved game do you want to load: ") 
                              
        if user_load_game_input.isdecimal():
            user_load_game_input = int(user_load_game_input) - 1
            if user_load_game_input in param_dict_of_load_games.keys():
                print("\nYou choose this game:", param_dict_of_load_games[user_load_game_input])
                selected_load_game = param_dict_of_load_games[user_load_game_input]
                return selected_load_game
            else:
                print("\nout of range, try again!\n")
                continue   
        elif user_load_game_input in param_dict_of_load_games.values():
                print("\nYou choose this game:", user_load_game_input)
                selected_load_game = user_load_game_input
                return selected_load_game        
        else:
            print("\nout of range, try again!\n")
            continue

# This function returns dictionary of games to choose.
user_possibilities_to_choose = load_game()
# This function returns the user's chosen loaded game.
user_choose = which_saved_game_choose(user_possibilities_to_choose)
print("This is user choice:", user_choose)


time.sleep(2)

print("\n\nb.) Working with a file:\n")
list_of_files_in_directory_01 = []

# check if directory 'saved_games' is EXIST, if yes
if os.path.isdir("saved_games/") is True: 
    # if directory 'saved_games' is NOT EMPTY, so if there are some files
    if os.listdir("saved_games/"):
        # create list of saved games from all saved files
        saved_games_files = os.listdir("saved_games/")
        for i in saved_games_files:
            list_of_files_in_directory_01.append(i)

# files in directory
print("FILES IN DIRECTORY saved_games --->", list_of_files_in_directory_01)

# iterating through the list of files
for file in list_of_files_in_directory_01:
    # check if file is EXIST
    if os.path.exists("saved_games/" + str(file)):
        # if file is NOT EMPTY, so if there are some codes/chars/strings...
        if os.path.getsize("saved_games/" + str(file)):
            print("\nThis file -", file, "- exist and have some codes:")
            # print lines in file
            file_handler = open("saved_games/" + str(file), "r")
            for line in file_handler:
                print(line.strip())
            file_handler.close()            
        # if file is empty
        else:
            print("\nThis file -", file, "- exist, but is empty.")
    # if file is not exist
    else:
        print("This file is not exist.")

# if file is not exist
if os.path.exists("saved_games/" + "not_exist_file.py") is False:
    print("\nThis file - not_exist_file.py - is not exist.")


time.sleep(2)



print("\n\n------------------- 2. Example -  third-party Python module - Matplotlib -------------------\n")
print("a.) Pyplot - plotting graph:\n")
from random import randint
from matplotlib import pyplot as plt

numbers_for_plotting = []
for i in range(1, 10+1):
    numbers_for_plotting.append(randint(1, 6))
print(numbers_for_plotting)

plt.plot(numbers_for_plotting)
plt.show()



print("\n")
