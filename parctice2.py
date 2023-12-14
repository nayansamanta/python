n=int(input("enter range : "))
for i in range(1,n):
    if i%3==0 and i%5==0:
        print("fizzbuz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
print("complete the task ")