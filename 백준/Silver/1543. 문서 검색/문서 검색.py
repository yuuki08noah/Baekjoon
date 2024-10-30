import sys
import math

input = sys.stdin.readline
s = input()[:-1]
pattern = input()[:-1]

while pattern in s:
    s = s.replace(pattern, "*")
print(s.count("*"))