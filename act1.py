import random 
x=True
num=str(random.randint(10,20))
print(num)
print("please try to guess a number between 10 to 20")
while x:
 guess=(input("Please guess the number- "))
 if guess==num :
  print("You won!")
  break
 else :
  print("please try again")
