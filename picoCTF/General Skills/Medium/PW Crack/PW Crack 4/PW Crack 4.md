# PicoCTF - PW Crack 4

## Challenge Overview
**Title:** PW Crack 4  
**Category:** General Skills  
**Difficulty:** Medium  
**Files Provided:** level4.flag.txt.enc, level4.hash.bin, level4.py  

## Description
Can you crack the password to get the flag? Download the password checker here and you'll need the encrypted flag and the hash in the same directory too. There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.

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

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_4_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_4_pw_check()



# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8c86", "7692", "a519", "3e61", "7dd6", "8919", "aaea", "f34b", "d9a2", "39f7", "626b", "dc78", "2a98", "7a85", "cd15", "80fa", "8571", "2f8a", "2ca6", "7e6b", "9c52", "7423", "a42c", "7da0", "95ab", "7de8", "6537", "ba1e", "4fd4", "20a0", "8a28", "2801", "2c9a", "4eb1", "22a5", "c07b", "1f39", "72bd", "97e9", "affc", "4e41", "d039", "5d30", "d13f", "c264", "c8be", "2221", "37ea", "ca5f", "fa6b", "5ada", "607a", "e469", "5681", "e0a4", "60aa", "d8f8", "8f35", "9474", "be73", "ef80", "ea43", "9f9e", "77d7", "d766", "55a0", "dc2d", "a970", "df5d", "e747", "dc69", "cc89", "e59a", "4f68", "14ff", "7928", "36b9", "eac6", "5c87", "da48", "5c1d", "9f63", "8b30", "5534", "2434", "4a82", "d72c", "9b6b", "73c5", "1bcf", "c739", "6c31", "e138", "9e77", "ace1", "2ede", "32e0", "3694", "fc92", "a7e2"]
```

## Analysis
In the source code, we are given **1000 possible passwords** at the end
```python
# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["8c86", "7692", "a519", "3e61" ...]
```
We **can't manually** check them, like in the previous challenge, so we will **write** a **Bash script** to do this.
## Bash Script
```bash
#!/bin/bash

values=("8c86" "7692" "a519" "3e61" "7dd6" "8919" "aaea" "f34b" "d9a2" "39f7" "626b" "dc78" "2a98" "7a85" "cd15" "80fa" "8571" "2f8a" "2ca6" "7e6b" "9c52" "7423" "a42c" "7da0" "95ab" "7de8" "6537" "ba1e" "4fd4" "20a0" "8a28" "2801" "2c9a" "4eb1" "22a5" "c07b" "1f39" "72bd" "97e9" "affc" "4e41" "d039" "5d30" "d13f" "c264" "c8be" "2221" "37ea" "ca5f" "fa6b" "5ada" "607a" "e469" "5681" "e0a4" "60aa" "d8f8" "8f35" "9474" "be73" "ef80" "ea43" "9f9e" "77d7" "d766" "55a0" "dc2d" "a970" "df5d" "e747" "dc69" "cc89" "e59a" "4f68" "14ff" "7928" "36b9" "eac6" "5c87" "da48" "5c1d" "9f63" "8b30" "5534" "2434" "4a82" "d72c" "9b6b" "73c5" "1bcf" "c739" "6c31" "e138" "9e77" "ace1" "2ede" "32e0" "3694" "fc92" "a7e2")

for val in "${values[@]}"
do
  python3 level4.py <<< "$val" | grep "picoCTF"
done
```
The script **iterates** over each **value**, runs the **Python** program and **inputs** that value as the **password**.
We **run** this and **wait** for the **flag** to be printed out

## Solution
- Get the passwords from the bottom of the source code
- Test them in the Python program like the Bash script provided.

### Execution Example
```
$ ./script.sh               
picoCTF{____REDACTED____}