# Sam's Python Cheat Sheet

## Variables
```python
a = input()

b = 1
b = b + 1
b += 1
```

## Global Function
```python
print("")
print(f"Hello {name}")

# Number conversion
string = "1"
integer = int(string)
string = str(integer)

# Number rounding
float = 1.6
rounded = round(float, 0)
# rounded == 2.0

if 1 == 1:
    print('')
elif 2 == 2:
    print('')
else:
    print('')
```

## String Functions
```python
string = "Sam".lower()
string = string.upper()
first_character = string[0]
```

## Custom Functions
```python
def makeBananaYellow(banana):
    return "yellow " + banana
```

## For/While Loops
```python
for a in 'Sam':
  print(a)
```

```python
fruits = ['apple', 'pear', 'orange']
for fruit in fruits:
  print(fruit)
```

```python
for m in range(10):

while True:

while a == 1:

i = 1
while i < 6:
  print(i)
  i += 1
```

### Star Turtle
```python
from turtle import *
pencolor('green')
pensize(5)
length = int(input('Length? '))
for t in range(5):
  forward(length)
  right(144)
```

### Unicode
```python
number = ord('S')
character = chr(number)
```
