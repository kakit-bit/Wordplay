# Script chooses a random word from a .csv file and provides clues

import random

# User input error check
def is_yn(value):
    if value == "Y" or value == "y" or value == "N" or value =="n":
        return True
    else:
        return False

# Function Opens .csv to import and create a list of words
def harvest_csv():
    import csv
    target_file = open("wordplay_dex.csv")
    csv_reader_object = csv.reader(target_file)

    wordplay_list = []

    for item in csv_reader_object:
        wordplay_list.append(item)

    return wordplay_list

# Function shuffles imported word list and chooses random word from list
def fetch_random_word():
    word_list = harvest_csv()
    #random.shuffle(word_list)

    return word_list[random.randint(0,len(word_list)-1)]

# Clue 1 Function returns word length
def find_word_length(target_word):
    return len(target_word[0])

# Clue 2 Function returns number of vowels
def detect_vowels(target_word):
    vowels = ["a","e","i","o","u","y"]
    word_analysis = target_word[0]
    num_vowels = 0
    for letter in word_analysis:
        if letter not in vowels:
            pass
        else:
            num_vowels +=1
    return num_vowels

# Clue 3 Function returns first and last letter
def first_last(target_word):
    word_analysis = target_word[0]
    first = word_analysis[0]
    last = word_analysis[len(word_analysis)-1]
    return first, last

# Wordplay Control Function
def start_wordplay(target_word):
    while True:
        user_guess = input("Enter your guess: ")
        if (user_guess) == (target_word[0]):
            print("Correct!")
            break
        else:
            continue

# Check if user wants to play
def get_yn(target_word):
    while True:
        user_input = input("Would you like to Play (Y/N)?: ")
        if not is_yn(user_input):
            print("Not a valid input")
            continue
        elif user_input.upper() == "N":
            break
        elif user_input.upper():
            return False

if __name__ == '__main__':

    target_word = fetch_random_word()

    if get_yn(target_word) == False:
        # Clue 1
        print("Clue 1#: The word has", find_word_length(target_word), "letters.")
        # Clue 2
        print("Clue 2#: There are", detect_vowels(target_word), "vowels in the word.")
        # Clue 3
        print("Clue 3#: The first letter of the word is", target_word[0][0].upper(), "and last letter of the word is", target_word[0][len(target_word[0])-1].upper())
        start_wordplay(target_word)