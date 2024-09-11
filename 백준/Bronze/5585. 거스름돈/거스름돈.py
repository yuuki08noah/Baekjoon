import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
balance = 1000-n
res = 0
res += balance // 500
balance %= 500
res += balance // 100
balance %= 100
res += balance // 50
balance %= 50
res += balance // 10
balance %= 10
res += balance // 5
balance %= 5
res += balance // 1
print(res)