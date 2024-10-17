import sys

input = sys.stdin.readline
s = list(input()[:-1])
pattern = list(input()[:-1])
index = 0
cnt = 0
j = 0
res = []
failure = [0 for _ in range(len(pattern))]

m, begin = 0, 1
while m + begin < len(pattern):
    if pattern[m+begin] == pattern[m]:
        m += 1
        failure[begin + m - 1] = m
    else:
        if m == 0:
            begin += 1
        else:
            begin += (m - failure[m-1])
            m = failure[m - 1]

while index < len(s):
    if s[index] == pattern[j]:
        index += 1
        j += 1
        if j == len(pattern):
            cnt += 1
            res.append(index - j + 1)
            j = failure[j - 1]
    else:
        if j != 0:
            j = failure[j - 1]
        else:
            index += 1

print(cnt)
print(*res)