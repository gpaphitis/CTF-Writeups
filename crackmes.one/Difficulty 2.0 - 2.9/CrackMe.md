# crackmes.one - CrackMe

## Challenge Overview
**Title:** CrackMe  
**Author:** Shai  
**Difficulty:** 2.1  
**Quality:** 3.4
**Language:** C/C++  
**Platform:** Windows  
**Arch:** x86-64  
**Files Provided:** GoCrackMe.exe  

## Description
This is a simple crack-me, patch it and be happy because you patched a pointless program!!! :D

## Analysis
We run the executable and see that we need to find the password
```
>GoCrackMe.exe
Enter the password:
```

I will use `strings` to find static strings in the executable to see if the password is there
```
...
<PASSWORD>
...
Enter the password:
Congratulations! You have successfully cracked the password!
You have no more attempts left.
attempts left.
...
``` 

In there we find the success message we are after and also find a string that looks like a password.  

We try it and it is correct.

### Correct Execution Example
```
>GoCrackMe.exe
Enter the password: <PASSWORD>
Congratulations! You have successfully cracked the password!
```

## Tools Used
- `strings`