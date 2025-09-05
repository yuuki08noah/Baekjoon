import sys
from collections import deque
input = sys.stdin.readline

INF = 10**18  # 여유 있게

class MinCostMaxFlow:
    def __init__(self, vertex_count: int):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, from_vertex: int, to_vertex: int, capacity: int, edge_cost: int):
        self.adjacency_list[from_vertex].append([to_vertex, capacity, edge_cost, len(self.adjacency_list[to_vertex])])
        self.adjacency_list[to_vertex].append([from_vertex, 0, -edge_cost, len(self.adjacency_list[from_vertex]) - 1])

    def spfa(self, source: int, sink: int):
        distance = [INF] * self.vertex_count
        in_queue = [False] * self.vertex_count
        previous_vertex = [-1] * self.vertex_count
        previous_edge_index = [-1] * self.vertex_count

        distance[source] = 0
        queue = deque([source])
        in_queue[source] = True

        while queue:
            u = queue.popleft()
            in_queue[u] = False
            for ei, (v, cap, cost, rev) in enumerate(self.adjacency_list[u]):
                if cap > 0 and distance[v] > distance[u] + cost:
                    distance[v] = distance[u] + cost
                    previous_vertex[v] = u
                    previous_edge_index[v] = ei
                    if not in_queue[v]:
                        in_queue[v] = True
                        queue.append(v)

        if distance[sink] == INF:
            return 0, 0, None, None
        return 1, distance[sink], previous_vertex, previous_edge_index

    def flow(self, source: int, sink: int):
        total_f = 0
        total_c = 0
        while True:
            found, path_cost, pv, pe = self.spfa(source, sink)
            if not found:
                break
            # 병목 용량
            v = sink
            delta = INF
            while v != source:
                u = pv[v]; ei = pe[v]
                delta = min(delta, self.adjacency_list[u][ei][1])
                v = u
            # 흘리기
            v = sink
            while v != source:
                u = pv[v]; ei = pe[v]
                to, cap, cost, rev = self.adjacency_list[u][ei]
                self.adjacency_list[u][ei][1] -= delta
                self.adjacency_list[v][rev][1] += delta
                v = u
            total_f += delta
            total_c += path_cost * delta
        return total_f, total_c


def solve():
    # N: 사람 수, M: 서점 수
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))  # 사람 j의 수요 Aj (j=1..N)
    B = [0] + list(map(int, input().split()))  # 서점 i의 재고 Bi (i=1..M)

    # 노드: S=0, store:1..M, person:M+1..M+N, T=M+N+1
    S, T = 0, M + N + 1
    V = T + 1
    mcmf = MinCostMaxFlow(V)

    # S -> store i (용량 Bi)
    for i in range(1, M + 1):
        mcmf.add_edge(S, i, B[i], 0)

    # 비용 행: M줄, 각 줄에 N개 (i번째 줄: 서점 i -> 사람 j 비용 Cij)
    costs = []
    for i in range(1, M + 1):
        row = [0] + list(map(int, input().split()))
        if len(row) != N + 1:
            # 방어: 입력 형식이 틀리면 여기서 바로 알림
            raise ValueError(f"{i}번째 비용 행 길이 {len(row)-1} != N({N})")
        costs.append(row)

    # store i -> person j (큰 용량, 비용 Cij)
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            mcmf.add_edge(i, M + j, INF, costs[i-1][j])

    # person j -> T (용량 Aj)
    for j in range(1, N + 1):
        mcmf.add_edge(M + j, T, A[j], 0)

    _, min_cost = mcmf.flow(S, T)
    print(min_cost)

if __name__ == "__main__":
    solve()