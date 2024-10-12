import sys

input = sys.stdin.readline
n, m = map(int, input().split())
words = {}
for i in range(n):
    word = input().strip()
    if len(word) >= m:
        if word in words:
            words[word][0] += 1
        else:
            words[word] = [1, len(word), word]

sd = sorted(words, key=lambda x: (-words[x][0], -words[x][1], words[x][2]))
for i in sd:
    print(i)