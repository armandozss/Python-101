bre = "----------------------------------------------"
end = "This is all of Nested loops"

#-----------------------------------------------------------------------------------------------------------------

rows = int(input("How many rows do you want to put?: "))
columns = int(input("How many columns do you want to have in this?: "))
symbol = input("What symbol do you want to put?: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end="")

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
