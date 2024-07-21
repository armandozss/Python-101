bre = "----------------------------------------------"
end = "This is all of exception handling"

#-----------------------------------------------------------------------------------------------------------------

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a / b
except ZeroDivisionError as e:
    print("You can't divide by 0 LMFAO")
except ValueError as e:
    print("Enter only entire numbers please")
except Exception as e:
    print("Enter only numbers please")
else:
    print(c)
finally:
    print("This will always appear")

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
