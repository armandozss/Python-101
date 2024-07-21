The `random` module in Python is used to generate random numbers and make random choices, which is useful for simulations, games, and other scenarios where randomness is needed.

## Basic syntax
```
import random
x = random.randint(1, 10)
print(x)
```
`random.randint(a, b)` returns a random integer between `a` and `b` (inclusive).

## Generating a random float
```
y = random.random()
print(y)
```
`random.random()` returns a random floating-point number between `0.0` and `1.0`.

## Selecting a random choice
```
game = ['rock', 'paper', 'scissors']
z = random.choice(game)
print(z)
```
`random.choice(sequence)` returns a random element from a non-empty sequence (like a list).

## Shuffling a list
```
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)
```
`random.shuffle(list)` shuffles the elements of the list in place, meaning the order of the list is randomized.

The `random` module provides a variety of functions to introduce randomness into your programs, making it a versatile tool for many applications.

Made by danilo.zs
