import sys
input = sys.stdin.readline
q = int(input())
fives = [0] * (10**7 + 1)
fives[1] = 5
fives[2] = 20
for i in range(3, 10**7+1):
    fives[i] = (fives[i - 1] * 5)%(10**9+7)

for k in range(q):
    print(fives[int(input())])