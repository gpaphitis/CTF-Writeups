# PicoCTF - endianness

## Challenge Overview
**Title:** endianness  
**Category:** General Skills  
**Difficulty:** Easy  
**Files Provided:** flag.c

## Description
Know of little and big endian? Source

Additional details will be available after launching your challenge instance.

## Background Knowledge

The challenge aims to **teach** about **endianness**. 
### Endianness
Endianness refers to **how** bytes are **stored** in memory.  
Assume the hex value `0xdeadbeef`.  
This value is **4 bytes** which would take **4 memory addresses** to store it.  
Assume the value is **stored** starting at address **0x0**.

There are **two** ways to store it, **Little**
#### Big Endian
| Address  |  0x0  |  0x1  |  0x2  |  0x3  |
|----------|-------|-------|-------|-------|
| Value    |  0xde |  0xad |  0xbe |  0xef |

#### Little Endian
| Address  |  0x0  |  0x1  |  0x2  |  0x3  |
|----------|-------|-------|-------|-------|
| Value    |  0xef |  0xbe |  0xad |  0xde |

The **least significant** (or rightmost) byte is stored at the
- Lowest address - Little Endian
- Highest address - Big Endian 

## Analysis
We **connect** to the **server** given when we launch the instance.
```
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: qhyne
Enter the Little Endian representation:
```
We are given a string `qhyne` and are asked to enter the **Little Endian** representation of it.

The string `qhyne` has the following hex representation: `0x71 0x68 0x79 0x6E 0x65`.  
The **Little Endian** representation is the hex values in **reverse**.  
**Note:** The input is expected to not have the `0x` prefix not spaces in between.

**Little Endian Representation:** `656e796871`

We **enter** the above and we are **correct**.

```
...
Correct Little Endian representation!
Enter the Big Endian representation:
```
Now we are asked for the **Big Endian** representation.  
This is the hex values in the **initial** order.

**Big Endian Representation:** `7168796e65`

We **enter** this and we get the **flag**.

## Solution
- Get the given **word** and **turn** it to **hex** 
- Enter the hex values in **reverse** for the **Little Endian** representation
- Enter the hex values in the **initial** for the **Big Endian** representation

### Execution Example
```
$ nc titan.picoctf.net 50725
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: qhyne
Enter the Little Endian representation: 656e796871
Correct Little Endian representation!
Enter the Big Endian representation: 7168796e65
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{____REDACTED____}
```