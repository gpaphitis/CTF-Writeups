# PicoCTF - repetitions

## Challenge Overview
**Title:** repetitions  
**Category:** General Skills  
**Difficulty:** Easy  

## Description
Can you make sense of this file? Download the file here.

## Analysis
### enc_flag
```
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbFZrTTBKeldWaHdRMDB4V2tWU2JFNVdDbUpXV2tkVU1WcFhWVzFHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```
The `==` at the end strongly indicates that this is a **Base64** encoded string.

We decode it using the `base64` Linux tool.
```
$ base64 -d enc_flag       
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JzWVhwQ00xWkVSbE5WCmJWWkdUMVpXVW1GdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
```
And we see **another** seemingly **Base64** encoded string.  
The title, **repetitions**, indicates that this is a **repeatedly** Base64 **encoded** string.

We slowly **add** another **decoding layer** until we get the **flag**.
```
$ base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
```
## Solution
```
$ base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d            
picoCTF{____REDACTED____}
```