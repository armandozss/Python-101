Math functions are operations provided by the built-in `math` module. These functions perform various mathematical operations such as calculating powers, square roots, and so on.

Firs of all, you need to import the `math` module before using its functions. You can achieve this by using the `import` statement, which is used to bring in modules and their functions, classes, and variables into your code so you can use them.

Its usage is as simple as writing `import math`. This will import the entire `math` module, so you can use any function or variable defined in the module. Also, you can use aliases to shorten the module name or function names.

## For example:
### Module alias:
```
import math as m
print(m.sqrt(16))
```

### Specific items alias:
```
from math import sqrt as square_root
print(square_root(16))
```

## Useful function
- The `round()` function rounds a number to the nearest integer.
- The `ceil()` function returns the smallest integer greater than or equal to a given number.
- The `floor()` function returns the largest integer less than or equal to a given number.
- The `abs()` function returns the absolute value of a number, therefore it will always return the positive form of a given number.
- The `pow()` function returns the value of a number raised to the power of another number `(math.pow(5, 5) = (5**5))`. Note: You can also achieve this by using "**". The difference is that the `pow()` function will return a float, and the "**" will return a integer
- The `sqrt()` function returns the square root of a number.
- The `max()` function returns the largest of the input values.
- The `min()` function returns the smallest of the input values.

There are more functions which I didn't mention, so I encourage you to go to the `math` module [documentation](https://docs.python.org/3/library/math.html) to learn more.

Made by danilo.zs
