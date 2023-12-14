import random

a=[1,2,5,4,8,789,785,3,6,9,2,58,962]
b=random.randint(0,10)
print(b)
# a=random.randrange(1,4)  # 1 included but 4 not 
# a=random.random()    #0.0 to 1.0 but 1.0 is not included
list=[2,8,-89,100]
# a=random.choice(list)
random.shuffle(list)
print(list)