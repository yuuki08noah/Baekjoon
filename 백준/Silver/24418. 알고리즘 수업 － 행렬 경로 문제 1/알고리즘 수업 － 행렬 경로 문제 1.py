import math
import sys
import heapq
from math import inf
import math

input = sys.stdin.readline
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
# for i in range(n):
#     matrix[i][0] = 0
# for j in range(1, n):
#     matrix[0][j] = 0
# for i in range(1, n):
#     for j in range(1, n):
#         matrix[i][j] += matrix[i][j] + max(matrix[i-1][j], matrix[i][j-1])
print(math.factorial(2*n)//(math.factorial(n)**2), n**2)