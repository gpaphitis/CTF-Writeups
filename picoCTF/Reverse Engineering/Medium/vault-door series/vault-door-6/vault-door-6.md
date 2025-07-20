# PicoCTF - vault-door-6

## Challenge Overview
**Title:** vault-door-6.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** VaultDoor6.java

## Description
This vault uses an XOR encryption scheme. The source code for this vault is here: VaultDoor6.java

## Source Code
```java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}

```

## Analysis
Similarly to the previous challenges, we see that the program takes a **password** as an **input**.  
The password is expected to havetheformat `picoCTF{...}`, since the input is split at `picoCTF{` and `}`.
```java
public static void main(String args[]) {
    VaultDoor6 vaultDoor = new VaultDoor6();
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter vault password: ");
    String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```

Then `checkPassword()` is called which:
- Converts password to **bytes**
- **XORs** each byte with `0x55` and **compares** to a **custom** byte array

```java
byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
```
**XOR** has the following **property**:  
A XOR B = C  
C XOR B = A

In **our** case:
- A = password
- B = 0x55
- C = myBytes

From the **source code**, we have **0x55 - B** and **myBytes - C**.  
So, we can **calculate** the **password**.

To **help** with the **calculation** and the **conversion** to string of the result I have written the following **Python** script
### Python Script
```python
bytes =[0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d]
xor_key=0x55
decoded_bytes=[]
for byte in bytes:
   decoded_bytes.append(byte^0x55)

ascii_string = ''.join(chr(byte) for byte in decoded_bytes)

print(ascii_string)
```
This **defines** the bytes found in `myBytes` in a list, **XORs** them with **0x55** and **converts** them to one **string**.  
The output is the **password**.
## Solution
- Take the `myBytes` bytes
- XOR them with 0x55
- Convert to an ASCII string  
**OR**
- Run above Python script
