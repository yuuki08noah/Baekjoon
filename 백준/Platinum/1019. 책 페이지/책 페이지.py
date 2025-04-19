import sys

input = sys.stdin.readline
n = int(input())
arr = [0] * 10
p = 1

def calc(k, l):
    while k > 0:
        arr[k % 10] += l
        k //= 10

while n > 0:
    while n % 10 != 9 and n > 0:
        calc(n, p)
        n -= 1
    if n == 0: break
    for i in range(10):
        arr[i] += (n // 10 + 1) * p
    arr[0] -= p
    n //= 10
    p *= 10
print(*arr)