# PicoCTF - mus1c

## Challenge Overview
**Title:** mus1c  
**Category:** General Skills  
**Difficulty:** Medium  
**Files Provided:** lyrics.txt  

## Description
I wrote you a song. Put it in the picoCTF{} flag format.

## Lyrics
```
Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico
```
## Analysis
The above lyrics may **seem useless** but they are not.  

They are actually a **runnable program** written in the [Rockstar language](https://codewithrockstar.com/)  
This language is meant to **represent** 80s rock song **lyrics**.

To **run** this program, we can use an **online interpreter**.  
We run it and the following
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```
This is our flag **encoded** in **ASCII** so we have to **convert** them back into characters.  
We can easily do this with a small **Python** script
### Python script
```python
nums = [114,114,114,111,99,107,110,114,110,48,49,49,51,114]

for num in nums:
    print(chr(num),end="")
```
We run this and get our flag.

## Solution
- Execute the lyrics iln an online Rockstar interpreter
- Convert the resulting decimal to ASCII characters