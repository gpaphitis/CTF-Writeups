# PicoCTF - Picker III

## Challenge Overview
**Title:** Picker III  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** picker-III.py

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