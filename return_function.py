def add(a , b):
    c=a+b
    # return c
    return  # if we dont return anything then it will show none 

result=add(5,4)   # here the value of c will repalce 
print(result)

# task : convert your name to title case 
def formated_name(f_name , l_name):
    f_name_final=f_name.title()
    l_name_final=l_name.title()
    return f"my name is : {f_name_final} {l_name_final}"
print(formated_name("nayan" , "Samanta"))