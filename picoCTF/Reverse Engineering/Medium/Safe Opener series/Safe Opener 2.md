# PicoCTF - Safe Opener 2

## Challenge Overview
**Title:** Safe Opener 2
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** SafeOpener.class

## Description
What can you do with this file? I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Analysis
We are provided with a `Java class` file this time.  
Using an **online tool**, we can **disassemble** the file.  
```java
 public static boolean openSafe(String password) {
      String encodedkey = "picoCTF{___REDACTED___}";
      if (password.equals(encodedkey)) {
         System.out.println("Sesame open");
         return true;
      } else {
         System.out.println("Password is incorrect\n");
         return false;
      }
   }
```

Another **approach** is using Java's `javap` tool which **disassembles** .class files.  
### javap -c -verbose SafeOpener.class
```
...
public static boolean openSafe(java.lang.String);
    descriptor: (Ljava/lang/String;)Z
    flags: (0x0009) ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=2, args_size=1
         0: ldc           #24                 // String picoCTF{___REDACTED___}
         2: astore_1
         3: aload_0
         4: aload_1
...
```
We find the `safeOpener()` function where we can see the **flag** in a comment towards the start of the function.
## Solution
- Use an online .class file disassembler
- Find flag inside `openSafe()` in a string.
## Tools Used
- `javap` - Optional