Keyword arguments in Python allow you to pass arguments to functions by explicitly naming them. This approach improves code readability and allows arguments to be provided in any order.

## Basic example
```
def cheers(first, middle, last):
    print("Hello " + first + " " + middle + " " + last + " ")

cheers(middle="Flaito", first="Befuzs", last="Shisazs")
```
In this function, `cheers` expects three parameters: `first`, `middle`, and `last`. When calling the function, you can use keyword arguments to specify values. By naming the arguments (middle, first, and last), you can provide values in any order. Python matches each value to the corresponding parameter by name, not by position.

Using keyword arguments is helpful when functions have many parameters or when you want to make your code clearer by explicitly stating what each value represents.

Made by danilo.zs
