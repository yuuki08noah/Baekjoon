import sys

input = sys.stdin.readline
while True:
    try:
        a, b = input().strip().split()
        a = list(a)
        b = list(b)
        cnt = 0
        last = -1
        for i in a:
            if i in b[last+1:]:
                last += b[last+1:].index(i)+1
                cnt += 1
            else:
                break
        print("Yes" if cnt == len(a) else "No")
    except:
        break