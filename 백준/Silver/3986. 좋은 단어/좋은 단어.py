import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
for _ in range(n):
    str = input()
    if str.count('A') % 2 == 1 or str.count('B') % 2 == 1:
        continue
    check = []
    for i in range(len(str)):
        # print(check)
        if str[i] == 'A':
            if len(check) != 0 and check[-1] == 'A':
                del check[-1]
            else:
                check.append(str[i])
        if str[i] == 'B':
            if len(check) != 0 and check[-1] == 'B':
                del check[-1]
            else:
                check.append(str[i])
    if len(check) == 0:
        cnt += 1
print(cnt)
