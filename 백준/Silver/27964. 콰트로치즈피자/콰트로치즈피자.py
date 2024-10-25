import sys
input = sys.stdin.readline
n = int(input())
arr = input().strip().split()
cheese = set()
for s in arr:
    if s.endswith("Cheese"):
        cheese.add(s)

print("yummy" if len(cheese) > 3 else "sad")