import sys
import math

sieve = [False] * 100001
for i in range(2, 100001):
    if sieve[i] == False:
        j = i
        while j + i < 100001:
            j += i
            sieve[j] = True

def primeFactors(n, l):
    if n > 1 and not sieve[n]:
        l.append(n)
        return
    for k in range(2, int(math.sqrt(n)) + 1, 2):
        while n % k == 0:
            l.append(k)
            n //= k
    if n > 2:
        l.append(n)

input = sys.stdin.readline
n = int(input())
str = input().split(' ')

mul_d = []
if int(str[0])==0:
    print("mint chocolate")
    exit()
if abs(int(str[0])) != 1 and abs(int(str[0])) != 0:
    primeFactors(abs(int(str[0])), mul_d)
div_d = []
for i in range(1, len(str)):
    if i % 2 == 1:
        if str[i] == '*':
            if int(str[i + 1]) == 0:
                print("mint chocolate")
                exit()
            primeFactors(abs(int(str[i+1])), mul_d)
        elif str[i] == '/':
            primeFactors(abs(int(str[i+1])), div_d)

if len(div_d) == 0:
    print("mint chocolate")
    exit()
for i in set(div_d):
    if mul_d.count(i) < div_d.count(i):
        print("toothpaste")
        exit()
print("mint chocolate")
