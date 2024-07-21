bre = "----------------------------------------------"
end = "This is all of string format"

#-----------------------------------------------------------------------------------------------------------------

animal = "fox"
item = "moon"

# 1st
print("The {} jumped over the {}".format(animal, item))

print(bre)

# 2nd
print("The {1} jumped over the {0}".format(animal, item))

print(bre)

# 3rd
print("The {animal} jumped over the {item}".format(item="moon", animal="fox"))

print(bre)

# 4th
text = "The {} jumped over the {}"
print(text.format(animal, item))

print(" ")
print(bre)

#-----------------------------------------------------------------------------------------------------------------

name = "befuzs"

print("Hello {}".format(name))

print(bre)

# Add space

print("Hello {:10}, nice to meet u".format(name))

print(bre)

# Left align

print("Hello {:>10}".format(name))

print(bre)

# Right align

print("Hello {:<10}, nice to meet you".format(name))

print(bre)

# Center

print("Hello {:^10}, nice to meet you".format(name))

print(" ")
print(bre)

# Numbers

num = 3.141592

print("pi is equal to {:.2f}".format(num))

print(bre)

# ,

num2 = 500000

print("The num is {:,}".format(num2))

print(bre)

# Binary

print("The num is {:b}". format(num2))

print(bre)

# Octal number

print("The num is {:o}".format(num2))

print(bre)

# Hexadecimal

print("The num is {:X}".format(num2))
print("The num is {:x}".format(num2))

print(bre)

# Scientific notation

print("The num is {:E}".format(num2))
print("The num is {:e}".format(num2))

#-----------------------------------------------------------------------------------------------------------------

# End
print(" ")
print(bre)
print(end)

#Made by danilo.zs
