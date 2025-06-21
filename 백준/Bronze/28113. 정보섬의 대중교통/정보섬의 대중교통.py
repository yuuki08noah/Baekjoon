n, a, b = map(int, input().split())
if b > a:
    print("Bus")
elif a > b:
    print("Subway")
else:
    print("Anything")