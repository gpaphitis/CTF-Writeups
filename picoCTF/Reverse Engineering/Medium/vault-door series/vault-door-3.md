# PicoCTF - vault-door-3

## Challenge Overview
**Title:** vault-door-3.py  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** VaultDoor3.java

## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

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
Similarly to the previous challenge, `vault-door-1`, we see that the program takes a **password** as an **input**.  
The password is expected to havetheformat `picoCTF{...}`, since the input is split at `picoCTF{` and `}`.
```java
public static void main(String args[]) {
    VaultDoor3 vaultDoor = new VaultDoor3();
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter vault password: ");
    String userInput = scanner.next();
String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
```

Then `checkPassword()` is called which **checks** the password.  
The checker first **creates** a new array, `buffer`, to which it **stores** the password characters in a **jumbled** order.
```java
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
```
We will **decode** each **loop** to understand how the **password** characters are **distributed**.
#### First Loop
```java
for (i=0; i<8; i++) {
    buffer[i] = password.charAt(i);
}
```
This simply **stores** the first **8 characters** in the **same** order.  
`buffer[0-7] = password[0-7]`
#### Second Loop
```java
for (; i<16; i++) {
    buffer[i] = password.charAt(23-i);
}
```
The next 8 characters of `buffer` are the password **indices** starting from **23-8=15** down to **23-15=8**.  
`buffer[8-15] = password[15-8]`
#### Third Loop
```java
for (; i<32; i+=2) {
    buffer[i] = password.charAt(46-i);
}
```
Now, `i` is **incremented** by **2** each time.  
The next 8 characters of `buffer` are the **even** password **indices** starting from **46-16=30** down to **46-30=16**.  
`buffer[16, 18, 20, ..., 30] = password[30, 28, 26, ..., 16]`
#### Fourth Loop
```java
for (i=31; i>=17; i-=2) {
    buffer[i] = password.charAt(i);
}
```
Now, `i` is **starts** from **31** and is **decremented** by **2** each time.  
The final 8 characters of `buffer` are the **odd** password **indices** starting from **31** down to **17**.  
`buffer[17, 19, 21, ..., 31] = password[17, 19, 21, ..., 31]`.

Finally, the constructed `buffer` is **compared** to a **string**.
```java
String s = new String(buffer);
return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
```  
We have to **reverse** the above buffer **construction** process to **find** the password.  
Since we **know** the **mapping** of the `buffer` characters to the `password` we know how do it. 

## Solution
- Rearrange the characters of `jU5t_a_sna_3lpm12g94c_u_4_m7ra41` by reversing the `buffer` construction process
