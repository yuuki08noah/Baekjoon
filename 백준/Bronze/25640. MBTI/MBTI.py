s = input().strip()
cnt = 0
n = int(input())
for _ in range(n):
    if input().strip() == s:
        cnt += 1
print(cnt)