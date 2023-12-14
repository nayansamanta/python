import math

def wall():
    height = int(input("enter the height of the wall : "))
    width = int(input("enter the width of the wall : "))
    # 1 can hold 7 mt.sq area
    area = height*width   # area of the wall 
    number_of_can = math.ceil(area/7)
    return number_of_can

result = wall()

print(f"you have to buy {result} no of can ")