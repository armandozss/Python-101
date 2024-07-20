Tuples are a fundamental data structure in Python that are similar to lists, but with one key difference: tuples are immutable, meaning once you create a tuple, you cannot change its contents. This immutability makes tuples useful for storing data that should not be modified.

## Creating a tuple
You can create a tuple by placing items inside parentheses `()`, separated by commas.
```
student = ("Befuzs", 14, "male")
```

## Accessing tuple items
You can access items in a tuple by their index, with the first item having an index of 0. Negative indices count from the end of the tuple, with `-1` being the last item.

## Finding the index of an item
You can use the `index()` method to find the index of an item in a tuple.

## Checking for an item in a tuple
You can use the `in` keyword to check if an item exists in a tuple.
```
if "Befuzs" in student:
    print("Befuzs is here")
```
## Looping through a tuple
```
for x in student:
    print(x, end=" ")
```
Feel free to explore the complete code in the repository for further practice!

Made by danilo.zs
