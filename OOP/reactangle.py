class AreaReactangle:
    def __init__(self , height , width) -> None:
        self.height=height
        self.width=width
    def formula(self):
        return 2* (self.height+self.width)
height=int(input("enter height :"))
width=int(input("enter width :"))
reactangle1=AreaReactangle(height, width)
print(reactangle1.formula())