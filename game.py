import random

computer_moves = {
    1 : "rock",
    2 : "papper",
    3 : "scissors"
}

def printResults(arg1, arg2):
    print("You: " + arg1)
    print("Computer: " + arg2)
    

def rock(arg):
    if arg == "rock":
        print("tie")
    elif arg == "papper":
        print("you lost")
    else:
        print("you won")

def papper(arg):
    if arg == "rock":
        print("you won")
    elif arg == "papper":
        print("tie")
    else:
        print("you lost")

def scissors(arg):
    if arg == "rock":
        print("you lost")
    elif arg == "papper":
        print("you won")
    else:
        print("tie")

def computerInput(): 
    r = random.randint(1, 3)
    return computer_moves.get(r)
user_choice = input("rock / papper / scissors: ")
while user_choice.lower() != "exit":
    computer_choice = computerInput()
    
    if user_choice == "papper":
        if computer_choice == "papper":
            printResults(user_choice, computer_choice)
            print("Tie")
            user_choice = input("rock / papper / scissors: ")
            
        elif computer_choice == "rock":
            printResults(user_choice, computer_choice)
            print("You Lost")
            user_choice = input("rock / papper / scissors: ")
            
        else: 
            printResults(user_choice, computer_choice)
            print("You Won !!!!!")
            user_choice = input("rock / papper / scissors: ")
            
    elif user_choice == "scissors":  
        if computer_choice =="rock":
            printResults(user_choice, computer_choice)
            print("You lost")
            user_choice = input("rock / papper / scissors: ")
            
        elif computer_choice == "papper":
            printResults(user_choice, computer_choice)
            print("You won !!!!!")
            user_choice = input("rock / papper / scissors: ")
            
        else: 
            printResults(user_choice, computer_choice)
            print("Tie")
            user_choice = input("rock / papper / scissors: ")
            
    elif user_choice == "rock":    
        if computer_choice == "papper":
            printResults(user_choice, computer_choice)
            print("You lost")
            user_choice = input("rock / papper / scissors: ")
            
        elif computer_choice == "rock":
            printResults(user_choice, computer_choice)
            print("Tie")
            user_choice = input("rock / papper / scissors: ")
            
        else: 
            printResults(user_choice, computer_choice)
            print("You Won !!!!!")
            user_choice = input("rock / papper / scissors: ")
    elif user_choice == "exit":
        break 
    else: 
        print("Wrong choice")
        user_choice = input("rock / papper / scissors: ")

