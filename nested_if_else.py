country=input("enter your country name : ")
if country=="india":
    print("you can paly the game but you have to pay somthing ")
    age=int(input("enter your age : "))
    if age>=18:
        print("pay only 250")
    else:
        print("pay only 500")
    print("carry on , best of luck ")
else:
    print("you can not play the game , you can go home ")                                
