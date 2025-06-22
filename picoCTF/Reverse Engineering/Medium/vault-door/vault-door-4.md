# PicoCTF - vault-door-4

## Challenge Overview
**Title:** vault-door-4.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** VaultDoor4.java

## Description
This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java

## Source Code
```java
cdimport java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
    }
}

```

## Analysis
Similarly to the previous challenges, we see that the program takes a **password** as an **input**.  
The password is expected to havetheformat `picoCTF{...}`, since the input is split at `picoCTF{` and `}`.
```java
public static void main(String args[]) {
    VaultDoor4 vaultDoor = new VaultDoor4();
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter vault password: ");
    String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```

Then `checkPassword()` is called which **checks** the password.  
The checker **converts** the password to **bytes** using the default character set which is **ASCII**.
```java
byte[] passBytes = password.getBytes();
```
Then it creates a **new byte array** with **custom** bytes.
```java
byte[] myBytes = {
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
    '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
};
```
This has bytes **represented** in **4** forms:
- Decimal
- Hexadecimal
- Octal
- ASCII Characters

It then **compares** the new **byte array** with the **password** bytes one by one to check if they are **equal**.

I will first **convert** them all the bytes in `myBytes` to **hex**
```
6a 55 35 74 5f 34 5f 62
55 6e 43 68 5f 30 66 5f
62 59 74 33 73 5f 63 31
39 34 66 37 34 35 38 65
```
Now we can use an **online** hex to ASCII **converter** and get the **password**.

## Solution
- Convert the bytes of `myBytes` inside `checkPassword()` to hex
- Convert the hex to ASCII text
