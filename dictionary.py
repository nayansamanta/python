# dictionary in python 
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates


# phone_no_list={
#     "ram": 45698231,
#     "mohon":789653258,
#     "shyam":4569512357
# }

phone_no_list=dict(
    {
    "ram": 1234,
    "mohon":7896,
    "shyam":9512
}
)
# print(phone_no_list)
# print(phone_no_list["mohon"])
# phone_no_list['mohon']=999999   # here we upadate the phone no of mohon 
# print(phone_no_list)
# print(phone_no_list.get("ram"))
# if we want to delete the phone numebr of any person 
# del phone_no_list["shyam"]
# print(phone_no_list)  

# print(phone_no_list.keys())
# print(phone_no_list.values())
# print(phone_no_list.items())

for i in phone_no_list.items():
    print(i)