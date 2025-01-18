import sys

input = sys.stdin.readline
n, m = map(int, input().split())
package = []
single = []
cost = 0
for i in range(m):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)
package.sort()
single.sort()

while n > 0:
    if single[0]*n < package[0]*(n/6 if n/6 > 1 else 1):
        cost += single[0]*n
        n -= n
    else:
        n -= 6
        cost += package[0]
print(cost)
