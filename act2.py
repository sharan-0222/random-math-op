import random
choi= ["rock","paper","scissor"]
compchoice= random.choice(choi)
co=input("please select between rock paper or scissors- ")
print(compchoice)
if compchoice==co:
    print("it is a tie")
elif (compchoice=="scissors") and (co=="paper"):
    print("you lost")
elif (compchoice=="paper") and (co=="rock"):
    print("you lost")
elif (compchoice=="rock") and (co=="scissor"):
    print("you lost")
else :
    print("you win")