# PicoCTF - 1_wanna_b3_a_r0ck5tar

## Challenge Overview
**Title:** 1_wanna_b3_a_r0ck5tar  
**Category:** General Skills  
**Difficulty:** Medium  
**Files Provided:** lyrics.txt  

## Description
I wrote you another song. Put the flag in the picoCTF{} flag format

## Lyrics
```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Shout A guitar!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"
Shout Music!                
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down
```
## Analysis
This challenge gives us some **lyrics** that seem **useless**.  
But, they actually **form** a **program** written in the **Rockstar** language.

### Rockstar Language
This is a Turing complete **language** and was made to **resemble** rock song lyrics.  
It uses **phrases** to perform operations.  
For example:
- My hopes are nothing - **Declares** the variable `hopes` and **assigns** it the value **0**
- Listen to the music - Takes an **input** and **assigns** it to the variable `music`
- Shout Tommy! - **Prints** the value of the variable `Tommy`

Knowing this, we can **start** to **interpret** the program.  
A few lines in we see he following:
```
A guitar is a six-string
...
Listen to the music             
If the music is a guitar
```
This **declares** the variable `A guitar` and **assigns** it a value like this:  
- `a six-string` is **converted** to the **number** of **letters per word**  
- In this case, it is **1-3-6** meaning **136**  

We could also simply add `Shout A guitar` after the **assignment** to find its value.

Then, it takes an **input**, **assigns** it to `music` and **compares** it to `A guitar`.  
So we **run** the program and enter **136** as our input.
```
Keep on rocking!
```
We made progress.  
**NOTE:** In the **Wayback Machine** provided, the **output** is shown **after** the **program exits**. So after every action, **cancel** the execution to view the output and **restart**

Moving on we see the **next comparison**:
```
Listen to the rhythm
If the rhythm without Music is nothing
```
`Music` is **defined** towards the **start**, close to `A guitar`. 
```
Music is a billboard-burning razzmatazz!
``` 
Note that variable names are **case sensitive**, so `Music` isn't the same as `music` we used before.  
Following the technique used for `A guitar`, the **value** assigned to `Music` is **1970** (10 maps to 0).  
So we enter **1970** for our next input.
```
Keep on rocking!
66
79
78
74
79
86
73
```
The **numbers** given are probably our **flag**.  
We just have to **convert** them to **characters**.  
To do so I have written a simple **Python** script

### Script
```python
vals = [66, 79, 78, 74, 79, 86, 73]

print("picoCTF{", end="")
for val in vals:
    print(chr(val), end="")
print("}")
```
```
$ python script.py
picoCTF{____REDACTED____}
```

## Solution

- Use the Wayback Machine provided to run the program
- Enter 136 and 1970 as the two inputs
- Convert the values given from the program to characters