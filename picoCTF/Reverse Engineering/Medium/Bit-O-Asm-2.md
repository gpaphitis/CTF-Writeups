# PicoCTF - Bit-O-Asm-2

## Challenge Overview
**Title:** Bit-O-Asm-2  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** disassembler-dump0_a.txt

## Disassembly Dump
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```

## Analysis
We are looking again for the final value of `eax` from this dump as with the previous challenge.

On line `<+15>` we see the value **0x9fe1a** being stored to the address `rbp-0x4`.  
That address is then loaded into `eax` on line `<+25>`.

So the value we want the **decimal** representation of **0x9fe1a**.

## Solution
Decimal representation of **0x9fe1a**.  
**Result:** 654874654874