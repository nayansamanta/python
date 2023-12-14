# 0 for rock 
# 1 for paper 
# 2 scissor 
import random

my_choice=int(input("enter your choice : "))
num=[0,1,2]
computer_choice=random.choice(num)
print("computer choice is : ",computer_choice)

if my_choice==computer_choice:
    print("draw! play again")
elif computer_choice>my_choice:
    print("computer win ")
elif my_choice>computer_choice:
    print("i am win ")
elif computer_choice==2 and my_choice==0:
    print("i am win ")
elif computer_choice==0 and my_choice==2:
    print("computer win")
else:
    print("best of luck ")