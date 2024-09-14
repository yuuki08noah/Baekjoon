import sys

input = sys.stdin.readline
s = input().strip()
U = False
C_1 = False
P = False
C_2 = False

for i in range(len(s)):
    if s[i] == 'U':
        U = True
    if s[i] == 'C' and not C_1 and U:
        C_1 = True
    if s[i] == 'C' and C_1 and P and U:
        C_2 = True
    if s[i] == 'P' and U and C_1:
        P = True
if U and C_1 and P and C_2:
    print('I love UCPC')
else:
    print('I hate UCPC')