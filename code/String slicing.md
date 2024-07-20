String slicing allows you to access a subset of characters from a string. As its name indicates, it's a way to "slice" out part of the string by defining a start and end index, sometimes with a step.

## Basic syntax
```
string[start:end:step]
```
- `start`: The index where the slice starts.
- `end`: The index where the slice ends.
- `step`: How many characters to move forward or backwards (negative number) after each character is retrieved.

## Examples
```
name = "Befuzs Shisa"
```
- Slice from the start to end
```
name[0:6]      #Output: Befuzs
```
This will give us `"Befuzs"`. Remember that starts at index 0.

- Slice with default start and end
```
name[:]      #Output: Befuzs Shisa
```
If you omit the start and end, Python wll assume that you mean the entire string,

- Slice from a specific start to the end
```
name[7:]      #Output: Shisa
```
This starts at index 7 and goes to the end of the string.

- Slice from the start to a specific end
```
name[:6]      #Output: Befuzs
```
This starts at the beginning and ends before index 6.

- Slice with a step
```
name[::2]      #Output: Bfz hs
```
This starts at the beginning and selects every second character.

- Negative indexing
```
name[-5:]      #Output: Shisa
```
This starts at the 5 character from the end and goes to the end.

- Reverse a string
```
name[::-1]      #Output: asihS szufeB
```
Using `-1` will allow you to reverse a string.

## Slice function
A different approach that you can take is using the `slice()` function. This is used to create a slice object, which can then be used to specify how to slice a sequence such as a string.

The syntax is the same `slice(start, stop, step)`. The unique difference is that it serves as a standard so you don't need to type each time from where to where you want to slice a string.
```
website1  =  "https://google.com"
website2  =  "https://youtube.com"
slice  =  slice(8, -4)

print(website1[slice])      #Output: google
print(website2[slice])      #Output: youtube
```
This slice, starts at index 8 and stop at index -4.

The `slice()` function is a flexible way that you can use to create multiple slice objects with a fixed coordinates, so they can be reused and dynamically set.

Made by danilo.zs
