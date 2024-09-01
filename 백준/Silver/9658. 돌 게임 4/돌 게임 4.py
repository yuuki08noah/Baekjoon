import sys

input = sys.stdin.readline
n = int(input())
if n % 7 == 3 or n % 7 == 1:
    print('CY')
else:
    print('SK')