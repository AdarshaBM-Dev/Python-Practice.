'''age = int(input("Age : "))
print(age)
print(type(age))'''

Boy_name = input("Boy_name : ")
Boy_age = int(input("Boy_age : "))
Girl_name = input("Girl_name : ")
Girl_age = int(input("Girl_age : "))
age_diff = abs(Girl_age - Boy_age) #absolute + or - value
print(Girl_name + " love "+ Boy_name)
print(f"{Girl_name} loves {Boy_name}.Age difference is {age_diff}" )

