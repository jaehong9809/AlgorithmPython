n = int(input())

data = list(map(int, input().split(" ")))

m = int(input())

data.sort()


def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        if data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


targets = list(map(int, input().split(" ")))

for target in targets:
    if binary_search(target, data):
        print(1)
    else:
        print(0)
