student_details={
    "Ram":{"roll_no":10, "age":22 , "course":"python"},
    "Mohon":{"roll_no":11, "age":25 , "course":"Java"},
}

# print(student_details["Ram"])
# print(student_details["Ram"]["course"])

############ if we want to add any data in dictionary then -    ############

# student_details["Ram"]["Phone_no"]=825624986
# print(student_details["Ram"])
# print(student_details["Ram"].pop("Phone_no"))
# del student_details["Ram"]["Phone_no"]
# print(student_details["Ram"]) 

# nesting a list in dictionary ##############
travel_data={
    "kolkata":["eco-park" , "park-street" , "victoria"],
    "Darjeeling":["Ghum" , "silong"]
}
# print(travel_data)
# print(travel_data["kolkata"])
# print(travel_data["kolkata"][0])

####### nesting dict in a list ########

student_data=[
    { 
     "name": "ram",
     "roll_no":10, 
     "age":22 , 
     "course":"python"
     },
    {
     "name": "Mohon",
     "roll_no":11, 
     "age":25 , 
     "course":"Java"},
]
print(student_data)
print(student_data[0])
print(student_data[0]["name"])