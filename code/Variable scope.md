Variable scope refers to the accessibility of variables in different parts of your code.

## Basic example of global scope
*Global scope* means a variable defined outside any function or block is in the global scope. It can be accessed and modified from anywhere in the code. For example:
```
name = "Befuzs"

print(name)  # This will print "Befuzs"
```

## Basic example of local scope
*Local scope* means a variable is only accessible within the function where it is defined. For example:
```
def local():
    name = "Shisazs"
    print(name)  # This will print "Shisazs"

local()
```
In this case, `name` is defined inside the `local()` function and can't be accessed outside it. Thus, variable scope helps control where variables can be used, avoiding conflicts and keeping your code organized.

Made by danilo.zs
