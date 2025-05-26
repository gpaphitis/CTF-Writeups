# PicoCTF - Picker II

## Challenge Overview
**Title:** Picker II  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** picker-II.py

## Analysis
The code is very similar to the previous challenge - Picker I where I have a write-up for as well.

There is a slight difference to the previous code

### while loop
```python
while(True):
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      eval(user_input + '()')
    else:
      print('Illegal input')
  except Exception as e:
    print(e)
    break
```

The `while` loop now calls a `filter()` function which checks if the input is `win`

### `filter()`
```python
def filter(user_input):
  if 'win' in user_input:
    return False
  return True
```

This prevents our previous attack which was to enter `win`.

Now we have to be more **creative**.

Instead of invoking `win()` we will enter its code as our input in one line.

### What we want to input
```python
flag = open('flag.txt', 'r').read();flag = flag.strip();print(flag)
```

**However**, the `eval()` function does not simply execute Python code.

It evaluates a string as a **single** expression.

We have to **compress** our logic into a Python **one liner**.

The first part is easy.
```python
flag = open('flag.txt', 'r').read();flag = flag.strip();
```
can be chained as 
```python
flag = open('flag.txt', 'r').read().strip();
```

The problem is `print()`.  
Python string do **not** have a print() attribute to invoke in our chain and we can't enter it as a second command.  
Our **solution** is to we can create a **lambda** function which prints our chain because lambdas are **single** expressions and can be executed using `eval()`

### Final input
```python
(lambda: print(open('flag.txt', 'r').read().strip()))
```

## Solution
Entering 
```python
(lambda: print(open('flag.txt', 'r').read().strip()))
```
as our input will print the flag.