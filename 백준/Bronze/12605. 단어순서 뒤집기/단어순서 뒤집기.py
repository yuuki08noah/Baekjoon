import sys
import heapq

input = sys.stdin.readline
n = int(input())
for i in range(n):
    s = input().split()
    s.reverse()
    print(f"Case #{i+1}:", *s)