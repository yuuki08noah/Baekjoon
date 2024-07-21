import sys

def main():
    fib = [0, 1]
    n = int(sys.stdin.readline())
    for i in range(2, abs(n)+1):
        fib.append((fib[i-1] + fib[i-2])%1000000000)

    if n>0:
        print(f'1\n{fib[n]%1000000000}')
    elif n==0:
        print(f'0\n{fib[n]%1000000000}')
    else:
        if n%2==0:
            print(f'-1\n{fib[-(n)]%1000000000}')
        else:
            print(f'1\n{fib[-(n)]%1000000000}')


if __name__ == "__main__":
    main()

