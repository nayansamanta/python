name1=input("enter your name : ")
name2=input("enter his/her name : ")
full_name=name1+name2
update_name=full_name.lower()

t= update_name.count('t')
r= update_name.count('r')
u= update_name.count('u')
e= update_name.count('e')

true = t+r+u+e

l= update_name.count('l')
o= update_name.count('o')
v= update_name.count('v')
e= update_name.count('e')

love = l+o+v+e

score=str(true)+str(love)
print("love calcilate score is ",score)