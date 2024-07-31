import decimal
import sys
import math
import heapq
sys.set_int_max_str_digits(100000000)
input = sys.stdin.readline
n = int(input())
zeros = 0
fac = math.factorial(n)
while True:
    zeros += n // 5
    if n // 5 == 0:
        break
    n //= 5
print((fac//(10**zeros))%10)