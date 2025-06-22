int_list = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734304867,
    942695730,
    942748212
]

chars = []

for int in int_list:
    b0 = (int >> 0) & 0xFF
    b1 = (int >> 8) & 0xFF
    b2 = (int >> 16) & 0xFF
    b3 = (int >> 24) & 0xFF

    chars.append(chr(b3))
    chars.append(chr(b2))
    chars.append(chr(b1))
    chars.append(chr(b0))

password = "".join(chars)
print(password)
