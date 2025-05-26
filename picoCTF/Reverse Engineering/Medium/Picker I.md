# PicoCTF - Picker I

## Challenge Overview
**Title:** Picker I  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** picker-I.py

## Analysis
Looking at the end of the code, we see that the program starts executing an infinite loop.
### while loop
```python
while(True):
  try:
    print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
  except Exception as e:
    print(e)
    break
```

In the loop, it takes some user input, appends it with "()" and executes it.

It is essentially **turning** the user input into a **funtion** and calling it.

Running the program we see
```
Try entering "getRandomNumber" without the double quotes...
==>
```

We enter `win` as our input and get a series of **hex values**.

### `win()` function
```python
def win():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
```
We see that the **flag** is turned into its **hex ASCII** representation using 
```python
str_flag += str(hex(ord(c))) + ' '
```

Now, using a hex to string **converter**, like RapidTables online, we can see the **flag**.  
(**Note:** RapidTables "Hex to Text" does **not** want the `0x` in front of each value).

## Solution
Enter `win` as our input to the program when prompted and and turn the given hex values to an ASCII string.