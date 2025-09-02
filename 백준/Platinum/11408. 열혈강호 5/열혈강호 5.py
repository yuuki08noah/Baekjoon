import sys
from collections import deque
input = sys.stdin.readline

INF = 10**15

class MinCostMaxFlow:
    def __init__(self, vertex_count: int):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, from_vertex: int, to_vertex: int, capacity: int, edge_cost: int):
        # forward edge
        self.adjacency_list[from_vertex].append([to_vertex, capacity, edge_cost, len(self.adjacency_list[to_vertex])])
        # backward edge
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
            current_vertex = queue.popleft()
            in_queue[current_vertex] = False
            for edge_index, (next_vertex, capacity, edge_cost, reverse_index) in enumerate(self.adjacency_list[current_vertex]):
                if capacity > 0 and distance[next_vertex] > distance[current_vertex] + edge_cost:
                    distance[next_vertex] = distance[current_vertex] + edge_cost
                    previous_vertex[next_vertex] = current_vertex
                    previous_edge_index[next_vertex] = edge_index
                    if not in_queue[next_vertex]:
                        in_queue[next_vertex] = True
                        queue.append(next_vertex)

        if distance[sink] == INF:
            return 0, 0, None, None

        current_vertex = sink
        while current_vertex != source:
            prev_vertex = previous_vertex[current_vertex]
            prev_edge_idx = previous_edge_index[current_vertex]
            edge = self.adjacency_list[prev_vertex][prev_edge_idx]

            edge[1] -= 1  # forward 간선 용량 줄이기
            self.adjacency_list[current_vertex][edge[3]][1] += 1  # backward 간선 용량 늘리기

            current_vertex = prev_vertex

        return 1, distance[sink], previous_vertex, previous_edge_index

    def flow(self, source: int, sink: int):
        total_flow, total_cost = 0, 0
        while True:
            augment_flow, augment_cost, _, _ = self.spfa(source, sink)
            if augment_flow == 0:  # 더 이상 경로 없음
                break
            total_flow += augment_flow
            total_cost += augment_cost
        return total_flow, total_cost


def solve():
    n, m = map(int, input().split())
    source, sink = 0, n + m + 1
    vertex_count = sink + 1
    mcmf = MinCostMaxFlow(vertex_count)

    # source → U
    for u in range(1, n + 1):
        mcmf.add_edge(source, u, 1, 0)

    # V → sink
    for v in range(1, m + 1):
        mcmf.add_edge(n + v, sink, 1, 0)

    # U → V (입력 간선)
    for u in range(1, n+1):
        arr = list(map(int, input().split()))
        k = arr[0]
        for j in range(k):
            v, cost = arr[1+j*2], arr[2+j*2]
            mcmf.add_edge(u, n + v, 1, cost)

    max_flow, min_cost = mcmf.flow(source, sink)
    print(max_flow, min_cost, sep='\n')

if __name__ == "__main__":
    solve()