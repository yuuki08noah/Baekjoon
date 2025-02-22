s = list(input().strip())
for k in s:
    print(k.lower() if k.isupper() else k.upper(), end='')