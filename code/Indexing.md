Indexing is a way to access individual characters in a string (or elements in other sequences like lists and tuples) using their position within the sequence. In Python, indexing starts from 0, which means the first character of a string has an index of 0, the second character has an index of 1, and so on.

## Basic indexing
You can use square brackets `[]` to access a character at a specific index in a string.
```
name = "Befuzs Shisazs"
print(name[0])  #Output: B
```

## Slicing
Slicing allows you to access a range of characters in a string. You can use the colon `:` inside the square brackets to specify the start and end indices.
```
name = "Befuzs Shisazs"
first_name = name[:6]  #From the start to index 5
last_name = name[7:]   #From index 7 to the end

print(first_name)  #Output: Befuzs
print(last_name)   #Output: Shisazs
```

## Negative indexing
You can use negative indices to access characters from the end of the string. The index `-1` refers to the last character, `-2` to the second last, and so on.
```
print(name[-1])  #Output: s
print(name[-2])  #Output: z
```

## String manipulation using indexing
You can manipulate strings using indexing and slicing. For example, you can change the case of specific characters or extract parts of the string to create new strings.
```
name = "Befuzs Shisazs"

# Check if the first character is uppercase
if name[0].isupper():
    # Convert the whole string to lowercase
    name = name.lower()
print(name)  #Output: befuzs shisazs
```

## Difference between indexing and string slicing
Indexing retrieves a single character from a string at a specific position. Slicing extracts a substring by specifying a start and end position, allowing you to obtain multiple characters from the original string. Both use bracket notation but serve different purposes in string manipulation.

Made by danilo.zs
