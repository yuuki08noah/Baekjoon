import itertools

# 입력 받기
n = int(input())

# 1부터 n까지의 숫자 리스트 생성
numbers = list(range(1, n + 1))

# 모든 순열 생성
permutations = itertools.permutations(numbers)

# 각 순열을 출력
for p in permutations:
    print(*p)