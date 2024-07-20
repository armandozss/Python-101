bre = "----------------------------------------------"
end = "This is all of For loops"

#-----------------------------------------------------------------------------------------------------------------

# import
import time

#-----------------------------------------------------------------------------------------------------------------

# Basic
for i in range(10):
    print(i+1)

# Break
print(" ")
print(bre)

for i in ("Hello"):
    print(i,end="")

# Break
print(" ")
print(bre)

for i in range (50,55+1):
    print(i, end=" ")

# Break
print(" ")
print(bre)

#-----------------------------------------------------------------------------------------------------------------

# Advanced
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Nice, " + "I hope that I'm learning something new")

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
