bre = "----------------------------------------------"
end = "This is all of logical operators"

#-----------------------------------------------------------------------------------------------------------------

# And, Or

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("It's a nice day, Go outside!!!")
elif temp <=0 or temp >=30:
    print("It's a really bad day, stay at home")

# Break
print(" ")
print(bre)

#-----------------------------------------------------------------------------------------------------------------

# Not

temp2 = int(input("What is the temperature outside?: "))

if not (temp2 >= 0 and temp2 <= 30):
    print("It's a nice day, Go outside!!!")
elif not (temp2 <= 0 or temp2 >= 30):
    print("It's a really bad day, stay at home")

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
