bre = "----------------------------------------------"
end = "This is all of dictionaries"

#-----------------------------------------------------------------------------------------------------------------

capitals = {"Usa":"Washington DC",
            "Nicaragua":"Managua",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals["Russia"])

print(capitals.get("Germany"))

# Break
print(" ")
print(bre)

print(capitals.keys())
print(capitals.values())
print(capitals.items())

# Break
print(" ")
print(bre)

for key,value in capitals.items():
    print(key, value)

# Break
print(" ")
print(bre)

capitals.update({"Germany":"Berling"})
print(capitals)

# Break
print(" ")
print(bre)

capitals.pop("China")
print(capitals)

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)


#Made by danilo.zs
