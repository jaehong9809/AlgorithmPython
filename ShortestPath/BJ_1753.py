import heapq
import sys

input = sys.stdin.readline
v, e = map(int, input().split(" "))
start_node = int(input())
INF = int(1e9)

graph = [[] for _ in range(v + 1)]
d = [INF for _ in range(v + 1)]

for _ in range(e):
    start, end, w = map(int, input().split(" "))
    sign = False
    graph[start].append([end, w])

def dijkstra(start_node: int):
    q = []
    heapq.heappush(q, [0, start_node])
    d[start_node] = 0

    while q:
        cost, now = heapq.heappop(q)
        if d[now] < cost:
            continue

        for i in graph[now]:
            next = cost + i[1]
            if d[i[0]] > next:
                d[i[0]] = next
                heapq.heappush(q, [next, i[0]])


dijkstra(start_node)

for i in range(1, v + 1):
    if d[i]==INF:
        print("INF")
    else:
        print(d[i])
