n, m = map(int, input().split(" "))

arr = [0 for i in range(m)]
visited = [False for i in range(n+1)]


def dfs(depth: int) -> None:
    global n, m
    if depth == m:
        for i in arr:
            print(i, end=" ")
        print()
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i
            dfs(depth + 1)
            visited[i] = False
dfs(0)