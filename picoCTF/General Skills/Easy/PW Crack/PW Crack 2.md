# PicoCTF - PW Crack 2

## Challenge Overview
**Title:** PW Crack 2  
**Category:** General Skills  
**Difficulty:** Easy  
**Files Provided:** level1.flag.txt.enc, level1.py  

## Description
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag in the same directory too.

## Source Code
```python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################


flag_enc = open('level1.flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()
```

## Analysis
Running the **Python** program we are asked for a **password**
```
$ python level1.py
Please enter correct password for flag:
```

Looking at the code, we see the `level_1_pw_check()` function which **takes** the user password and **checks** it.
```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
```
The **user password** is compared with `8713` so this is out password.
## Solution
- Run the **Python** program
- Enter `8713` as the password

### Execution Example
```
Please enter correct password for flag: 8713
Welcome back... your flag, user:
picoCTF{____REDACTED____}
```