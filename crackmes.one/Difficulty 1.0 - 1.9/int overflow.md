# crackmes.one - int overflow

## Challenge Overview
**Title:** int overflow  
**Author:** izijerry  
**Difficulty:** 1.8  
**Quality:** 4.2  
**Language:** C/C++  
**Platform:** Unix/linux  
**Arch:** x86-64  
**Files Provided:** pass  

## Description
integer overflow!!!

## Analysis
We unzip the provided file using `crackmes.one` as the password and we find a **pass** file.  
This is an ELF executable
```
$ file pass                        
pass: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3c9a8ede197746d8138929ba3a31302a49829c52, for GNU/Linux 3.2.0, not stripped
```

When we run it, it asks for a password.
```
$ ./pass                             
input your password here: 
```

First I try `strings` to see if the password is somewhere in there
```
$ strings ./pass                      
:10*I
R/lib64/ld-linux-x86-64.so.2
atoi
__libc_start_main
__cxa_finalize
printf
__isoc99_scanf
```

But it didn't help.  
So now I will use `gdb` to find the point the check happens.
```
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000001198 <+0>:	push   %rbp
   0x0000000000001199 <+1>:	mov    %rsp,%rbp
   0x000000000000119c <+4>:	sub    $0x10,%rsp
   0x00000000000011a0 <+8>:	mov    $0x0,%eax
   0x00000000000011a5 <+13>:	call   0x1159 <GetPass>
   0x00000000000011aa <+18>:	mov    %rax,-0x8(%rbp)
   0x00000000000011ae <+22>:	mov    -0x8(%rbp),%rax
   0x00000000000011b2 <+26>:	mov    %rax,%rdi
   0x00000000000011b5 <+29>:	call   0x1050 <atoi@plt>
   0x00000000000011ba <+34>:	mov    %eax,-0xc(%rbp)
   0x00000000000011bd <+37>:	cmpl   $<PASSWORD>,-0xc(%rbp)
   0x00000000000011c4 <+44>:	jne    0x11dc <main+68>
```

We see that in `main()` there is a `GetPass()` function which I guess reads our input password.  
Then we see a call to `atoi()` which converts a string to an integer.  
Finally we see the result of `atoi()` be used in a comparison followed by a conditional jump.  
The value it is compared to is `<PASSWORD>` which is a hexadecimal.  
So we have to convert it to decimal and that is our password.

### Correct Execution Example
```
$ ./pass
input your password here: <PASSWORD>
Password Correct!!!
```

## Tools Used
- `gdb`