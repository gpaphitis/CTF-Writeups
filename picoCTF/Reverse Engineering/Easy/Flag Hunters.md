# PicoCTF - Flag Hunters

## Challenge Overview
**Title:** Flag Hunters  
**Category:** Reverse Engineering  
**Difficulty:** Easy  
**Files Provided:** lyric-reader.py

## Initial Analysis

The flag is contained in the `secret_intro` string.

```python
secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether’s ours to conquer, '''\
+ flag + '\n'
```

Which is then embedded at the start of `song_flag_hunters` string

```python
song_flag_hunters = secret_intro +\
'''

[REFRAIN]
We’re flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
...
```

Further down in the `reader` function we see a while loop which processes the `song_flag_hunters`.  
This contains a part with user input from which we will perform our exploit.



## Detailed Analysis

### While loop
```python
  while not finished and line_count < MAX_LINES:
    line_count += 1
    for line in song_lines[lip].split(';'):
      if line == '' and song_lines[lip] != '':
        continue
      if line == 'REFRAIN':
        song_lines[refrain_return] = 'RETURN ' + str(lip + 1)
        lip = refrain
      elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
      elif re.match(r"RETURN [0-9]+", line):
        lip = int(line.split()[1])
      elif line == 'END':
        finished = True
      else:
        print(line, flush=True)
        time.sleep(0.5)
        lip += 1
```
In the loop we can see that each line is split on `;`
and checked if each part is a control sequence, like `REFRAIN`.

The `CROWD` section is the only place with user input.  
That's how we will manipulate the program.
```python
elif re.match(r"CROWD.*", line):
        crowd = input('Crowd: ')
        song_lines[lip] = 'Crowd: ' + crowd
        lip += 1
```

Above the `CROWD` section, we see the `REFRAIN` section.  
There, `REFRAIN` is switched with a `RETURN <number>` which contains the line number the next `REFRAIN` will return to.

If we can insert our own `RETURN` statement with line number `0`, it will start printing from the `secret_intro` lyrics
and print the flag.



## Solution

The user input is embedded into the song's lyrics.

This means that `RETURN 0` as our input, will be processed as part of the lyrics and start from the `secret_intro` and print the flag.

However simply entering `RETURN 0` won't work since the whole line processed is `Crowd: RETURN 0`.


In order to separate it from the previous text of the line, we have to enter a `;` at the start
since the loop splits each line on `;` and processes each token individually.

**Final input:** `;RETURN 0`