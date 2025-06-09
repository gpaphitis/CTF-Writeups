# PicoCTF - Bbbbloat

## Challenge Overview
**Title:** bbbbloat.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** bbbbloat

## Description
Can you get the flag? Reverse engineer this binary.

## Analysis
Using `file` we see that the binary is stripped, meaning there will be no symbols to ease our analysis using `gdb`.
```
bbbbloat: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1989eb2c7cb4aad23df277d8aed3c97482740d7a, for GNU/Linux 3.2.0, stripped
```

I run the binary and see it asking for a number
```
What's my favorite number? 
``` 
So I will add a breakpoint and `printf()` and find the return address.
```
(gdb) b printf
Breakpoint 1 at 0x1120
(gdb) r
Starting program: /home/george/Downloads/bbbbloat 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, __printf (format=0x555555556004 "What's my favorite number? ") at ./stdio-common/printf.c:28
warning: 28	./stdio-common/printf.c: No such file or directory
(gdb) x/8gx $rsp
0x7fffffffdb18:	0x00005555555553dc	0x00007fffffffdc98
0x7fffffffdb28:	0x0000000100000000	0x000d2c4900000000
0x7fffffffdb38:	0x0000000000000000	0x4c75257240343a41
0x7fffffffdb48:	0x3062396630664634	0x63633066635f3d33
```
The first stack value, `0x00005555555553dc`, is the return address.
So we disassemble starting there to see the assembly code.
```
(gdb) x/80i 0x00005555555553dc
...
0x55555555544d:	lea    0xbcc(%rip),%rdi        # 0x555555556020
0x555555555454:	mov    $0x0,%eax
0x555555555459:	call   0x555555555140 <__isoc99_scanf@plt>
0x55555555545e:	movl   $0x3078,-0x3c(%rbp)
0x555555555465:	addl   $0x13c29e,-0x3c(%rbp)
0x55555555546c:	subl   $0x30a8,-0x3c(%rbp)
0x555555555473:	shll   $1,-0x3c(%rbp)
0x555555555476:	mov    -0x3c(%rbp),%eax
0x555555555479:	movslq %eax,%rdx
0x55555555547c:	imul   $0x55555556,%rdx,%rdx
0x555555555483:	shr    $0x20,%rdx
0x555555555487:	sar    $0x1f,%eax
0x55555555548a:	mov    %edx,%esi
0x55555555548c:	sub    %eax,%esi
0x55555555548e:	mov    %esi,%eax
0x555555555490:	mov    %eax,-0x3c(%rbp)
0x555555555493:	movl   $0x3078,-0x3c(%rbp)
0x55555555549a:	addl   $0x13c29e,-0x3c(%rbp)
0x5555555554a1:	subl   $0x30a8,-0x3c(%rbp)
0x5555555554a8:	shll   $1,-0x3c(%rbp)
0x5555555554ab:	mov    -0x3c(%rbp),%eax
0x5555555554ae:	movslq %eax,%rdx
0x5555555554b1:	imul   $0x55555556,%rdx,%rdx
0x5555555554b8:	shr    $0x20,%rdx
0x5555555554bc:	sar    $0x1f,%eax
0x5555555554bf:	mov    %edx,%edi
0x5555555554c1:	sub    %eax,%edi
0x5555555554c3:	mov    %edi,%eax
0x5555555554c5:	mov    %eax,-0x3c(%rbp)
0x5555555554c8:	mov    -0x40(%rbp),%eax
0x5555555554cb:	cmp    $0x86187,%eax
0x5555555554d0:	jne    0x555555555583
...
```
We see a call to `scanf()` whcih probably gets our input and stores it at `%rip + 0xbcc` or `0x555555556020` as `gdb` calculates for us.  
Then we see a bunch of instructions and a **conditional** jump towards the end.  
Instead of trying to **understand** all the **bloat**, I **first** try to input the **value** I see in the `cmp` instruction.  
That value is `0x86187` or `549255` in decimal.

I **run** the program, **enter** that value and check.  
And we are **successful**.
## Solution
- Run the program
- Enter the `549255` when asked

### Execution Example
```
What's my favorite number? 549255         
picoCTF{____REDACTED____}
```