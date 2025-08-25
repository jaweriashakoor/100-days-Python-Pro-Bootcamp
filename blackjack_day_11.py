import random
list1=[11,2,3,4,5,6,7,8,9,10,10,10,10]

should_continue=True
# my_choice1=int(input("Enter your card number\n"))
# my_choice2=int(input("Enter your card\n"))
while should_continue:
    my_choice1= 8
    my_choice2=10
    my_list=[my_choice1,my_choice2]
    print(f"Your Card : {my_list}")
    sum1=sum(my_list)
# print(f"Sum of your cards is : {sum1}")
    computer_choice1=random.choice(list1)
    computer_choice2=random.choice(list1)
    computer_list=[computer_choice1,computer_choice2]
    print(f"Compuer cards: {computer_list}")
    sum2=sum(computer_list)
# print(f"Sum of Computer cards is : {sum2}")

    card=input("Type 'y' to get another card, type 'n' to pass")
    if card=="n":
        if sum1> sum2:
            print("You Won")
        else:
            print("You lose")








