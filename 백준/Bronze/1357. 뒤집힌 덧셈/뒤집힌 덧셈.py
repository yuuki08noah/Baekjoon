import sys
from collections import deque

input = sys.stdin.readline

a, b = input().strip().split()
print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))