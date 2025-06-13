# PicoCTF - Safe Opener

## Challenge Overview
**Title:** Safe Opener
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** SafeOpener.java

## Description
Can you open this safe? I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: picoCTF{password}

## Source Code
```java
import java.io.*;
import java.util.*;  
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}
```

## Analysis
We are provided with a `Java` file.  
In `main()` we see a **Base64** encoder being initialized.  
```java
Base64.Encoder encoder = Base64.getEncoder();
```

We later see it takes a **password** as input, **encodes** it with the encoder and **attempts** to open the **safe**.  
```java
while (i < 3) {
   System.out.print("Enter password for the safe: ");
   key = keyboard.readLine();

   encodedkey = encoder.encodeToString(key.getBytes());
   System.out.println(encodedkey);
      
   isOpen = openSafe(encodedkey);
   if (!isOpen) {
         System.out.println("You have  " + (2 - i) + " attempt(s) left");
         i++;
         continue;
   }
   break;
        }
```

We now look at `openSafe()` and see the `encodedkey` string.  
Since it is encoded with **Base64** which doesn't use a secret key, we can simply **decode** using an online tool.
## Solution
- Find the `encodedKey` string insinde `safeOpener()`
- Copy the **string** and **decode** it using an online Base64 decoder.