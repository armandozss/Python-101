bre = "----------------------------------------------"
end = "This is all of functions"

#-----------------------------------------------------------------------------------------------------------------

def data (first_name, last_name, age):
    print("Hello " + first_name)
    print("your last name is " + last_name)
    print("you are " + str(age)  + " years old")

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = int(input("What is your age?: "))

# Break
print(" ")
print(bre)

data(first_name, last_name, age)

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
