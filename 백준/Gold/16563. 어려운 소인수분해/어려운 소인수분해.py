import math
import sys
import heapq

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))

sieve = [0]*(max(num)+1)
arr = []
for i in range(2, int(math.ceil(math.sqrt(max(num))+1))):
    if sieve[i] == 0:
        for j in range(i*2, max(num)+1, i):
            sieve[j] = i

for i in num:
    if sieve[i] == False:
        print(i)
    else:
        arr = []
        while i > 1:
            if sieve[i] == 0:
                heapq.heappush(arr, i)
                break
            heapq.heappush(arr, sieve[i])
            i //= sieve[i]
        print(*sorted(arr))