String formatting lets you create strings with dynamic content. Python provides several methods to format strings, including using `str.format()`, `f-strings`, and the `%` operator. We'll focus on `str.format()` here.

## Basic syntax
- Positional arguments
```
animal = "fox"
item = "moon"
print("The {} jumped over the {}".format(animal, item))
```
This inserts the variables into the placeholders `{}` in the order they appear.

- Indexed arguments
```
print("The {1} jumped over the {0}".format(animal, item))
```
This specifies the position of the arguments with indices, {0} and {1}, in the string.

- Named arguments
```
print("The {animal} jumped over the {item}".format(item="moon", animal="fox"))
```
This allows you to use named arguments to be inserted into the placeholders.

- Reuse format strings
```
text = "The {} jumped over the {}"
print(text.format(animal, item))
```
You can store the format string in a variable and use it multiple times.

## Advanced formatting
- Padding and alignment
```
name = "befuzs"
print("Hello {:10}".format(name))        # Pad to 10 characters
print("Hello {:>10}".format(name))       # Right-align
print("Hello {:<10}".format(name))       # Left-align
print("Hello {:^10}".format(name))       # Center-align
```

- Formatting numbers
```
num = 3.141592
print("pi is equal to {:.2f}".format(num))  # Float with 2 decimal places
```

- Thousand separators
```
num2 = 500000
print("The num is {:,}".format(num2))  # Add commas for thousands
```

- Different number systems
```
print("The num is {:b}".format(num2))  # Binary
print("The num is {:o}".format(num2))  # Octal
print("The num is {:X}".format(num2))  # Hexadecimal (uppercase)
print("The num is {:x}".format(num2))  # Hexadecimal (lowercase)
```

- Scientific notation
```
print("The num is {:E}".format(num2))  # Scientific notation (uppercase)
print("The num is {:e}".format(num2))  # Scientific notation (lowercase)
```

String formatting is a powerful feature for creating dynamic and readable strings, making your code more versatile and user-friendly.

Made by danilo.zs
