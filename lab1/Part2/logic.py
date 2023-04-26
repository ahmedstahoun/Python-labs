#!/usr/bin/env python

# ---------------- 1 -----------------

# def remove_duplicates(list):
#     new_list = []
#     for i in list:
#         if i not in new_list:
#             new_list.append(i)

#     return new_list

# entered_list = input("please enter numbers separated by comma  ")
# entered_list = entered_list.split(',')

# new_list = remove_duplicates(entered_list)
# print(f"list without commas {new_list}")

# ---------------- 2 -----------------

# def front_back(a,b):
#     a_length = len(a)
#     b_length = len(b)
#     a_half = a_length // 2 + a_length%2 
#     b_half = b_length // 2 + b_length%2 
#     return a[:a_half] + b[:b_half] + a[a_half:] + b[b_half:]

# print(front_back('abc', 'xy')) 


# ---------------- 3 -----------------

# def is_different(seq):
#     return len(set(seq)) == len(seq)
# print(is_different([1,5,7,9]))  
# print(is_different([1,5,5,7,9])) 

# ---------------- 4 -----------------

# def bubble_sort(list):
#     n = len(list)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#                 swapped = True
#         if not swapped:
#             break
#     return list

# print(bubble_sort([2,1,5,7,6]))

# ---------------- 5 -----------------
import random

def guesses_game():
   
    secret_number = random.randint(1, 100)
    tries = 10
    prev_guesses = []
    
    while tries > 0:
        user_guess = input("Guess a number between 1 and 100: ")
        if not user_guess.isdigit() or int(user_guess) < 1 or int(user_guess) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        user_guess = int(user_guess)
        
        if user_guess in prev_guesses:
            print("You already guessed that number. Try again.")
            continue
        
        tries -= 1
        prev_guesses.append(user_guess)

        if user_guess == secret_number:
            print("Congratulations! You guessed the number in", 10 - tries, "tries.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == 'y':
                guesses_game()
            else:
                print("Thanks for playing!")
            return
        
        elif user_guess < secret_number:
            print("Too low. Guess again.")
        else:
            print("Too high. Guess again.")

    print("Sorry, you ran out of tries. The number was", secret_number)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        guesses_game()
    else:
        print("Thanks for playing!")

guesses_game()