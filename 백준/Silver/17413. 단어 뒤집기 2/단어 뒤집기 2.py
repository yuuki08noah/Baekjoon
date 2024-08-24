import sys
input = sys.stdin.readline
s = input().strip()
i = 0
while i < len(s):
    if s[i] == '<':
        t = i
        while s[i] != '>':
            i += 1
        print(s[t:i+1], end='')
        i += 1
    else:
        t = i
        while i < len(s) and s[i] != ' ' and s[i] != '<':
            i += 1
        print(s[t:i][::-1], end='')
        if i < len(s) and s[i] == ' ':
            print(' ', end='')
            i += 1