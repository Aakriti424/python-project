import random
n=[1,2,3,4,5,6,7,8,9]
com=random.choice(n)
user= int(input("Enter a number from 1 to 9: "))
while com>user:
    d=com-user
    if d<=4:
        print("Your number is low")
        break
    else:
        print("Your number is very low")
        break
while com<user:
    di=user-com
    if di<=4:
        print("Your number is high")
        break
    else:
        print("Your number is very high")
        break
while com==user:
    print("You guessed the right number")
    break
    