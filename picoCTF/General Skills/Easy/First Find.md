# PicoCTF - First Find

## Challenge Overview
**Title:** First Find  
**Category:** General Skills  
**Difficulty:** Easy  
**Files Provided:** files.zip  

## Description
Unzip this archive and find the file named 'uber-secret.txt'  
Download zip file


## Analysis
To **quickly** search through the **folder hierarchy** for the file `uber-secrets.txt` we will use the `find` Linux tool.

```
$ find files -name "uber-secret.txt" | xargs cat
```
#### Explanation
- `find files -name "uber-secret.txt"` searches for a file with the name `uber-secret.txt` starting from the `files` folder
- `xargs cat` takes the result from `find`, which is the relative path, and executes `cat` with it as am argument 
## Solution
```
$ unzip files    
Archive:  files.zip
   ...  
$ find files -name "uber-secret.txt" | xargs cat
picoCTF{____REDACTED____}
```