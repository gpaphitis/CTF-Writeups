# PicoCTF - WinAntiDbg0x100

## Challenge Overview
**Title:** WinAntiDbg0x100  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** WinAntiDbg0x100.zip

## Initial Analysis
Upon extracting the zip with `picoctf` password we see an executable name `WinAntiDbg0x100.exe`.

Using `Detect It Easy (DIE)` we see it is an **unpacked 32-bit** executable.

When running it from a command prompt we see this:
```
        _            _____ _______ ______
       (_)          / ____|__   __|  ____|
  _ __  _  ___ ___ | |       | |  | |__
 | '_ \| |/ __/ _ \| |       | |  |  __|
 | |_) | | (_| (_) | |____   | |  | |
 | .__/|_|\___\___/ \_____|  |_|  |_|
 | |
 |_|
  Welcome to the Anti-Debug challenge!
### To start the challenge, you'll need to first launch this program using a debugger!
```

So we need to run it with a **debugger**.

Firstly, I use `strings` tool to see some strings contained in the file to help me **locate** where the flag is being printed or even try to cheese it and get the flag. 

I cannot see the flag **but** I find some **interesting** things. 

### `strings`
```
### To start the challenge, you'll need to first launch this program using a debugger!
### Error reading the 'config.bin' file... Challenge aborted.
### Level 1: Why did the clever programmer become a gardener? Because they discovered their talent for growing a 'patch' of roses!
### Oops! The debugger was detected. Try to bypass this check to get the flag!
### Something went wrong...
### Good job! Here's your flag:
...
IsDebuggerPresent
...
```

We see some of the programs **output** strings and the last one (### Good job! Here's your flag) is **probably** where the flag will be printed.

## Detailed Analysis
The IsDebuggerPresent is a **Microsoft** function that checks if a **debugger** is present.  
This means that the program calls this at some point and thats what we will have to **bypass**.

Now, I will use `IDA Free` to look at the programs disassembly and run the debugger.

When the executable is loaded in IDA, we are put right at the start of **main**.  
Using the `Search > Text...` feature and entering "Good job", we are taken to the program location where the `### Good job! Here's your flag:` resides.

Now by viewing its **cross references**, we see it is used at an **address** in main.  
Thus, we see where the **flag** output happens in main.

```
push    offset aGoodJobHereSYo ; "### Good job! Here's your flag:\n"
call    ds:OutputDebugStringW
push    offset asc_4036EC ; "### ~~~ "
call    ds:OutputDebugStringW
```

Using the **graph** view, we follow the execution that lead to that block and we find the call to `IsDebuggerPresent`.

Now for **bypassing** it, we set a **breakpoint** after the call to `IsDebuggerPresent`.  
We launch the debugger and it will pause right after the return of `IsDebuggerPresent`.

If we let the execution continue, we will see this **error** message in the debugger's Output window.
```
Debugged application message: ### Oops! The debugger was detected. Try to bypass this check to get the flag!
```

To bypass it, once we reach the breakpoint, we have to change `eax` value from **1** to **0** in order for the jump to follow the branch we want

```
call    ds:IsDebuggerPresent
test    eax, eax
jz      short loc_ED161B
```

Once we **change** the value and let the execution **continue**, we will see in the Output window the success message following the flag

## Solution
Using `IDA Free`, locate the call to `IsDebuggerPresent` in main.  
Set a breakpoint after the call and start the debugger.  
Once execution pauses at the breakpoint, change `eax` value from **1** to **0**.
Continue execution and find flag in the Output window

## Tools Used
- `Detect it Easy (DIE)`
- `strings`
- `IDA Free`