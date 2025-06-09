# PicoCTF - patchme.py

## Challenge Overview
**Title:** patchme.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** patchme.flag.py, flag.txt.enc

## Description
Can you get the flag? Run this Python program in the same directory as this encrypted flag.

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


flag_enc = open('flag.txt.enc', 'rb').read()



def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()

```

## Analysis
The script calls the `level_1_pw_check()`.  
In there, the user is asked to **enter** a password which is then **compared** with a string
```python
user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
```
The string is **separated** in multiple lines using the `\` operator.  
Putting it together we get: `ak98-=90adfjhgj321sleuth9000`.

Now we **run** the program and **enter** the above password.
## Solution
- Run the program
- Enter the password `ak98-=90adfjhgj321sleuth9000` when asked

### Execution Example
```
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{____REDACTED____}
```