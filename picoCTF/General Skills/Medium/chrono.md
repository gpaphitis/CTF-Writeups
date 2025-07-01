# PicoCTF - chrono

## Challenge Overview
**Title:** chrono  
**Category:** General Skills  
**Difficulty:** Medium  

## Description
How to automate tasks to run at intervals on linux servers?

## Analysis
From the challenge **description**, we understand that it has to do with `cron`.  
`cron` is a Linux job scheduler.  
You can define **scripts** or **jobs** and **specify** when you want to run them.  
For example, you can schedule a database backup every Sunday at midnight.

We connect to he server given when we launch the challenge.

To view the cronjobs scheduled in the server, we will see he contents of `/etc/crontab`
```
$ cat /etc/crontab
# picoCTF{____REDACTED____}
```
## Solution

- Connect to the server 
- Run `$ cat /etc/crontab`