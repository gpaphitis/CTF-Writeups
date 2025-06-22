byte_list = [
    0xF4,
    0xC0,
    0x97,
    0xF0,
    0x77,
    0x97,
    0xC0,
    0xE4,
    0xF0,
    0x77,
    0xA4,
    0xD0,
    0xC5,
    0x77,
    0xF4,
    0x86,
    0xD0,
    0xA5,
    0x45,
    0x96,
    0x27,
    0xB5,
    0x77,
    0xD2,
    0xD0,
    0xB4,
    0xE1,
    0xC1,
    0xE0,
    0xD0,
    0xD0,
    0xE0,
]

def switch_bits(b, p1, p2):
   mask1=1<<p1
   mask2=1<<p2
   bit1=b&mask1
   bit2=b&mask2
   rest=b & ~(mask1 | mask2)
   shift = (p2 - p1)
   result =((bit1 << shift) | (bit2 >> shift) | rest)
   return result

def unscramble():
   pass_chars=[]
   for b in byte_list:
      b = switch_bits(b, 6, 7)
      b = switch_bits(b, 2, 5)
      b = switch_bits(b, 3, 4)
      b = switch_bits(b, 0, 1)
      b = switch_bits(b, 4, 7)
      b = switch_bits(b, 5, 6)
      b = switch_bits(b, 0, 3)
      b = switch_bits(b, 1, 2)
      pass_chars.append(chr(b))
   
   password="".join(pass_chars)
   print(len(password))
   print(password)
   
unscramble()