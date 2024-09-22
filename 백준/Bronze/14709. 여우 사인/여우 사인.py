import sys

input = sys.stdin.readline
n = int(input())

trues = [(1, 4), (1, 3), (3, 1), (3, 4), (4, 1), (4, 3)]
parents = [-1] * 6
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    parents[y] = x

res = set()
for i in range(n):
    a, b = map(int, input().split())
    if (a, b) not in trues:
        print('Woof-meow-tweet-squeek')
        exit()

    res.add((min(a, b), max(a, b)))

if res == {(1, 3), (1, 4), (3, 4)}:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')