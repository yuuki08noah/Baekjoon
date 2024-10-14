import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(int(input())):
    h, w = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(list(map(str, input().strip())))
    keys = set(map(str, input().strip()))
    after = {}
    queue = deque()
    dollar = set()
    for i in range(h):
        if board[i][0] == '.' or (board[i][0].isupper() and board[i][0].lower() in keys):
            queue.append((i, 0))
        elif board[i][0].islower() and board[i][0].isalpha():
            queue.append((i, 0))
            keys.add(board[i][0].lower())
        elif board[i][0].isupper() and board[i][0].lower() not in keys:
            if board[i][0].lower() in after:
                after[board[i][0].lower()].append((i, 0))
            else:
                after[board[i][0].lower()] = [(i, 0)]
        elif board[i][0] == '$':
            dollar.add((i, 0))
            queue.append((i, 0))
        if board[i][w-1] == '.' or (board[i][w-1].isupper() and board[i][w-1].lower() in keys):
            queue.append((i, w-1))
        elif board[i][w-1].islower() and board[i][w-1].isalpha():
            queue.append((i, w-1))
            keys.add(board[i][w-1].lower())
        elif board[i][w-1].isupper() and board[i][w-1].lower() not in keys:
            if board[i][w-1].lower() in after:
                after[board[i][w-1].lower()].append((i, w-1))
            else:
                after[board[i][w-1].lower()] = [(i, w-1)]
        elif board[i][w-1] == '$':
            dollar.add((i, w-1))
            queue.append((i, w-1))
    for i in range(w):
        if board[0][i] == '.' or (board[0][i].isupper() and board[0][i].lower() in keys):
            queue.append((0, i))
        elif board[0][i].islower() and board[0][i].isalpha():
            keys.add(board[0][i].lower())
            queue.append((0, i))
        elif board[0][i].isupper() and board[0][i].lower() not in keys:
            if board[0][i].lower() in after:
                after[board[0][i].lower()].append((0, i))
            else:
                after[board[0][i].lower()] = [(0, i)]
        elif board[0][i] == '$':
            dollar.add((0, i))
            queue.append((i, 0))
        if board[h-1][i] == '.' or (board[h-1][i].isupper() and board[h-1][i].lower() in keys):
            queue.append((h-1, i))
        elif board[h-1][i].islower() and board[h-1][i].isalpha():
            queue.append((h-1, i))
            keys.add(board[h-1][i].lower())
        elif board[h-1][i].isupper() and board[h-1][i].lower() not in keys:
            if board[h-1][i].lower() in after:
                after[board[h-1][i].lower()].append((h-1, i))
            else:
                after[board[h-1][i].lower()] = [(h-1, i)]
        elif board[h-1][i] == '$':
            dollar.add((h-1, i))
            queue.append((h-1, i))
    for key in after.keys():
        if key in keys:
            for i in after[key]:
                queue.append(i)
            after[key].clear()
    # print(keys)
    while queue:
        x, y = queue.popleft()
        if board[x][y] == '^':
            continue
        board[x][y] = '^'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == '.':
                    queue.append((nx, ny))
                elif board[nx][ny] == '$':
                    dollar.add((nx, ny))
                    queue.append((nx, ny))
                elif board[nx][ny].islower():
                    keys.add(board[nx][ny].lower())
                    if board[nx][ny] in after:
                        for k in after[board[nx][ny]]:
                            queue.append(k)
                        after[board[nx][ny]].clear()
                    queue.append((nx, ny))
                elif board[nx][ny].isupper():
                    if board[nx][ny].lower() in keys:
                        queue.append((nx, ny))
                    else:
                        if board[nx][ny].lower() in after:
                            after[board[nx][ny].lower()].append((nx, ny))
                        else:
                            after[board[nx][ny].lower()] = [(nx, ny)]
    print(len(dollar))