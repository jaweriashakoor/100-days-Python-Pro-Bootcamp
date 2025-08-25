# enemies="Jaweria" # global varibale
# def my_function():
#     enemies="Jiya" # local variable that is declared inside the the function
#     print(enemies)
# my_function()
# print(enemies)


# enemies=1 
# def my_function():
#     global enemies  # global keyword is used to modify the outside declared globle variable inside the function
#     enemies+=1 
#     print(enemies)
# my_function()
# print(enemies)


# pi=3.14
# GOOGLE_COM="https://www.google.com"

# def my_func():
#     print(GOOGLE_COM)

# my_func()

from random import randint


EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(user_guess,actual_answer):
    if user_guess> actual_answer:
        print("Too High")
    elif user_guess < actual_answer:
        print("Too Low")
    else:
        print(f"You Got It! Thw answer is {actual_answer}")


def set_difficulty():
    level=input("Choose a Difficulty 'Easy' or 'Hard'?").lower()
    if level=="easy":
        global turns
        return EASY_LEVEL_TURNS

    else:
        return HARD_LEVEL_TURNS
    
print("Welcome to a Number Guessing Game!")
print("I am Guessing of a number between 1 and 100")
answer = randint(1,100)
print(f"YES! The actual answer is {answer}")



turns=set_difficulty
print(f"You Have {turns} attempts remaining to guess the number.")
guess=int(input("Make a Guess"))
check_answer(guess,answer)