# Name
# Weight in kilograms
# Height in meters
name=input('your name')
weight=float(input('ur weight in kilogram'))
height=float(input('ur heigh in meter'))
print("name:",name)
print("weight:",weight)
print("height:",height)

body_max_index=weight/(height*height)
print("your BMI",body_max_index)

