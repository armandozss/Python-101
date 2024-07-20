bre = "----------------------------------------------"
end = "This is all of string slicing"

#-----------------------------------------------------------------------------------------------------------------

# Index = [start:stop:skip]

name = "Befuzs Shisa"
weird_name = name[:5:1]
weird_name2 = name[::2]
weird_name3 = name[::-1]

print(weird_name)
print(weird_name2)
print(weird_name3)

# Break
print(" ")
print(bre)

#-----------------------------------------------------------------------------------------------------------------

# Slice = (start,stop,step)

website = "https://google.com"
website2 = "https://youtube.com"
slice = slice(8,-4)

print(website[slice])
print(website2[slice])

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
