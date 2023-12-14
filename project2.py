import random
print("welcome to password generator ! ")
letter_list=[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L" , "M", "N", "O", "P", "Q", "R" "S", "T",  "V","W", "X","Y", "Z" ]
symbols_list=["$","%","^","&","*", "_" , "-", "+", "=", "<" ,">","?" ]
number_list=["1", "2", "3","4","5","6","7","8","9","10"]
n1=int(input("how many letters would you want in your password : "))
n2=int(input("how many symbol would you want in your password : "))
n3=int(input("how many number would you want in your password : "))
random_letters = random.sample(letter_list, n1)
random_symbol= random.sample(symbols_list, n2)
random_number= random.sample(number_list, n3)

# Concatenate the lists and shuffle them
password_characters = random_letters + random_symbol + random_number
random.shuffle(password_characters)   
# print(password_characters)

# Convert the list to a string
password = ''.join(password_characters)
print(password)
