# PicoCTF - Bit-O-Asm-1

## Challenge Overview
**Title:** Bit-O-Asm-1  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** disassembler-dump0_a.txt

## Disassembly Dump
```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

## Analysis
We are looking for the final value of `eax` from this dump.

On line `<+15>` we see the value **0x30** being moved to `eax`.

So the value we want the **decimal** representation of **0x30**.

## Solution
Decimal representation of **0x30**.  
**Result:** 48