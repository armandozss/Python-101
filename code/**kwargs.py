bre = "----------------------------------------------"
end = "This is all of **kwargs"

#-----------------------------------------------------------------------------------------------------------------

def dictionary(**kwargs):
    print("Hello ", end="")
    for key, value in kwargs.items():
        print(value, end="")

dictionary(tittle="Mr. ", first="befuzs ", last="shisazs")

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
