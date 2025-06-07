# PicoCTF - Picker III

## Challenge Overview
**Title:** Picker III  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** picker-III.py

## Description
Can you figure out how this program works to get the flag?
Additional details will be available after launching your challenge instance.

## Source Code
```python
import re



USER_ALIVE = True
FUNC_TABLE_SIZE = 4
FUNC_TABLE_ENTRY_SIZE = 32
CORRUPT_MESSAGE = 'Table corrupted. Try entering \'reset\' to fix it'

func_table = ''

def reset_table():
  global func_table

  # This table is formatted for easier viewing, but it is really one line
  func_table = \
'''\
print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
'''

def check_table():
  global func_table

  if( len(func_table) != FUNC_TABLE_ENTRY_SIZE * FUNC_TABLE_SIZE):
    return False

  return True


def get_func(n):
  global func_table

  # Check table for viability
  if( not check_table() ):
    print(CORRUPT_MESSAGE)
    return

  # Get function name from table
  func_name = ''
  func_name_offset = n * FUNC_TABLE_ENTRY_SIZE
  for i in range(func_name_offset, func_name_offset+FUNC_TABLE_ENTRY_SIZE):
    if( func_table[i] == ' '):
      func_name = func_table[func_name_offset:i]
      break

  if( func_name == '' ):
    func_name = func_table[func_name_offset:func_name_offset+FUNC_TABLE_ENTRY_SIZE]
  
  return func_name


def print_table():
  # Check table for viability
  if( not check_table() ):
    print(CORRUPT_MESSAGE)
    return

  for i in range(0, FUNC_TABLE_SIZE):
    j = i + 1
    print(str(j)+': ' + get_func(i))


def filter_var_name(var_name):
  r = re.search('^[a-zA-Z_][a-zA-Z_0-9]*$', var_name)
  if r:
    return True
  else:
    return False


def read_variable():
  var_name = input('Please enter variable name to read: ')
  if( filter_var_name(var_name) ):
    eval('print('+var_name+')')
  else:
    print('Illegal variable name')


def filter_value(value):
  if ';' in value or '(' in value or ')' in value:
    return False
  else:
    return True


def write_variable():
  var_name = input('Please enter variable name to write: ')
  if( filter_var_name(var_name) ):
    value = input('Please enter new value of variable: ')
    if( filter_value(value) ):
      exec('global '+var_name+'; '+var_name+' = '+value)
    else:
      print('Illegal value')
  else:
    print('Illegal variable name')


def call_func(n):
  """
  Calls the nth function in the function table.
  Arguments:
    n: The function to call. The first function is 0.
  """

  # Check table for viability
  if( not check_table() ):
    print(CORRUPT_MESSAGE)
    return

  # Check n
  if( n < 0 ):
    print('n cannot be less than 0. Aborting...')
    return
  elif( n >= FUNC_TABLE_SIZE ):
    print('n cannot be greater than or equal to the function table size of '+FUNC_TABLE_SIZE)
    return

  # Get function name from table
  func_name = get_func(n)

  # Run the function
  eval(func_name+'()')


def dummy_func1():
  print('in dummy_func1')

def dummy_func2():
  print('in dummy_func2')

def dummy_func3():
  print('in dummy_func3')

def dummy_func4():
  print('in dummy_func4')

def getRandomNumber():
  print(4)  # Chosen by fair die roll.
            # Guaranteed to be random.
            # (See XKCD)

def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)

def help_text():
  print(
  '''
This program fixes vulnerabilities in its predecessor by limiting what
functions can be called to a table of predefined functions. This still puts
the user in charge, but prevents them from calling undesirable subroutines.

* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  '''
  )
  print_table()



reset_table()

while(USER_ALIVE):
  choice = input('==> ')
  if( choice == 'quit' or choice == 'exit' or choice == 'q' ):
    USER_ALIVE = False
  elif( choice == 'help' or choice == '?' ):
    help_text()
  elif( choice == 'reset' ):
    reset_table()
  elif( choice == '1' ):
    call_func(0)
  elif( choice == '2' ):
    call_func(1)
  elif( choice == '3' ):
    call_func(2)
  elif( choice == '4' ):
    call_func(3)
  else:
    print('Did not understand "'+choice+'" Have you tried "help"?')
```

## Analysis
This is the third and final challenge ind the Picker series (write-ups exist for the previous two).

The code now is quite different.

When running the file, we can enter `help` to be displayed with a list fo actions we can perform.

### Output
```
* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
```

We are now **restricted** to only execute the functions **defined** in the table

**One** action is of particular **interest** and that is `write_variable`

### `write_variable()`
```python
def write_variable():
  var_name = input('Please enter variable name to write: ')
  if( filter_var_name(var_name) ):
    value = input('Please enter new value of variable: ')
    if( filter_value(value) ):
      exec('global '+var_name+'; '+var_name+' = '+value)
    else:
      print('Illegal value')
  else:
    print('Illegal variable name')
```

This function defines a **new** global variable, if the name is allowed, variable and **assigns** it a value we want.

We can also enter the name of an **existing** global variable and **redefine** it, like `func_table`

### `func_table`
```python
  func_table = \
'''\
print_table                     \
read_variable                   \
write_variable                  \
getRandomNumber                 \
```

`func_table` is a long **one line** string and contains the **allowed** function names to be executed.  
Each **entry** is 32 characters long, which explains the long spaces between each function, and there are 4 entries as defined here.

```python
FUNC_TABLE_SIZE = 4
FUNC_TABLE_ENTRY_SIZE = 32
```

We can also print it to verify this.
Inputting '2' as our input will execute the `read_variable` operation.
Then we can specify `func_table` as the variable we want to see and we get

```
==> 2
Please enter variable name to read: func_table
print_table                     read_variable                   write_variable                  getRandomNumber
```

What we need to do is carefully **craft** our own `func_table` definition which contains `win` as one of the **allowed** operations.

To do so, we can **change** the last function, `getRandomNumber` to win and **replace** the extra characters with **spaces** to fill the 32 character entry size.

### Payload
```
"print_table                     read_variable                   write_variable                  win                             "
```

**Notice** the inclusion of `""` around the payload.  
If we carefully look at the **instruction** that defines the variable
```python
exec('global '+var_name+'; '+var_name+' = '+value)
```
It **executes** the following statement
```python
global var_name; var_name = value
``` 
The value is **not** wrapped in `""` since it might be a number.  
So we need to **explicitly** add them

The **final step** is to get the output, which is hex values, and **convert** it to an ASCII string (similarly to Picker I) to get our **flag**.

## Solution
**Overwrite** `func_table` using the `write_variable` operation with our own definition.
```
"print_table                     read_variable                   write_variable                  win                             "

```
**Execute** the fourth operation.  
**Convert** the hex values to an ASCII string.

### Example
```
==> 3
Please enter variable name to write: func_table
Please enter new value of variable: "print_table                     read_variable                   write_variable                  win                             "
==> 2
Please enter variable name to read: func_table
print_table                     read_variable                   write_variable                  win                             
==> 4
______flag hex______
```