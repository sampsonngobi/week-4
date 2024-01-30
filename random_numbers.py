"""
team assighnment 
Core requirements

Plan
1. import the random lib

2. Write two functions 
    1. main - no parameter
        creates a list 
        prints the number list 
        calls the append_number_function with one argurment(numbers)
        prints the number list 
        calls the append_number_function again with two argurments(numbers , quantity-3)
        prints the number list 

    2. append_random_numbers - 2 parameters - (number_list , quantity = 1)
        loope through quantity and while in range
        gets random numbers using the random.uniform
        round the random number to 1 decimal place using the round function 
        append the rounded number to the number list


Add a function named append_random_words that meets the following criteria:
Has two parameters: a list named words_list and an integer named quantity. The parameter quantity has a default value of 1
Randomly selects quantity words from a list of words and appends the selected words at the end of words_list.
Add statements in the main function that create a list of words, call the append_random_words function, and then print the list of words.
Add something or change something in your program that you think would make your program better, easier for the user, more elegant, or more fun. Be creative.

"""

import random

random_words_list = ["Lion" , "Chicken" , "hippo", "Pig", "Elephant", "Duck", "Fox", "Swan","Apple", "Cat", "Dog", "Cow", "Sheep"]

def main():

    numbers = [16.2, 75.1, 52.3]
    print(f"Numbers: {numbers}")

    append_random_numbers(numbers)
    print(f"Numbers: {numbers}")

    append_random_numbers(numbers, 3)
    print(f"Numbers: {numbers}")

    words = []
    print(f"Words {words}")

    append_word_function(words)
    print(f"Words {words}")

    append_word_function(words, 3)
    print(f"Words {words}")



def append_random_numbers(number_list, quantity=1):

    for n in range(quantity):
        random_number = round(random.uniform(1, 100), 1)
        number_list.append(random_number)

    return number_list


def append_word_function(word_list, quantity=1):

    for w in range(quantity):
        random_word = random.choice(random_words_list)

        if len(word_list) == len(random_words_list):
             print("All available words added")
             break
        else:
             while random_word in word_list:
                random_word = random.choice(random_words_list)
                

        word_list.append(random_word)

    return word_list

if __name__ == "__main__":
    main()