# List is a collection which is ordered and changeable. Allows duplicate members.

roll_no =[1,18,6,9,8,-1,-65,85]
names=["nayan", "mukunda","sayan", "biplab" , "parthib"]
mix_list=["nayan" , 10 , 54.36, "sayan", True, 85]

print(roll_no)
roll_no.sort()
print(roll_no)
roll_no.append(4596)
print(roll_no)
roll_no.insert(2,69)
print(roll_no)
roll_no.remove(4596)
print(roll_no)
print("#######")
print(names[2])
print(mix_list)
print(len(mix_list))
print(mix_list[-1])
print(mix_list[-2])

# slicing 
print(names[1:4])
print(names[:4])
print(names[0:])