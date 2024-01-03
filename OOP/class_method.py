class Method:
    flowers=0       # it is class object variable
    def __init__(self , my_name , my_sarname) -> None:
        self.f_name=my_name
        self.l_name=my_sarname

    def dispaly(self, subject): # this will accept subject as a string 
        print(f"hiii i am {self.f_name} and i will teach you {subject}")

    def flowers_count(self , flowers_name):
        self.flowers+=1
        print(flowers_name)

person1=Method("Nayan", "Samanta")
print(f"hello i am {person1.f_name}")
person1.dispaly("python")
person1.flowers_count("zoya")
print(f"Now my flowers is {person1.flowers}")

person2=Method("niraj", "walia")
print(person2.flowers)  #it will show 0