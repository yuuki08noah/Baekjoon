l = sorted([int(input()) for _ in range(9)])

def dfs(n, li):
    if len(li) < 7:
        for j in range(9):
            if l[j] not in li:
                dfs(j, li+[l[j]])

    elif len(li) == 7:
        if sum(li) == 100:
            print(*li, sep='\n')
            exit()
        else:
            return
    else:
        return

for i in range(9):
    dfs(i, [l[i]])