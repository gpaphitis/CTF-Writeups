# PicoCTF - vault-door-7

## Challenge Overview
**Title:** vault-door-7.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** VaultDoor7.java

## Description
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java

## Source Code
```java
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class VaultDoor7 {
    public static void main(String args[]) {
        VaultDoor7 vaultDoor = new VaultDoor7();
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

    // Each character can be represented as a byte value using its
    // ASCII encoding. Each byte contains 8 bits, and an int contains
    // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
    // example: if the hex string is "01ab", then those can be
    // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
    // bytes are represented as binary, they are:
    //
    // 0x30: 00110000
    // 0x31: 00110001
    // 0x61: 01100001
    // 0x62: 01100010
    //
    // If we put those 4 binary numbers end to end, we end up with 32
    // bits that can be interpreted as an int.
    //
    // 00110000001100010110000101100010 -> 808542562
    //
    // Since 4 chars can be represented as 1 int, the 32 character password can
    // be represented as an array of 8 ints.
    //
    // - Minion #7816
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734304867
            && x[6] == 942695730
            && x[7] == 942748212;
    }
}

```

## Analysis
Similarly to the previous challenges, we see that the program takes a **password** as an **input**.  
The password is expected to havetheformat `picoCTF{...}`, since the input is split at `picoCTF{` and `}`.
```java
public static void main(String args[]) {
    VaultDoor7 vaultDoor = new VaultDoor7();
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter vault password: ");
    String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```

Then `checkPassword()` is called which:
- Converts password to **bytes**
- **Groups** every **4 bytes** into an **integer** creating **8** integers

```java
byte[] hexBytes = hex.getBytes();
for (int i=0; i<8; i++) {
    x[i] = hexBytes[i*4]   << 24
            | hexBytes[i*4+1] << 16
            | hexBytes[i*4+2] << 8
            | hexBytes[i*4+3];
}
```
Then the **password** is **checked** by **comparing** the **8** resulting **integers**.
```java
int[] x = passwordToIntArray(password);
return x[0] == 1096770097
    && x[1] == 1952395366
    && x[2] == 1600270708
    && x[3] == 1601398833
    && x[4] == 1716808014
    && x[5] == 1734304867
    && x[6] == 942695730
    && x[7] == 942748212;
```
We can **take** each of those **integers** and **break** them into **32 bytes** which will be the **password** characters.

To do so, I will **construct** a small **Python** script.
### Python Script
```python
int_list = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734304867,
    942695730,
    942748212
]

chars = []

for int in int_list:
    b0 = (int >> 0) & 0xFF
    b1 = (int >> 8) & 0xFF
    b2 = (int >> 16) & 0xFF
    b3 = (int >> 24) & 0xFF

    chars.append(chr(b3))
    chars.append(chr(b2))
    chars.append(chr(b1))
    chars.append(chr(b0))

password = "".join(chars)
print(password)
```
This **defines** the integers and **splits** each one to its **4 bytes** using **bit shifts**.   
Then it **appends** them to a **character list** in the **correct** order.  
Based on the source code, the **characters** that make up each **integer** are placed in **reverse** order
```java
x[i] = hexBytes[i*4]   << 24
    | hexBytes[i*4+1] << 16
    | hexBytes[i*4+2] << 8
    | hexBytes[i*4+3];
```
The **first character** becomes the **most significant byte** since it is **shifted** by **24** bits.

The output of the script is the **password**.
## Solution
- Take each integer found in `checkPassword()`
- Split it to its 4 bytes
- Reverse their order
- Convert them to characters  
**OR**
- Run above Python script
