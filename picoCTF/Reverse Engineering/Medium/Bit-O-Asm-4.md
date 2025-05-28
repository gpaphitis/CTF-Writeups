# PicoCTF - Bit-O-Asm-4

## Challenge Overview
**Title:** Bit-O-Asm-4  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** disassembler-dump0_d.txt

## Description
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}. Download the assembly dump here.

## Disassembly Dump
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

## Analysis
We are looking again for the final value of `eax` from this dump as with the previous challenges.

On line `<+15>` we see the value **0x9fe1a** being stored to the address `rbp-0x4`.  
Then we see the value at `rbp-0x4` being compared to **0x2710**

**0x9fe1a** is greater than **0x2710** so the branch is not taken.

Now **0x65** is **subtracted** from the value at `rbp-0x4` and then we **jump** to line `<+41>` which loads the final value to `eax`

## Solution
0x9fe1a -0x65 = 0x9FDB5  
**Result:** 654773