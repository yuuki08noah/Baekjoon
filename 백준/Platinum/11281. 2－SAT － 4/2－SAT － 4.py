import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    global num
    for vertex in graph[n]:
        if not visited[vertex]:
            visited[vertex] = True
            dfs(vertex)
    numbers[n][0] = num
    num += 1

def dfs2nd(n, li):
    group[n] = p
    li.append(n)
    for vertex in graph_inversed[n]:
        if not visited_inversed[vertex]:
            visited_inversed[vertex] = True
            dfs2nd(vertex, li)


v, e = map(int, input().split())
graph = {i:[] for i in range(-v, v + 1)}
graph_inversed = {i:[] for i in range(-v, v+1)}
visited = {i:False for i in range(-v, v+1)}
visited_inversed = {i:False for i in range(-v, v+1)}
numbers = {i:[0, i] for i in range(-v, v + 1)}
group = [0] * (2*v + 1)
num = 1
p = 0

for i in range(e):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)
    graph_inversed[b].append(-a)
    graph_inversed[a].append(-b)

for i in range(-v, v + 1):
    if i == 0:
        continue
    if not visited[i]:
        dfs(i)

por = sorted(numbers.values(), key = lambda x:x[0], reverse = True)

re = []
for i in por:
    r = []
    if i[1] == 0: continue
    if not visited_inversed[i[1]]:
        visited_inversed[i[1]] = True
        dfs2nd(i[1], r)
        p += 1
    re.append(r)

flag = 1
for i in range(1, v+1):
    if i == 0: continue
    if group[i] == group[-i]:
        flag = 0
print(flag)
if flag == 0:
    exit()
tf = {i:False for i in range(-v, v + 1)}
for k in re:
    for j in k:
        tf[j] = True
        tf[-j] = False

for key, value in tf.items():
    if key > 0:
        print(int(value), end=' ')