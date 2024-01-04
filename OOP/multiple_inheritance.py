class Human:
    def eat(self):
        print("i can eat")
    def cook(self):
        print("i can cook")  

class Male:
    def work(self):
        print("i can work")
    def cook(self):
        print("i can cook egg")  

class Boy(Human,Male):   # here if we change the order of parent class name output is also different but it is not a good practice 
    def sleep(self):
        print("i can sleep")
    def cook(self):
        print("i can cook chiken")

boy_1=Boy()
# boy_1.eat()
# boy_1.cook()  # within child class in which order we have written those parent name  ...output will be also in same order ..thats why output is " i can cook "

Male.cook(boy_1)    # it is good practice 
boy_1.sleep()