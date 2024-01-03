class Human:
    def __init__(self) -> None:
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class Male(Human):
    def __init__(self,name) -> None:
        super().__init__()  #by using supper we can acess the attribute of Human class  
        self.my_name=name
    def study(self):
        print("i am currently pursuing B.Tech ")
    def work(self):
        super().work()
        print("i can code ")

male_1=Male("Nayan")
# male_1.study()
# male_1.work()   # here inheritance is working 
# male_1.work()   # overwite the pervious one 
male_1.work()       # when we use the supper function we can also add the previous one method also 
print(male_1.num_eyes)
print(male_1.my_name)