To control the flow of loops in python we use these three keywords. They help you manage how and when to exit or skip parts of your loop.

## Break
The `break` statement is used to exit a loop prematurely, meaning it will stop the loop entirely, regardless of whether the loop condition is still true.
```
while True:
    name = input("What is your name?: ")
    if name != "":
        print("Hello!!, " + name)
        break
```
Now, let's break it down:
- `while True:`: Creates an infinite loop.
- Inside the loop, the program asks for the user's name. If the user provides a name, it prints a greeting and then executes `break`, which exits the loop.

## Continue
The `continue` statement is used to skip the current iteration of a loop and move to the next iteration. It does not terminate the loop but instead bypasses the rest of the code inside the loop for the current iteration.
```
Phone_number = "+1-456-8595-456"

for i in Phone_number:
    if i == "-":
        continue
    print(i, end="")
```
Now, let's break it down:
- The loop iterates over each character in the `Phone_number` string.
- When it encounters a hyphen `(-)`, `continue` is executed, which skips printing that character.
- All other characters are printed, resulting in the phone number being printed without hyphens.

## Pass
The `pass` statement is a placeholder that does nothing. It is used when a statement is syntactically required but you do not want to execute any code.
```
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i, end=" ")
```
Now, let's break it down:
- The loop iterates through numbers from 1 to 5.
- When the loop variable `i` equals 3, `pass` is executed. It effectively does nothing and allows the loop to continue to the next iteration.
- For all other values of `i`, the number is printed.

## Summary
- `break`: Exits the loop completely.
- `continue`: Skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.
- `pass`: Acts as a placeholder and does nothing. It is used when a statement is required syntactically but no action is needed.

Made by danilo.zs
