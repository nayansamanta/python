student_marks={
    "jenny":92,
    "harry":78,
    "dimpy":56,
    "rahul":41,
    "ankit":99,
    "prem":34,
}


#     (91, 100): "A+",
#     (81, 90): "A",
#     (71, 80): "B+",
#     (61, 70): "B",
#     (51, 60): "C",
#     (41, 50): "D",


student_grade={

}

for student in student_marks:  #jenny
    mark=student_marks[student] #92
    if mark>90:
        student_grade[student]="A+"
    elif mark>80:
        student_grade[student]="A"
    elif mark>70:
        student_grade[student]="B+"
    elif mark>60:
        student_grade[student]="B"
    elif mark>50:
        student_grade[student]="C"
    elif mark>40:
        student_grade[student]="D"
    else:
        student_grade[student]="F"

print(student_grade)