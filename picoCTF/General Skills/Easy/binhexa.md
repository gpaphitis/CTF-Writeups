# PicoCTF - binhexa

## Challenge Overview
**Title:** binhexa  
**Category:** General Skills  
**Difficulty:** Easy  

## Description
How well can you perform basic binary operations?

Additional details will be available after launching your challenge instance.

## Analysis
This challenge is about performing **binary operations** on two **bit strings**.  
Specifically, we are asked to perform **7 operations**
- Addition (+)
- Multiplication (*)
- Left shift (<<)
- Right shift (>>)
- AND (&)
- OR (|)
- Convert to hex

## Example Solution
```
$ nc titan.picoctf.net 62679

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 01000101
Binary Number 2: 00111011


Question 1/6:
Operation 1: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10000000
Correct!

Question 2/6:
Operation 2: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 01111111
Correct!

Question 3/6:
Operation 3: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 111111100111
Correct!

Question 4/6:
Operation 4: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 00000001
Correct!

Question 5/6:
Operation 5: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 10001010
Correct!

Question 6/6:
Operation 6: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 00011101
Correct!

Enter the results of the last operation in hexadecimal: 1d

Correct answer!
The flag is: picoCTF{____REDACTED____}
```