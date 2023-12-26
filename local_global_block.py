b=15  #global 
def dispaly():
    a=10    #local
    # print(a)  
    def show():
        print(a)  
    show()
dispaly()
# print(b)