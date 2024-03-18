import random

target = random.randint(1,100)

while True:
    userNum = int(input("Guess the number: "))

    if(userNum==target):
        print("You won....")
        break
    elif(userNum>target):
        print("Guess more less Number")
    else:
        print("Guess more big Number")

print("......Game Over.....")