from collections import deque

n = int(input())
q = deque()
for i in range(1, n + 1):
    q.append(i)

while True:
    if len(q) == 1:
        print(q.pop())
        break

    q.popleft()
    q.append(q.popleft())
