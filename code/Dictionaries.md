Dictionaries are a fundamental data structure in Python that allow you to store data in key-value pairs. They are mutable, unordered collections, making them perfect for managing associative arrays where you can look up values by unique keys.

## Creating a dictionary
You can create a dictionary by placing key-value pairs inside curly braces `{}`, separated by commas. Each key is followed by a colon `:` and its associated value.
```
capitals = {"USA": "Washington DC",
            "Nicaragua": "Managua",
            "China": "Beijing",
            "Russia": "Moscow"}
```

## Accessing values
You can access values in a dictionary by using their corresponding keys.
```
print(capitals["Russia"])  #Output: Moscow
```

If you try to access a key that does not exist, it will raise a `KeyError`. To avoid this, you can use the `get()` method, which returns `None` if the key is not found.
```
print(capitals.get("Germany"))  #Output: None
```

## Viewing keys, values, and items
You can view all the keys, values, or key-value pairs (items) in a dictionary.
```
print(capitals.keys())  #Output: dict_keys(['USA', 'Nicaragua', 'China', 'Russia'])
print(capitals.values())  #Output: dict_values(['Washington DC', 'Managua', 'Beijing', 'Moscow'])
print(capitals.items())  #Output: dict_items([('USA', 'Washington DC'), ('Nicaragua', 'Managua'), ('China', 'Beijing'), ('Russia', 'Moscow')])
```

## Looping through a dictionary
You can use a `for` loop to iterate through the key-value pairs in a dictionary.
```
for key, value in capitals.items():
    print(key, value)
```

## Adding and updating items
You can add a new key-value pair or update an existing key's value using the `update()` method or by directly assigning a value to a key.
```
capitals.update({"Germany": "Berlin"})
print(capitals)

# Or directly:
capitals["Germany"] = "Berlin"
print(capitals)
```

## Removing items
You can remove a key-value pair from a dictionary using the `pop()` method.
```
capitals.pop("China")
print(capitals)
```

Made by danilo.zs


