import random
c=["rock", "paper", "scissors"]
user=input("Rock,paper or scissors?Enter 1, 2, 3 respectively ")
comp= random.choice(c)
while user=="1":
    if comp=="rock":
        print("Computer picked rock. TIE")
        break
    elif comp=="paper":
        print("Computer picked paper. You lose")
        break
    else:
        print("Computer picked scissors. You win")
        break
while user=="2":
    if comp=="rock":
        print("Computer picked rock. You win")
        break
    elif comp=="paper":
        print("Computer picked paper. TIE")
        break
    else:
        print("Computer picked scissors. You lose")
        break
while user=="3":
    if comp=="rock":
        print("Computer picked rock. You lose")
        break
    elif comp=="paper":
        print("Computer picked paper. You win")
        break
    else:
        print("Computer picked scissors. TIE")
        break 