import sys

input = sys.stdin.readline
while True:
    str = input()
    if str == '.\n':
        break
    stack = []
    flag = True
    for char in str:
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']':
            if not stack:
                flag = False
                print("no")
                break

            if stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                print("no")
                break
        elif char == ')':
            if not stack:
                flag = False
                print("no")
                break

            if stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                print("no")
                break
    if len(stack) > 0 and flag:
        print("no")
        continue
    if flag:
        print("yes")
