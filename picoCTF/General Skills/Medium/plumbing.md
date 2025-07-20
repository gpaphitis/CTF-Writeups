# PicoCTF - plumbing

## Challenge Overview
**Title:** plumbing  
**Category:** General Skills  
**Difficulty:** Medium  

## Description
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 14291.
## Analysis
We connect to the server using
```
nc jupiter.challenges.picoctf.org 14291
```

And we are faced with a **lot** of random **text**.  
We want to **filter** this output in order to easily **find** the **flag**.  

To do so, I will use `grep`.
```
nc jupiter.challenges.picoctf.org 14291 | grep "picoCTF{"
```

## Solution
### Execution Example
```
$ nc jupiter.challenges.picoctf.org 14291 | grep "picoCTF{"
picoCTF{____REDACTED____}
```