class Instructor:
    def __init__(self,instructor_name , instructor_adress) -> None:
        self.name=instructor_name       # here attribute is name and adress 
        self.adress=instructor_adress
        self.flowers=0      # we can set default value also 
instructor_1=Instructor("Nayan", "delhi")
instructor_2=Instructor("sayan", "pune")
print(instructor_1.name)
print(instructor_2.name)