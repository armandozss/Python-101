Lists are a fundamental data structure in Python that allow you to store multiple items in a single variable. You can think of a list as a collection of items, all grouped together in a single, ordered sequence.

## Creating a list
You can create a list by placing items inside square brackets `[]`, separated by commas.
```
food = ["Pizza", "Spaghetti", "Hot dog", "Pudding"]
```
In this example, food is a list containing four items.

## Modifying list
Lists are mutable, meaning you can change their contents after they are created. Here’s how you can modify a list:

- Accessing Items: You can access items in a list by their index, with the first item having an index of 0. Negative indices count from the end of the list, with `-1` being the last item.
```
print(food[-1])  #Output: Pudding
```
- Updating Items: You can change an item in a list by accessing its index and assigning a new value.
```
food[-1] = "Sushi"
print(food)  #Output: ['Pizza', 'Spaghetti', 'Hot dog', 'Sushi']
```
- Adding Items: Use the `append()` method to add an item to the end of the list.
```
food.append("Ice cream")
print(food)  #Output: ['Pizza', 'Spaghetti', 'Hot dog', 'Sushi', 'Ice cream']
```
- Removing Items: Use the `remove()` method to delete an item by its value. If the item is not found, it will raise a `ValueError`.

## Looping through list
You can use a for loop to iterate through the items in a list. This is useful for performing actions on each item.
```
for x in food:
    print(x, end=" ")
```
This loop prints each item in the food list, separated by a space.

Summary
- Lists: A collection of items stored in a single variable.
- Accessing: Use indices to get items from the list.
- Updating: Modify items by accessing their index.
- Adding: Use append() to add new items.
- Removing: Use remove() to delete items by value.
- Looping: Use a for loop to iterate through items.

Made by danilo.zs
