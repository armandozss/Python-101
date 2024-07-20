Sets are an essential data structure in Python that allow you to store unique items. They are unordered and unindexed, making them perfect for membership testing and eliminating duplicate entries.

## Creating a set
You can create a set by placing items inside curly braces `{}`, separated by commas.
```
beverages = {"Water", "Fanta", "Sprite", "Coke", "Coffee"}
utensils = {"Fork", "Spoon", "Knife", "me"}
dishes = {"Bowl", "Plate", "Cup", "me"}
```

## Adding items to a set
You can add a new item to a set using the `add()` method.
```
utensils.add("napkin")
print(utensils)
```

## Removing items from a set
You can remove an item from a set using the `remove()` method.
```
utensils.remove("Fork")
print(utensils)
```

## Updating a set
You can add items from another set to an existing set using the `update()` method.
```
dishes.update(utensils)
print(dishes)
```

## Union of sets
You can combine multiple sets using the `union()` method, which returns a new set containing all unique items from the original sets.
```
dinner_table = utensils.union(dishes, beverages)
print(dinner_table)
```

## Looping through a set
You can use a `for` loop to iterate through the items in a set.
```
for x in dinner_table:
    print(x, end=" ")
```

## Difference between sets
You can find the difference between two sets using the `difference()` method, which returns items that are in the first set but not in the second.
```
print(dishes.difference(utensils))
```

## Intersection of sets
You can find the intersection of two sets using the `intersection()` method, which returns items that are present in both sets.
```
print(dishes.intersection(utensils))
```

Feel free to explore the complete code in the repository for further practice!

Made by danilo.zs
