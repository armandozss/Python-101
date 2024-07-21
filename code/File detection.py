bre = "----------------------------------------------"
end = "This is all of file detection"

#-----------------------------------------------------------------------------------------------------------------

# import
import os

#-----------------------------------------------------------------------------------------------------------------

path = "C:\\Users\\shisazs\\Documents\\PythonProjects\\TestDir"
path1 = "C:\\Users\\shisazs\\Documents\\PythonProjects\\TestDir"
path2 = "C:\\Users\\shisazs\\Documents\\PythonProjects\\TestDir\\example.txt"
path3 = "C:\\Users\\shisazs\\Documents\\PythonProjects"

if os.path.exists(path3):
    print("That location exists!!")
    if os.path.isfile(path2):
        print("That is a file")
    else:
        print("That isn't a file {}".format(":("))
    if os.path.isdir(path1):
        print("That is a directory")
    else:
        print("That isn't a directory {}".format(":("))
else:
    print("That location doesn't exists {}".format(":("))

# Break
print(bre)

# -----------------------------------------------------------------------------------------------------------------

# Else program

if 1 == 1:
    pass
    if os.path.exists(path):
        print("That location exists!!")
    else:
        print("That location doesn't exists {}".format(":("))
    if os.path.isfile(path1):
        print("That is a file")
    else:
        print("That isn't a file {}".format(":("))
    if os.path.isdir(path2):
        print("That is a directory")
    else:
         print("That isn't a directory {}".format(":("))
else:
    print("Hi {}".format(":)"))

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
