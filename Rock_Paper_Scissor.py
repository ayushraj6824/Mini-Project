import random
user_choice=int(input("Enter your choice:0 for Rock , 1 for Paper ,2 for Scissors :"))
if (user_choice>=3) or user_choice<0 :
    print("Invalid number")
else :
    computer_choice=random.randint(0,2)
    print("Computer choice :",computer_choice)
    if computer_choice== user_choice:
        print("Draw")
    elif computer_choice==0 and user_choice==2 :
        print("Lose")

    elif user_choice==0 and computer_choice==2:
        print("Win")
    elif computer_choice> user_choice:
        print("Lose")
    elif user_choice> computer_choice:
        print("Win")