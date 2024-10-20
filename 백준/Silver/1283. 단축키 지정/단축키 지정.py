import sys

input = sys.stdin.readline
n = int(input())
alphabets = [False] * 26
for i in range(n):
    s = input().strip()
    k = False
    p = False
    l = s.split() if len(s.split()) > 0 else s
    for j in range(len(l)):
        if not alphabets[ord(l[j][0].lower())-97]:
            alphabets[ord(l[j][0].lower())-97] = True
            p = True
            print((' '.join(l[:j]) + ' [' + l[j][0] + ']' + l[j][1:] + ' ' + ' '.join(l[j+1:])).strip(), end='')
            break

    for j in s:
        if p: break
        if j != ' ' and not alphabets[ord(j.lower()) - 97] and not k:
            alphabets[ord(j.lower()) - 97] = True
            k = True
            print(f'[{j}]', end='')
            continue
        print(j, end='')
    print()