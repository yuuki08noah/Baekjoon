import sys

input = sys.stdin.readline
s = input().strip()
cnt = 0
while len(s) != 1:
    t = 0
    for k in s:
        t += int(k)
    s = str(t)
    cnt += 1
print(cnt)
print("NO" if int(s) % 3 else "YES")