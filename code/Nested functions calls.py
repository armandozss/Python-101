bre = "----------------------------------------------"
end = "This is all of nested function calls"

#-----------------------------------------------------------------------------------------------------------------

# Without nested function calls

num = input("Put a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)

print(num)

# Break
print(" ")
print(bre)

#-----------------------------------------------------------------------------------------------------------------

# With nested function calls

print(round(abs(float(input("Put a whole positive number: ")))))

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
