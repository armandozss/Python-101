bre = "----------------------------------------------"
end = "This is all of Sets"

#-----------------------------------------------------------------------------------------------------------------
beverages = {"Water", "Fanta", "Sprite", "Coke", "Coffee"}
utensils = {"Fork", "Spoon", "Knife", "me"}
dishes = {"Bowl", "Plate", "Cup", "me"}
print(utensils)

# Break
print(" ")
print(bre)

utensils.add ("napkin")
print(utensils)

# Break
print(" ")
print(bre)

utensils.remove("Fork")
print(utensils)

# Break
print(" ")
print(bre)

dishes.update(utensils)
print(dishes)

# Break
print(" ")
print(bre)

dinner_table = utensils.union(dishes, beverages)
print(dinner_table)

for x in dinner_table:
    print(x, end=" ")

# Break
print(" ")
print(bre)

print(dishes.difference(utensils))

# Break
print(" ")
print(bre)

print(dishes.intersection(utensils))

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
