def greet(fname , lname):
    print(f"hii {fname} {lname} how are you ?")

# greet("nayan" , "samanta")

def addition(num1 , num2):
    num3=num1+num2
    print(num3)
# addition(5,5)

def greet1(fname , lname):
    print(f"hii {fname} {lname}")
    print("how are you?")
# greet1(lname="samanta" , fname="nayan" )

def bio(name , subject, dept="cs"):     # default argument 
    print(f"hii i am {name} i love {subject} and i am in now {dept}")

# bio("nayan" , "math" , )
# bio("jeet" , "english" , "ECE" )


# arbitaery arguments 
def add(*numbers):   #(5,6,7)
   c=0
   for i in numbers:
       c=c+i
   print(f"sum is {c}")
    
# add(5,6,7)
# add(5,6,7 ,10,7,53,12)

def infoname(**person):
    for key,value in person.items():
        print(key , value)

infoname(name="nayan" , title="samanta" , age="20" )
infoname(name="shyam" , village="malida")