''' a=10
def dispaly():
    a=a+1   #cannot access local variable 'a' where it is not associated with a value  ...we can not modefied global variable in local scope 
    print(a)
dispaly()   '''

# ####  but if we want to modefied the value : ########
'''a=10
def dispaly():
    global a
    a=a+2
    print(a)
dispaly()  '''

def dispaly():
    a=20
    def show():
        global a
        a=30
        print(f"inside show function {a}")
    print(f"outside show function {a}")
    show()
    print(f"inside display function {a}")
dispaly()
print(f"outside display function {a}")  # here a is 30 because we defiend a in show function as globally 


name ="nayan"
def nam():
    global name
    name=name+" samanta"
    print(name)
# print(name)
nam()
print(name)
