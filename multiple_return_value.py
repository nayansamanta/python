import statistics

def mean_median_mode(list):
    return statistics.mean(list), statistics.median(list) , statistics.mode(list)

# print(mean_median_mode([5,6,4,5]))
a,b,c=mean_median_mode([5,6,4,5])
# print(f"a is ={a} \nb is ={b} and \nc is ={c}")

# #### return multiple value ########

def add(a,b):
    if a==0 and b==0:
        return None
    else:
        return a+b
var1=int(input("enter 1st no:"))
var2=int(input("enter 2nd no:"))

result=add(var1 , var2)
print(f"addition is {result}")