#!/bin/bash

input_file="dictionary.txt"

while IFS= read -r val || [[ -n "$val" ]]
do
  python3 level5.py <<< "$val"  | grep "picoCTF"
done < "$input_file"
