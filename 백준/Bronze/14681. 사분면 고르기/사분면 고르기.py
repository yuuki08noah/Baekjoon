x = int(input())
y = int(input())
res = {(True, True): 1, (False, True):2, (False, False):3, (True, False):4}
print(res[(x>0, y>0)])