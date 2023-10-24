# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # User Word Check
    # Make while loop for menu
    done = False
    while not done:
        print("\n--MAIN MENU--")
        print("- 1: Spell Check a word (Linear Search) -")
        print("- 2: Spell Check a word (Binary Search) -")
        print("- 3: Spell Check Alice in Wonderland (Linear Search) - ")
        print("- 4: Spell Check Alice In Wonderland (Binary Search) - ")
        print("- 5: Exit - ")
        # Get User Input
        selection = input("Please Enter Menu Selection (1-5): ")


        # Spellcheck a word Linear
        if selection == "1":
            # Start time
            start_time = time.time()
            word_selection = input("Please enter a word: ")
            # Start linear search
            print("\nLinear Search starting...")
            word_index = linearSearch(dictionary, word_selection)
            # Print results
            if word_index == -1:
                # End time and get total time
                end_time = time.time()
                total_time = end_time - start_time
                print(f"{word_selection} is not in the dictionary.({total_time} seconds)")
            else:
                # End time and get total time
                end_time = time.time()
                total_time = end_time - start_time
                print(f"{word_selection} is in the dictionary at position {word_index}.({total_time} seconds)")

        # Spellcheck a word binary
        elif selection == "2":
            # Start time
            start_time = time.time()
            word_selection = input("Please enter a word: ")
            # Start binary search
            print("\nBinary Search starting...")
            word_index = binarySearch(dictionary, word_selection)
            # Print results
            if word_index == -1:
                # End time and get total time
                end_time = time.time()
                total_time = end_time - start_time
                print(f"{word_selection} is not in the dictionary. ({total_time} seconds)")
            else:
                # End time and get total time
                end_time = time.time()
                total_time = end_time - start_time
                print(f"{word_selection} is in the dictionary at position {word_index}. ({total_time} seconds)") 

        # Spellcheck a word Alice in Wonderland Linear
        elif selection == "3":
            print("\nLinear Search starting...")
            words_not_found = 0
            
            for i in range(len(aliceWords)):
                word_index = linearSearch(dictionary, aliceWords[i])
                if word_index == -1:
                    words_not_found += 1
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Number of words not found in the dictionary: {words_not_found}({total_time} seconds)")

        # Spellcheck a word Alice in Wonderland Binary
        elif selection == "4":
            print("\nBinary Search starting...")
            words_not_found = 0
            start_time = time.time()
            for i in range(len(aliceWords)):
                word_index = binarySearch(dictionary, aliceWords[i])
                if word_index == -1:
                    words_not_found += 1
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Number of words not found in the dictionary: {words_not_found}({total_time} seconds)")
        # Exit
        elif selection == "5":
            done = True

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

# Linear Search Function
def linearSearch(a_list, item):
            for i in range(len(a_list)):
                if a_list[i] == item:
                    return i
            return -1

# Binary search function
def binarySearch(a_list, item):
    lower_index = 0
    higher_index = len(a_list) - 1
    while lower_index <= higher_index:
        middle_index = math.floor((lower_index + higher_index) / 2)
        if item == a_list[middle_index]:
            return middle_index
        elif item < a_list[middle_index]:
            higher_index = middle_index - 1
        elif item > a_list[middle_index]:
            lower_index = middle_index + 1
    return -1


# Call main() to begin program
main()
