# PicoCTF - vault-door-8

## Challenge Overview
**Title:** vault-door-8.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** VaultDoor8.java

## Description
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: VaultDoor8.java

## Source Code
```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*; import javax.crypto.Cipher; import javax.crypto.spec.SecretKeySpec;
import java.security.*; class VaultDoor8 {public static void main(String args[]) {
Scanner b = new Scanner(System.in); System.out.print("Enter vault password: ");
String c = b.next(); String f = c.substring(8,c.length()-1); VaultDoor8 a = new VaultDoor8(); if (a.checkPassword(f)) {System.out.println("Access granted."); }
else {System.out.println("Access denied!"); } } public char[] scramble(String password) {/* Scramble a password by transposing pairs of bits. */
char[] a = password.toCharArray(); for (int b=0; b<a.length; b++) {char c = a[b]; c = switchBits(c,1,2); c = switchBits(c,0,3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ c = switchBits(c,5,6); c = switchBits(c,4,7);
c = switchBits(c,0,1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ c = switchBits(c,3,4); c = switchBits(c,2,5); c = switchBits(c,6,7); a[b] = c; } return a;
} public char switchBits(char c, int p1, int p2) {/* Move the bit in position p1 to position p2, and move the bit
that was in position p2 to position p1. Precondition: p1 < p2 */ char mask1 = (char)(1 << p1);
char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ char bit1 = (char)(c & mask1); char bit2 = (char)(c & mask2); /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
System.out.println("bit2 " + Integer.toBinaryString(bit2)); */ char rest = (char)(c & ~(mask1 | mask2)); char shift = (char)(p2 - p1); char result = (char)((bit1<<shift) | (bit2>>shift) | rest); return result;
} public boolean checkPassword(String password) {char[] scrambled = scramble(password); char[] expected = {
0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD2, 0xD0, 0xB4, 0xE1, 0xC1, 0xE0, 0xD0, 0xD0, 0xE0 }; return Arrays.equals(scrambled, expected); } }
```

## Analysis
The source code is **not formatted** so we can do this by **using** either an **IDE**, like Intellij IDEA or an **online tool**.
### Formatted Source Code
```java
// These pesky special agents keep reverse engineering our source code and then
// breaking into our secret vaults. THIS will teach those sneaky sneaks a
// lesson.
//
// -Minion #0891
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;
class VaultDoor8 {
    public static void main(String args[]) {
        Scanner b = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String c = b.next();
        String f = c.substring(8, c.length() - 1);
        VaultDoor8 a = new VaultDoor8();
        if (a.checkPassword(f)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }
    public char[] scramble(String password) { /* Scramble a password by transposing pairs of bits. */
        char[] a = password.toCharArray();
        for (int b = 0; b < a.length; b++) {
            char c = a[b];
            c = switchBits(c, 1, 2);
            c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
            c = switchBits(c, 5, 6);
            c = switchBits(c, 4, 7);
            c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
            c = switchBits(c, 3, 4);
            c = switchBits(c, 2, 5);
            c = switchBits(c, 6, 7);
            a[b] = c;
        }
        return a;
    }
    public char switchBits(char c, int p1, int p2) {
        /* Move the bit in position p1 to position p2, and move the bit
        that was in position p2 to position p1. Precondition: p1 < p2 */
        char mask1 = (char)(1 << p1);
        char mask2 = (char)(1 << p2); /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */
        char bit1 = (char)(c & mask1);
        char bit2 = (char)(c & mask2);
        /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
        char rest = (char)(c & ~(mask1 | mask2));
        char shift = (char)(p2 - p1);
        char result = (char)((bit1 << shift) | (bit2 >> shift) | rest);
        return result;
    }
    public boolean checkPassword(String password) {
        char[] scrambled = scramble(password);
        char[] expected = {
            0xF4,
            0xC0,
            0x97,
            0xF0,
            0x77,
            0x97,
            0xC0,
            0xE4,
            0xF0,
            0x77,
            0xA4,
            0xD0,
            0xC5,
            0x77,
            0xF4,
            0x86,
            0xD0,
            0xA5,
            0x45,
            0x96,
            0x27,
            0xB5,
            0x77,
            0xD2,
            0xD0,
            0xB4,
            0xE1,
            0xC1,
            0xE0,
            0xD0,
            0xD0,
            0xE0
        };
        return Arrays.equals(scrambled, expected);
    }
}
```
Similarly to the previous challenges, we see that the program takes a **password** as an **input**.  
The **password** now **isn't** split on `picoCTF` but any **8 leading characters** but this doesn't matter.
```java
public static void main(String args[]) {
        Scanner b = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String c = b.next();
        String f = c.substring(8, c.length() - 1);
        VaultDoor8 a = new VaultDoor8();
```

