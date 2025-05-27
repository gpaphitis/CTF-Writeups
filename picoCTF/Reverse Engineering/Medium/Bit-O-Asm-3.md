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
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```

## Analysis
We are looking again for the final value of `eax` from this dump as with the previous challenges.

On line `<+15>` we see the value **0x9fe1a** being stored to the address `rbp-0xc`.  
We also see the value **0x4** being stored to the address `rbp-0x8`.  

`rbp-0xc` is then loaded into `eax` on line `<+29>`.  
Right after, eax is multiplied with the value at `rbp-0x8` which is **0x4** using `imul`.  
Finally, `eax` is incremented by **0x1f5**

So the value we want the **decimal** representation of **(0x9fe1a * 0x4) + 0x1f5**.

## Solution
(0x9fe1a * 0x4) + 0x1f5 = 0x27FA5D  
**Result:** 2619997