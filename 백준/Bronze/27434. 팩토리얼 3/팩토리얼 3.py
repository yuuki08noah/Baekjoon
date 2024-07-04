def calculate_factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    n = int(input())
    print(calculate_factorial(n))