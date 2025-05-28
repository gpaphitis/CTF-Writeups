# PicoCTF - unpackme.py

## Challenge Overview
**Title:** unpackme.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** unpackme.py

## Description
Can you get the flag? Reverse engineer this Python program.

## Source Code
```python
import base64
from cryptography.fernet import Fernet



payload = b'gAAAAABkzWGSzE6VQNTzvRXOXekQeW4CY6NiRkzeImo9LuYBHAYw_hagTJLJL0c-kmNsjY33IUbU2IWlqxA3Fpp9S7RxNkiwMDZgLmRlI9-lGAEW-_i72RSDvylNR3QkpJW2JxubjLUC5VwoVgH62wxDuYu1rRD5KadwTADdABqsx2MkY6fKNTMCYY09Se6yjtRBftfTJUL-LKz2bwgXNd6O-WpbfXEMvCv3gNQ7sW4pgUnb-gDVZvrLNrug_1YFaIe3yKr0Awo0HIN3XMdZYpSE1c9P4G0sMQ=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
print(plain)
exec(plain.decode())
```

## Analysis
From the code we can see the `payload` and a key string `key_str`.  
The key string is used to initialize the Fernet encryption engine.  
Then the payload is decrypted.

The interesting part is a `decode()` function is called on the **decrypted payload** which is then **executed** as Python code using `exec()`.

Executing the program, we are prompted with
```
What's the password?
```
which is not part of the original code, so it is **part** of the **decoded payload** which is executed.

`plain.decode()` generates valid **Python** code which is executed and checks for a password

We can print `plain.decode()` output and observe the **hidden code** like this.

```python
...
plain = f.decrypt(payload)
print(plain.decode())
...
```
Running the code, we now see
### Output
```
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('_______flag_______')
else:
  print('That password is incorrect.')
```

## Solution
We can grab the flag from the output of
```python
print(plain.decode())
```