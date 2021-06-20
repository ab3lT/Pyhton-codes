import random

random_value = random.randint(0,1)

gender = input("please put your gues gender")

if(gender == "male" and random_value == 1):
    print("your gues was correct")
elif(gender =="female" and random_value == 0):
    print("your guees was correct")
else:
    print("your gues is incorrect")

print(random_value)
