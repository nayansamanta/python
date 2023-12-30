class CalculateArea:
    pi=3.14     # here pi is class object attribute 
    def __init__(self , r) -> None:
        self.radious=r
    def findarea(self):
        return self.pi*(self.radious)*(self.radious)
    
radious_meter=int(input("enter the radious of the circle:"))
circle1=CalculateArea(radious_meter)
result=circle1.findarea()
print(result)