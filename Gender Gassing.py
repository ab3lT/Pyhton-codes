from string import * 

x = 0

while int(x) != 1:

         gender = input("please give us gener ")

         if gender == "male".lower() or gender == "femal".lower():
                  if gender.upper() == "FEMAL":
                           print("gender is femal")
                  else:
                           print("gender is Male")
         else:
                  print("unknow gender")
         x = input("if you want me to exit insert 1 if not insert other number")
