class Human:
    def __init__(self , num_heart) -> None:
        print("i am 1st calling ")
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("i can eat")
    def cook(self):
        print("i can cook")  

class Male:
    def __init__(self , name) -> None:
        print("i am 2nd calling")
        self.my_name=name
    def work(self):
        print("i can work")
    def cook(self):
        print("i can cook egg")  

class Boy(Human,Male):   # here if we change the order of parent class name output is also different but it is not a good practice 
    def __init__(self,name , heart , language) -> None:
        Human.__init__(self, heart)
        Male.__init__(self,name)
        self.my_language=language   #here language is own argument of Boy class 
    def sleep(self):
        print("i can sleep")
    def cook(self):
        print("i can cook chiken")

boy_1=Boy("nayan" ,1, "python")

# boy_1.eat()
# boy_1.cook()  # within child class in which order we have written those parent name  ...output will be also in same order ..thats why output is " i can cook "

# Male.cook(boy_1)    # it is good practice 
# boy_1.sleep()

# MRO = method resolution order 
# print(Boy.mro())    #[<class '__main__.Boy'>, <class '__main__.Human'>, <class '__main__.Male'>, <class 'object'>]

print(f"hii i am {boy_1.my_name} and i teach {boy_1.my_language}")