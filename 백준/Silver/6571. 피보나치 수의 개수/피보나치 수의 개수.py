import math
import sys

if __name__ == "__main__":
    while True:
        n, m = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0:
            break
        dp = [1, 2]
        cnt = 0
        for i in range(2):
            if dp[i] <= m and dp[i] >= n:
                cnt+=1
        
        for i in range(2, 100000):
            if dp[i-1]+dp[i-2] <= m and dp[i-1]+dp[i-2] >= n:
                cnt+=1
            if dp[i-1]+dp[i-2] > m:
                break
            dp.append(dp[i-1]+dp[i-2])
        print(cnt)