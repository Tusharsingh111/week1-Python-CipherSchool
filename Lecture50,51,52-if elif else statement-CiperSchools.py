# if else condition
# show tickets pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
#above 60 (200)

age = input("enter your age please :")
age = int(age)

if  0<age<3:
    print("ticket price : free")
elif 3<age<10:
    print("ticket price :150")
elif 10<age<60:
    print("ticket price : 250")
else:
    print("ticket price : 200")


#in keyword
name = "nishant"
if 'n' in name:
    print("'n' is present in name")
else:
    print("not present")


# check empty or not
# important
name = "abc"
if name: # true if string is not empty
    print("string is not empty")
else:
    print("string is empty")


    name = ""
if name: # true if string is not empty
    print("string is not empty")
else:
    print("string is empty")
