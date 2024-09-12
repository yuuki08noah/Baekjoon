import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
str = input()
split_str = []
temp = str[0]
for i in range(1, n):
    if str[i] == str[i-1]:
        temp += str[i]
    else:
        split_str.append(temp)
        temp = str[i]
split_str.append(temp)

acnt1 = 0
for i in range(len(split_str)-2, -1, -1):
    if 'R' in split_str[i]:
        acnt1 += len(split_str[i])
acnt2 = 0
for i in range(len(split_str)-2, -1, -1):
    if 'B' in split_str[i]:
        acnt2 += len(split_str[i])

bcnt1 = 0
for i in range(1, len(split_str)):
    if 'R' in split_str[i]:
        bcnt1 += len(split_str[i])
bcnt2 = 0
for i in range(1, len(split_str)):
    if 'B' in split_str[i]:
        bcnt2 += len(split_str[i])

print(min(bcnt1, bcnt2, acnt1, acnt2))