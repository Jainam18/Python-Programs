import random
num = random.randint(1,101)
name = input("Enter Your name : ")
nguesses = 1
guess = int(input("Enter a Number : "))
while(not(guess == num)):
    if(guess>num):
        print("Enter A Lower Number")
    else:
        print("Enter A Higher Number")    
    guess = int(input("Enter a Number Again : "))    
    nguesses = nguesses + 1
with open("highscore.txt","r") as f:
    highscore = int(f.read())
if (highscore > nguesses):
    with open("highscore.txt","w") as f:
        f.write(str(nguesses))
    print("You have Broken Your Highest Score and Achieved New Milestone !!")
print(f"Congratulations {name}!!, You have Guessed The Number In {nguesses} attempts")