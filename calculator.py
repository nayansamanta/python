def addition(a,b):
    return a+b
def subtruction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divition(a,b):
    return a/b

operation_dict={
    "+":addition,
    "-":subtruction,
    "*":multiplication,
    "/":divition
}

def calculator():
    number1=int(input("enter 1st number:"))
    for symbol in operation_dict:
            print(symbol)

    continueCalculation=True
    while continueCalculation:
        op_symbol=input("pick an operation:") # "+"
        number2=int(input("enter next number:"))

        calculate=operation_dict[op_symbol] #add
        output=calculate(number1 , number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue=input(f"Enter 'yes' to continue calculation with {output} or enter 'no' for fresh calculation and enter 'X' to exit :").lower()

        if should_continue=="yes":
            number1=output
        elif should_continue=="no":
            continueCalculation=False
            calculator()
        else:
            continueCalculation=False
            print("bye!")
calculator()