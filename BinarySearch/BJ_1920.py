import bisect

def binary_search(data: list, target: int) -> int:
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


n: int = int(input())
data = list(map(int, input().split(" ")))

data.sort()

m: int = int(input())

target = list(map(int, input().split(" ")))

for i in target:
    if binary_search(data, i) != -1:
        print(1)
    else:
        print(0)
