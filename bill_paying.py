import random

frinds=input("Enter your friends' names separated by spaces: ")
arry=frinds.split()
random.shuffle(arry)
random_person = random.choice(arry)
print("Randomly selected person is :", random_person)
print(f"{random_person} will pay the bill  ")