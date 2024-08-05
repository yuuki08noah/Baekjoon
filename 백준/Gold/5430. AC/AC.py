import sys
from collections import deque

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    arr_input = input().strip()[1:-1]

    if arr_input:
        arr = deque(map(int, arr_input.split(',')))
    else:
        arr = deque()

    reverse = False
    error = False

    for command in p:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                error = True
                break

    if not error:
        if reverse:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')
