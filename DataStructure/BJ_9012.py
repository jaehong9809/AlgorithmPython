from collections import deque

n = int(input())


def check() -> bool:
    inputstr = input()
    st = deque()
    for i in inputstr:
        if i == '(':
            st.append(i)
        else:
            if len(st) == 0 or st[-1] != '(':
                return False
            else:
                st.pop()
    if len(st) != 0:
        return False
    else:
        return True


for _ in range(n):
    if check():
        print("YES")
    else:
        print("NO")
