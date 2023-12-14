
def prime_number(number):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                print(f"{number} is not prime ")
                break
        else:
            print(f"{number} is prime ")
    else:
        print(f"{number} is not prime")

N=int(input("enter the number : "))

prime_number(number=N)