Then `checkPassword()` is called which **scrambles** the buts of each character
```java
char[] a = password.toCharArray();
for (int b = 0; b < a.length; b++) {
    char c = a[b];
    c = switchBits(c, 1, 2);
    c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
    c = switchBits(c, 5, 6);
    c = switchBits(c, 4, 7);
    c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
    c = switchBits(c, 3, 4);
    c = switchBits(c, 2, 5);
    c = switchBits(c, 6, 7);
    a[b] = c;
}
```
Then the **scrambled characters** are compared to the `expected` list of characters.
```java
char[] expected = {
            0xF4,
            0xC0,
            0x97,
            0xF0,
            0x77,
            0x97,
            0xC0,
            0xE4,
            0xF0,
            0x77,
            0xA4,
            0xD0,
            0xC5,
            0x77,
            0xF4,
            0x86,
            0xD0,
            0xA5,
            0x45,
            0x96,
            0x27,
            0xB5,
            0x77,
            0xD2,
            0xD0,
            0xB4,
            0xE1,
            0xC1,
            0xE0,
            0xD0,
            0xD0,
            0xE0
        };
        return Arrays.equals(scrambled, expected);
```
We will **take** these `expected` characters and **reverse** the **scrambling process** to reveal the password.

To do so, I will use the following **Python**  script
### Python Script
```python
byte_list = [
    0xF4,
    0xC0,
    0x97,
    0xF0,
    0x77,
    0x97,
    0xC0,
    0xE4,
    0xF0,
    0x77,
    0xA4,
    0xD0,
    0xC5,
    0x77,
    0xF4,
    0x86,
    0xD0,
    0xA5,
    0x45,
    0x96,
    0x27,
    0xB5,
    0x77,
    0xD2,
    0xD0,
    0xB4,
    0xE1,
    0xC1,
    0xE0,
    0xD0,
    0xD0,
    0xE0,
]

def switch_bits(b, p1, p2):
   mask1=1<<p1
   mask2=1<<p2
   bit1=b&mask1
   bit2=b&mask2
   rest=b & ~(mask1 | mask2)
   shift = (p2 - p1)
   result =((bit1 << shift) | (bit2 >> shift) | rest)
   return result

def unscramble():
   pass_chars=[]
   for b in byte_list:
      b = switch_bits(b, 6, 7)
      b = switch_bits(b, 2, 5)
      b = switch_bits(b, 3, 4)
      b = switch_bits(b, 0, 1)
      b = switch_bits(b, 4, 7)
      b = switch_bits(b, 5, 6)
      b = switch_bits(b, 0, 3)
      b = switch_bits(b, 1, 2)
      pass_chars.append(chr(b))
   
   password="".join(pass_chars)
   print(len(password))
   print(password)
   
unscramble()
```
This **defines** the characters and **unscrambles** them.  
We follow the **same procedure** to **switch bits**.  
**But**, we have to be careful to **reverse** the **order** of bit **switches** from the original since **each bit** may be part of **many switches**.

The output of the script is the **password**.
## Solution
- Take each byte found in `checkPassword()` inside `expected`
- Reverse the bit switches for each byte
- Convert them to characters  
**OR**
- Run above Python script