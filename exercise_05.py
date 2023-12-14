# wap days weak and months u have until you reach 90 years old 
age = int(input("enter your age : "))

years_left=90-age
days_left=years_left * 365
weak_left=years_left * 52
month_left= years_left *12
print(f"you have {days_left} days and {weak_left} weak and {month_left} month and {years_left} year ")