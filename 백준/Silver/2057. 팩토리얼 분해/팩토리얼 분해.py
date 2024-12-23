import sys
input = sys.stdin.readline

n = int(input())
if n == 0: print("NO"); exit()
fac = [1, 1, 2]
for i in range(3, 201):
    fac.append(fac[i - 1] * i)

for i in range(len(fac)-1, -1, -1):
    if n == 0: break
    if fac[i] <= n:
        n -= fac[i]

if n == 0:
    print("YES")
else:
    print("NO")