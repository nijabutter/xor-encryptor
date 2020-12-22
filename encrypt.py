import random
import sys

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: encrypt.py <input_file> <output_file> [key]")
    exit(0)

input_file = sys.argv[1]
output_file = sys.argv[2]

def genkey(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"£$%^&*()-=_+[]{};'#:@~',/.<?>\\|"

    output = ""
    for _ in range(length):
        output += random.choice(chars)
    return output

def sxor(s1, s2):
    return bytes(a ^ ord(b) for a,b in zip(s1,s2))

a = open(input_file, "rb")
contents = a.read()
a.close()
if len(sys.argv) == 4:
    key = sys.argv[3]
else:
    key = genkey(len(contents))
    print("Key:", key)
encrypted = sxor(contents, key)
with open(output_file, "wb") as out:
    out.write(encrypted)
