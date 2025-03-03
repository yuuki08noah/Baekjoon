n = int(input())
for _ in range(int(input())):
    n -= (lambda x: x[0]*x[1])(list(map(int, input().split())))
print("No" if n else "Yes")