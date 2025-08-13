import time
import random
import ctypes

# C's rand() and srand() from the standard library
libc = ctypes.CDLL("msvcrt.dll")
libc.srand.argtypes = [ctypes.c_uint]
libc.rand.restype = ctypes.c_int

def generate_secret_code(key, secret_code, print_val=False):
    high=((key*0x4EC4EC4F)>>32)&0xFFFFFFFF
    low=(key*0x4EC4EC4F)&0xFFFFFFFF
    high>>=3
    low = key
    low>>=0x1F
    high-=low
    low=high
    low *= 0x1A
    key-=low
    low=key
    low+=0x41
    secret_code+=chr(low&0xFF)
    return secret_code

def c_rand(seed, count=1):
    libc.srand(seed)
    return [libc.rand() for _ in range(count)]

# Use the timeframe -5 seconds -> +5 seconds of current time
start_time = int(time.time()) - 5
end_time   = int(time.time()) + 5
calls_to_rand = 16

# Generate code for every timestamp
for t in range(start_time, end_time + 1):
    values=c_rand(t, calls_to_rand)
    secret_code=""
    i=0
    for key in values:
        secret_code=generate_secret_code(key, secret_code, i==0)
        i+=1
    print(f"{hex(t)} => {secret_code}")