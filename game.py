import random

computer_moves = {
    1 : "rock",
    2 : "papper",
    3 : "scissors"
}

def rock():
    if computer_choice == "rock":
        print("tie")
    elif computer_choice == "papper":
        print("you lost")
    else:
        print("you won")

def papper():
    if computer_choice == "rock":
        print("you won")
    elif computer_choice == "papper":
        print("tie")
    else:
        print("you lost")

def scissors():
    if computer_choice == "rock":
        print("you lost")
    elif computer_choice == "papper":
        print("you won")
    else:
        print("tie")

# def user_moves_switcher(usr_arg):
switcher = {
    "rock" : rock(),
    "papper" : papper(),
    "scissors" : scissors(), 
    }
    
    # return switcher.get(usr_arg, "input invalid")
    

def computerInput(): 
    r = random.randint(1, 3)
    return computer_moves.get(r)

user_choice = input("rock / papper / scissors: ")
while user_choice.lower() != "exit":
    computer_choice = computerInput()
    print("You: " + user_choice)
    print("Computer: " + computer_choice)
    funct = switcher.get(user_choice, "Invalid")
    user_choice = input("rock / papper / scissors: ")
    

