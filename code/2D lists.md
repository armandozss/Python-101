A 2D list is primarily a list that contains other lists as its elements.

There are different ways to create a 2D list.

A common method for beginners is demonstrated in the code. This method involves creating separate lists for different categories and then combining them into a new single list. To print a specific item from the 2D list, you need to use two different values, being the first one referring to the menu list and the second value the item that you want to display within the list.

For example if you want to print Lemonade from the menu list, you should call `menu[0]` to accesses the drinks list, and `[3]` to accesses the fourth item. (Remember that in Python, lists start at index 0.)

Another method involves creating a 2D list by nesting lists inside another list. To access an element within the list you need to use two values as in the first method, being your first value the row and the second value the column.

```
menu = [
    ["coffee", "Tea", "Soda", "Lemonade"],
    ["Pizza", "Sushi", "Spaguetti", "Hot dog"],
    ["Ice cream", "Pudding", "Cake"]
]
```

For example, to print Pudding, first you need to call `menu[2]` to accesses the "desserts" category, and `[1]` to accesses the second item. (Again, Python lists start at index 0.)

Made by danilo.zs
