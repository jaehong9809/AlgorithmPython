from collections import deque

TestCase = int(input())


def bfs(startx: int, starty: int, map, visited, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    visited[startx][starty] = True
    q.append([startx, starty])
    while q:
        now = q.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and map[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = True

    return visited


def case():
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    # print(matrix)
    # print(visited)
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and matrix[i][j] == 1:
                visited = bfs(i, j, matrix, visited, n, m)
                cnt += 1
    print(cnt)


for _ in range(TestCase):
    case()
