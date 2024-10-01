import sys
from collections import deque
import heapq
arr = []
input = sys.stdin.readline
for _ in range(9):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        for k in range(9):
            if j == k or i == k:
                continue
            for l in range(9):
                if l == k or l == j or l == i:
                    continue
                for o in range(9):
                    if o == l or o == k or o == j or o == i:
                        continue
                    for p in range(9):
                        if p == o or p == l or p == k or p == j or p == i:
                            continue
                        for q in range(9):
                            if q == p or q == o or q == l or q == k or q == j or q == i:
                                continue
                            if arr[i] + arr[j] + arr[k] + arr[l] + arr[o] + arr[p] + arr[q] == 100:
                                print(arr[i])
                                print(arr[j])
                                print(arr[k])
                                print(arr[l])
                                print(arr[o])
                                print(arr[p])
                                print(arr[q])
                                exit()

