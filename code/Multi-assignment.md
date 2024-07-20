Multi-assingment is just a different approach that you can take to set variables.

Firstly, without multi-assignment, variables are assigned values individually. Therefore, each variable can only be printed one by one. On the other hand, with multi-assignment, multiple variables are assigned values in a single statement.

For example, in the code, the variables `age`, `name`, and `last_name` are assigned values simultaneously. The variable `MA` (short of multi-assignment—I know, it's clever—) captures all the values in a tuple, which can then be used to print all the values at once.

Some of the benefits of multi-assignment are:
- Allowment for more concise code by reducing the number of lines for variables.
- Make the code easier to read and understand.
- It can be used to unpack values from a list or tuple directly into variables.


## Example of Tuple Unpacking
```
flowers  =  ("Tulip", "bougainvillea", "Lily")
spring_bloom, tropical_vine, fragrant_perennial = flowers

print(spring_bloom)            #Output: Tulip
print(tropical_vine)           #Output: Bougainvillea
print(fragrant_perennial)      #Output: Lily
```
Using multiple assignment and tuple unpacking can simplify your code and make it more readable.

Made by danilo.zs
