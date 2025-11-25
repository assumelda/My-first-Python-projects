import random
rock='''                 
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_
'''
paper=''' _ __   __ _ _ __   
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
'''
scissors='''                              
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ 
|___/\___|_|___/___/\___/|_|  |___/
'''
rps=[rock, paper, scissors]
print("Welcome to the Rock Paper Scissors game!!")
me=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
computer=random.randint(a=0, b=2)
print(f"You choose: {rps[me]}")
print(f"computer chose: {rps[computer]}")
if me==0:
    if me==0 and computer==2:
        print("You win!")
    elif me==0 and computer==1:
        print("You lose. Computer Wins!")
    else:
        print("This is a tie")
        
elif me==1:
    print(paper)
    if me==1 and computer==0:
        print("You win!")
    elif me==1 and computer==2:
        print("You lose. Computer Wins!")
    else:
        print("This is a tie")
        
elif me==2:
    print(scissors)
    if me==2 and computer==1:
        print("You win!")
    elif me==2 and computer==0:
        print("You lose. Computer Wins!")
    else:
        print("This is a tie")


# # 2nd Method
# if me == computer:
#     print("It's a tie!")
# elif (me == 0 and computer == 2) or (me == 1 and computer == 0) or (me == 2 and computer == 1):
#     print("You win!")
# else:
#     print("You lose. Computer wins!")
