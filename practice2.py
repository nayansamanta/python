#  we have to add new data in this list 

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

new_student = {
    "name": "John",
    "roll_no": 12,
    "age": 20,
    "course": "C++"
}

student_data.append(new_student)
print(student_data)