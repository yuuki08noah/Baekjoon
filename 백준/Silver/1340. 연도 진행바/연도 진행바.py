import sys
from decimal import Decimal

def isPrime(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

input = sys.stdin.readline
month, day, year, time = input().strip().split()
day = day[:-1]
hour = time.split(":")[0]
minute = time.split(":")[1]
k = (1 if isPrime(int(year)) else 0)
alphamonths = {"January":0, "February":31, "March":59 + k, "April":90 + k, "May":120 + k, "June":151 + k, "July":181 + k, "August":212 + k, "September":243 + k, "October":273 + k, "November":304 + k, "December":334 + k}

total = (365 + (1 if isPrime(int(year)) else 0)) * 24 * 60
user = (alphamonths[month] * 24 + (int(day)-1) * 24) * 60 + int(hour) * 60 + int(minute)
print(f"{Decimal(Decimal(user) / Decimal(total))*Decimal('100')}")