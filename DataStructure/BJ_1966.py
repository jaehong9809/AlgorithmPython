from collections import deque

TestCase = int(input())


def run_function():
    n, m = map(int, input().split(" "))
    data = list(map(int, input().split(" ")))
    MaxNumbers = data.copy()
    MaxNumbers.sort(reverse=True)
    MNIndex = 0
    data = [[data[i], i] for i in range(n)]

    queue = deque(data)
    cnt = 0
    while queue:
        now = queue.popleft()
        if MaxNumbers[MNIndex] == now[0]:
            cnt += 1
            if now[1] == m:
                break
            else:
                MNIndex += 1
        else:
            queue.append(now)
    print(cnt)


for _ in range(TestCase):
    run_function()
