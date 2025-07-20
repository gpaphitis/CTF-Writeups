# PicoCTF - Shop

## Challenge Overview
**Title:** Shop  
**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Files Provided:** source

## Description
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 3952.

## Analysis
When we connect to the server, we are presented with a **menu**
```
Welcome to the market!
=====================
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option:
```

I assume that **option 2** is our target.  
However, we don't have enough coins for it.

We can try to buy something else
```
...
Choose an option: 
0
How many do you want to buy?
```

We are asked for a **quantity**.  
Let's try to insert a **negative** amount
```
How many do you want to buy?
-6
You have 100 coins
```

Great. now we have enough coins to **buy** one Fruitful Flag and get our **flag**
```
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [____REDACTED____]
```

Instead, of the flag, we are given a **list of numbers**.  
This is probably our flag but **ASCII** encoded.  
So we have to **decode** them.  
To do so, I have written a small **Python** script
```python
numbers=[____REDACTED____]

for num in numbers:
   print(chr(num), end="")
```
## Solution
- Buy a negative amount of either option 0 or 1
- Buy Fruitful Flag
- Convert numbers to ASCII characters
### Execution Example
```
Welcome to the market!
=====================
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-6
You have 100 coins
	Item		Price	Count
(0) Quiet Quiches	10	18
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 57 99 49 49 56 98 98 102 125]
```