# PicoCTF - PW Crack 5

## Challenge Overview
**Title:** PW Crack 5  
**Category:** General Skills  
**Difficulty:** Medium  
**Files Provided:** level5.flag.txt.enc, level5.hash.bin, level5.py, dictionary.txt  

## Description
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

## Source Code
```python
import hashlib

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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_5_pw_check()
```

## Analysis
The challenge now gives us `dictionary.txt` that contains **65536** possible passwords.
```python
# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8c86", "7692", "a519", "3e61" ...]
```
We **can't manually** check them, obviously, so we will **write** a **Bash script** to do this, similar to the last challenge.
## Bash Script
```bash
#!/bin/bash

input_file="dictionary.txt"

while IFS= read -r val || [[ -n "$val" ]]
do
  python3 level5.py <<< "$val"  | grep "picoCTF"
done < "$input_file"

```
The script **reads** the values from `dictionary.txt` one by one, runs the **Python** program and **inputs** that value as the **password**.
We **run** this and **wait** for the **flag** to be printed out.  
**Warning:** It will take a **while** until it prints the flag.

## Solution
- Use the Bash script.

### Execution Example
```
$ ./script.sh               
picoCTF{____REDACTED____}