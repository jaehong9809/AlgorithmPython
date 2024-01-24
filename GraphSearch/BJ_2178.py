from collections import deque

n, m = map(int, input().split())

map = [[0] * m for _ in range(n)]

for i in range(n):
    str = input()
    for j in range(m):
        map[i][j] = int(str[j])


def bfs(map) -> int:
    q = deque()
    visited = [[False] * m for _ in range(n)]
    q.append([0, 0])
    visited[0][0] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while len(q) != 0:
        now = q.popleft()
        for i in range(4):
            nx = dx[i] + now[0]
            ny = dy[i] + now[1]
            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 1 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    map[nx][ny] = map[now[0]][now[1]] + 1
    return map[n - 1][m - 1]


print(bfs(map))
