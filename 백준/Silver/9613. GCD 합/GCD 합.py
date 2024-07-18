def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
def main():
    t = int(input())
    for i in range(t):
        sum = 0
        n = list(map(int, input().split()))
        for j in range(1, len(n)):
            for k in range(j+1, len(n)):
                sum+=gcd(n[j], n[k])
        print(sum)

if __name__ == "__main__":
    main()