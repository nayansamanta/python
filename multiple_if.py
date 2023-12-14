age=int(input("enter your age :"))
take_pictur=input("you want to take photos: ")
if age<12:
    if take_pictur=="yes":
        print("you have to pay 150 rs ")
        print(f"you have to pay total {150+50} also ")
    else:
        print(f"you have to pay total {150} also ")
elif age<18:
    if take_pictur=="yes":
        print("you have to pay 250 rs ")
        print(f"you have to pay total {250+50} also ")
    else:
            print(f"you have to pay total {250} also ")
else:
    if take_pictur=="yes":
        print("you have to pay 500 rs ")
        print(f"you have to pay total {500+50} also ")
    else:
        print(f"you have to pay total {500} also ")