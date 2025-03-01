s = input().strip()
print(f"{69-ord(s[0])+((-0.3 if s[1] == '-' else 0 if s[1] == '0' else 0.3) if len(s) > 1 else 1):.1f}")