from collections import deque


def bfs(sx, sy, n, m, graph):
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = 0
    while q:
        now = q.popleft()

        for i in range(8):
            nx = dx[i] + now[0]
            ny = dy[i] + now[1]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


def main():
    m, n = map(int, input().split(" "))

    if n == 0 and m == 0:
        return False

    graph = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        tmp = list(map(int, input().split(" ")))

        for j in range(m):
            graph[i][j] = tmp[j]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j, n, m, graph)
                cnt += 1

    print(cnt)
    return True


while True:
    b = main()
    if not b:
        break
