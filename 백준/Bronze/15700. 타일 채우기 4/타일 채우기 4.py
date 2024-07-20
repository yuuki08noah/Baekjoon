from queue import PriorityQueue
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    print(n*m//2)

if __name__ == "__main__":
    main()