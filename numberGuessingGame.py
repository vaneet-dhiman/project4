import random
random_num=random.randint(1,100)
attempts=10
while attempts>0 :
    user_guess=int(input("enter your number between 1 to 100"))
    if user_guess==random_num:
        print("Congratulation!")
        break
    elif random_num > user_guess:
        print("Too low")
    else:
        print("Too High")
    
    attempts-=1
    print("attempts left: ",attempts)
    if attempts==0:
        print("Game Over")
        print("correct number was: ",random_num)