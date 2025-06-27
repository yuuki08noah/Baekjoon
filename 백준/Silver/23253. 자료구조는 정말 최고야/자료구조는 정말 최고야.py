import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
top = defaultdict(tuple)
st = []
for i in range(m):
    k = int(input())
    b = list(map(int, input().split()))
    st.append((k, b))
    top[b[-1]] = (i, -1)


for i in range(1, n+1):
    if top[i] != ():
        if -top[i][1] != st[top[i][0]][0]:
            top[st[top[i][0]][1][top[i][1]-1]] = (top[i][0], top[i][1]-1)
        top[i] = ()
        flag = False
    else:
        print("No")
        exit()
print("Yes")




